import sys
import selectors
import json
import io
import struct
import socket
import ssl
import controllers.mainwindow as maincontroller
import PySide2.QtCore as QtCore

request_search = {
    "morpheus": "Follow the white rabbit. \U0001f430",
    "ring": "In the caves beneath the Misty Mountains. \U0001f48d",
    "\U0001f436": "\U0001f43e Playing ball! \U0001f3d0",
}


class Message(QtCore.QObject):
    addNetNodeInUse = QtCore.Signal(object)
    removeNetNodeInUse = QtCore.Signal(object)
    update_waveform_signal = QtCore.Signal(object)
    update_fft_signal = QtCore.Signal(object)
    update_spectrogram_signal = QtCore.Signal(object)
    update_rt_node_status = QtCore.Signal(object)
    # checkNodeInUseSignal = QtCore.Signal(object)
    def __init__(self, selector, sock, addr, controller):
        super().__init__()
        self.selector = selector
        self.sock = sock
        self.controller = controller
        self.addr = addr
        self._recv_buffer = b""
        self._send_buffer = b""
        self._jsonheader_len = None
        self.jsonheader = None
        self.request = None
        self.response_created = False

        #Signals and Slots Connections
        self.addNetNodeInUse.connect(self.controller.addNetNodeInUse)
        self.removeNetNodeInUse.connect(self.controller.removeNetNodeInUse)
        # self.checkNodeInUseSignal.connect(self.controller.checkIfNetNodeInUse)
        self.update_waveform_signal.connect(self.controller.update_waveform)
        self.update_fft_signal.connect(self.controller.update_fft)
        self.update_spectrogram_signal.connect(self.controller.update_spectrogram)
        self.update_rt_node_status.connect(self.controller.update_rt_status)

    def _set_selector_events_mask(self, mode):
        """Set selector to listen for events: mode is 'r', 'w', or 'rw'."""
        if mode == "r":
            events = selectors.EVENT_READ
        elif mode == "w":
            events = selectors.EVENT_WRITE
        elif mode == "rw":
            events = selectors.EVENT_READ | selectors.EVENT_WRITE
        else:
            raise ValueError(f"Invalid events mask mode {mode!r}.")
        self.selector.modify(self.sock, events, data=self)

    def _read(self):
        try:
            # Should be ready to read
            data = self.sock.recv(16384)
        except ssl.SSLError as e:
            # Resource temporarily unavailable (errno EWOULDBLOCK)
            if e.errno != ssl.SSL_ERROR_WANT_READ and e.errno != ssl.SSL_ERROR_WANT_WRITE:
                raise
            pass
        else:
            if data:
                self._recv_buffer += data
            else:
                raise RuntimeError("Peer closed.")

    def _write(self):
        if self._send_buffer:
            # print(f"Sending {self._send_buffer!r} to {self.addr}")
            try:
                # Should be ready to write
                sent = self.sock.send(self._send_buffer)
            except ssl.SSLError as e:
                # Resource temporarily unavailable (errno EWOULDBLOCK)
                if e.errno != ssl.SSL_ERROR_WANT_READ and e.errno != ssl.SSL_ERROR_WANT_WRITE:
                    raise
                pass
            else:
                self._send_buffer = self._send_buffer[sent:]
                # Close when the buffer is drained. The response has been sent.
                if sent and not self._send_buffer:
                    self.close()

    def _json_encode(self, obj, encoding):
        return json.dumps(obj, ensure_ascii=False).encode(encoding)

    def _json_decode(self, json_bytes, encoding):
        tiow = io.TextIOWrapper(
            io.BytesIO(json_bytes), encoding=encoding, newline=""
        )
        obj = json.load(tiow)
        tiow.close()
        return obj

    def _create_message(
        self, *, content_bytes, content_type, content_encoding
    ):
        jsonheader = {
            "byteorder": sys.byteorder,
            "content-type": content_type,
            "content-encoding": content_encoding,
            "content-length": len(content_bytes),
        }
        jsonheader_bytes = self._json_encode(jsonheader, "utf-8")
        message_hdr = struct.pack(">H", len(jsonheader_bytes))
        message = message_hdr + jsonheader_bytes + content_bytes
        return message

    def _create_response_json_content(self):
        action = self.request.get("action")
        if action == "search":
            query = self.request.get("value")
            answer = request_search.get(query) or f"No match for '{query}'."
            content = {"result": answer}
        elif action == "get_netnodes_in_use":
            answer = self.controller.getNetNodesIDInUse()
            content = {"action": action,
                       "result": answer}
        elif action == "add_node_in_use":
            nodesDict = self.request.get("value")
            self.addNetNodeInUse.emit(nodesDict)
            content = {"action": action,
                       "result": "Done"}
        elif action == "disconnect_net_node":
            netNodeId = self.request.get("value")
            self.removeNetNodeInUse.emit(netNodeId)
            content = {"action": action,
                       "result": "Done"}
        elif action == "check_if_net_in_use":
            netNodeId = self.request.get("value")
            answer = self.controller.checkIfNetNodeInUse(netNodeId)
            content = {"action": action,
                       "result": answer,
                       "nodeId": netNodeId}
        elif action == "update_waveform":
            values_dict = self.request.get("value")
            x = values_dict.get("x")
            y = values_dict.get("y")
            ptr = values_dict.get("ptr")
            values_list = [x, y, ptr]
            self.update_waveform_signal.emit(values_list)
            content = {"action": action,
                       "result": "Done"}
        elif action == "update_fft":
            values = self.request.get("value")
            self.update_fft_signal.emit(values)
            content = {"action": action,
                       "result": "Done"}
        elif action == "update_spectrogram":
            values = self.request.get("value")
            self.update_spectrogram_signal.emit(values)
            # self.controller.update_spectrogram(values)
            content = {"action": action,
                       "result": "Done"}
        elif action == "request_creation":
            content = {"action": action,
                       "result": True}
        elif action == "update_rt_node":
            rtNodeDict = self.request.get("value")
            self.update_rt_node_status.emit(rtNodeDict)
            content = {"action": action,
                       "result": "Done"}
        else:
            content = {"result": f"Error: invalid action '{action}'."}
        content_encoding = "utf-8"
        response = {
            "content_bytes": self._json_encode(content, content_encoding),
            "content_type": "text/json",
            "content_encoding": content_encoding,
        }
        return response

    def _create_response_binary_content(self):
        response = {
            "content_bytes": b"First 10 bytes of request: "
            + self.request[:10],
            "content_type": "binary/custom-server-binary-type",
            "content_encoding": "binary",
        }
        return response

    def process_events(self, mask):
        if mask & selectors.EVENT_READ:
            self.read()
        if mask & selectors.EVENT_WRITE:
            self.write()

    def read(self):
        self._read()

        if self._jsonheader_len is None:
            self.process_protoheader()

        if self._jsonheader_len is not None:
            if self.jsonheader is None:
                self.process_jsonheader()

        if self.jsonheader:
            if self.request is None:
                self.process_request()

    def write(self):
        if self.request:
            if not self.response_created:
                self.create_response()

        self._write()

    def close(self):
        # print(f"Closing connection to {self.addr}")
        try:
            self.selector.unregister(self.sock)
        except Exception as e:
            print(
                f"Error: selector.unregister() exception for "
                f"{self.addr}: {e!r}"
            )

        try:
            self.sock.shutdown(socket.SHUT_RDWR)
            self.sock.close()
        except ssl.SSLError as e:
            print(f"Error: socket.close() exception for {self.addr}: {e!r}")
        finally:
            # Delete reference to socket object for garbage collection
            self.sock = None

    def process_protoheader(self):
        hdrlen = 2
        if len(self._recv_buffer) >= hdrlen:
            self._jsonheader_len = struct.unpack(
                ">H", self._recv_buffer[:hdrlen]
            )[0]
            self._recv_buffer = self._recv_buffer[hdrlen:]

    def process_jsonheader(self):
        hdrlen = self._jsonheader_len
        if len(self._recv_buffer) >= hdrlen:
            self.jsonheader = self._json_decode(
                self._recv_buffer[:hdrlen], "utf-8"
            )
            self._recv_buffer = self._recv_buffer[hdrlen:]
            for reqhdr in (
                "byteorder",
                "content-length",
                "content-type",
                "content-encoding",
            ):
                if reqhdr not in self.jsonheader:
                    raise ValueError(f"Missing required header '{reqhdr}'.")

    def process_request(self):
        content_len = self.jsonheader["content-length"]
        if not len(self._recv_buffer) >= content_len:
            return
        data = self._recv_buffer[:content_len]
        self._recv_buffer = self._recv_buffer[content_len:]
        if self.jsonheader["content-type"] == "text/json":
            encoding = self.jsonheader["content-encoding"]
            self.request = self._json_decode(data, encoding)
            # print(f"Received request {self.request!r} from {self.addr}")
        else:
            # Binary or unknown content-type
            self.request = data
            print(
                f"Received {self.jsonheader['content-type']} "
                f"request from {self.addr}"
            )
        # Set selector to listen for write events, we're done reading.
        self._set_selector_events_mask("w")

    def create_response(self):
        if self.jsonheader["content-type"] == "text/json":
            response = self._create_response_json_content()
        else:
            # Binary or unknown content-type
            response = self._create_response_binary_content()
        message = self._create_message(**response)
        self.response_created = True
        self._send_buffer += message
