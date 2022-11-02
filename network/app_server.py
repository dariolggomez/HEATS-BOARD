#!/usr/bin/env python3

import sys
import socket
import ssl
import selectors
from datetime import datetime
from threading import Thread
import traceback
import PySide2.QtCore as QtCore
import network.libserver as libserver

class ServerController(QtCore.QObject):
    consoleMessageSignal = QtCore.Signal(str)
    def __init__(self, mainWindow):
        super().__init__()
        self.mainWindow_controller = mainWindow
        self.consoleMessageSignal.connect(self.mainWindow_controller.showConsoleMessage)
        self.create_ssl_context()


    def accept_wrapper(self, sel, sock, addr):
        # conn, addr = sock.accept()  # Should be ready to read
        # print(f"Accepted connection from {addr}")
        sock.settimeout(10)
        conn = self.ssl_context.wrap_socket(sock, server_side=True)
        conn.setblocking(False)
        message = libserver.Message(sel, conn, addr, self.mainWindow_controller)
        sel.register(conn, selectors.EVENT_READ, data=message)

    def create_ssl_context(self):
        self.ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        self.ssl_context.load_cert_chain(certfile="security/server.crt", keyfile="security/server.key")

    # if len(sys.argv) != 3:
    #     print(f"Usage: {sys.argv[0]} <host> <port>")
    #     sys.exit(1)


    def start_server(self, host, port):
        self.sel = selectors.DefaultSelector()
        self.lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Avoid bind() exception: OSError: [Errno 48] Address already in use
        self.lsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.lsock.bind((host, port))
        self.lsock.listen(5)
        print(f"Listening on {(host, port)}")
        self.consoleMessageSignal.emit(f"Servidor iniciado >> {host} : {port}")
        self.lsock.setblocking(False)
        self.sel.register(self.lsock, selectors.EVENT_READ, data=None)
        self.serverRunning = True

        try:
            while True:
                events = self.sel.select(timeout=0.01)
                if(not self.serverRunning):
                    break
                for key, mask in events:
                    if key.data is None:
                        conn, addr = key.fileobj.accept()
                        # self.accept_wrapper(self.sel, conn, addr, controllerInstance)
                        handshaker_thread = Thread(target=self.accept_wrapper, args=(self.sel, conn, addr))
                        handshaker_thread.daemon = True
                        handshaker_thread.start()
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
            self.consoleMessageSignal.emit(f"Servidor apagado")
        except Exception as e:
            print(f"Ocurrió un error al intentar apagar el servidor.\nException:{e}")

