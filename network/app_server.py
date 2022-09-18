#!/usr/bin/env python3

import sys
import socket
import selectors
import traceback
import PySide2.QtCore as QtCore
import network.libserver as libserver

class ServerController(QtCore.QObject):
    def __init__(self):
        super().__init__()


    def accept_wrapper(self, sel, sock, controllerInstance):
        conn, addr = sock.accept()  # Should be ready to read
        print(f"Accepted connection from {addr}")
        conn.setblocking(False)
        message = libserver.Message(sel, conn, addr, controllerInstance)
        sel.register(conn, selectors.EVENT_READ, data=message)


    # if len(sys.argv) != 3:
    #     print(f"Usage: {sys.argv[0]} <host> <port>")
    #     sys.exit(1)


    def start_server(self, host, port, controllerInstance):
        self.sel = selectors.DefaultSelector()
        self.lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Avoid bind() exception: OSError: [Errno 48] Address already in use
        self.lsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.lsock.bind((host, port))
        self.lsock.listen()
        print(f"Listening on {(host, port)}")
        self.lsock.setblocking(False)
        self.sel.register(self.lsock, selectors.EVENT_READ, data=None)
        self.serverRunning = True

        try:
            while True:
                events = self.sel.select(timeout=None)
                if(not self.serverRunning):
                    break
                for key, mask in events:
                    if key.data is None:
                        self.accept_wrapper(self.sel, key.fileobj, controllerInstance)
                    else:
                        message = key.data
                        try:
                            message.process_events(mask)
                        except Exception:
                            print(
                                f"Main: Error: Exception for {message.addr}:\n"
                                f"{traceback.format_exc()}"
                            )
                            message.close()
        except Exception as e:
            print(e)

    def stop_server(self):
        self.serverRunning = False
        try:
            self.lsock.close()
            self.lsock = None
            self.sel.close()
            print("Servidor apagado.")
        except Exception as e:
            print(f"Ocurrió un error al intentar apagar el servidor.\nException:{e}")

