import socket
import os

BUFFER_SIZE = 4096

def connectToHost(mainWindow, SERVER_HOST, SERVER_PORT):
    connectionStablished = False
    socket_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        socket_s.connect((SERVER_HOST, SERVER_PORT))
        connectionStablished = True
    except:
        mainWindow.ui.console.insertPlainText(f"CONSOLA >> No se pudo conectar al servidor >> {SERVER_HOST} : {SERVER_PORT}\r")
        mainWindow.ui.connectBtn.setEnabled(True)
        socket_s.close()
    if(connectionStablished):
        mainWindow.ui.console.insertPlainText(f"CONSOLA >> Conexión establecida al servidor >> {SERVER_HOST} : {SERVER_PORT}\r")
        filename = "network/log.txt"
        with open(filename, "wb") as file:
            while True:
                bytes_read = socket_s.recv(BUFFER_SIZE)
                if not bytes_read:
                    break
                file.write(bytes_read)
        
        mainWindow.ui.console.insertPlainText(f"CONSOLA >> Archivo recibido.\r")
        socket_s.close()
        mainWindow.ui.connectBtn.setEnabled(True)
    
