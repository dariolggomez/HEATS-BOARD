import socket
import os

BUFFER_SIZE = 4096

def connectToHost(mainWindow, SERVER_HOST, SERVER_PORT):
    socket_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        socket_s.connect((SERVER_HOST, SERVER_PORT))
    except:
        mainWindow.ui.console.appendPlainText(f"No se pudo conectar al servidor {SERVER_HOST}:{SERVER_PORT}")
        mainWindow.ui.console.setFocus()
        # print(f"No se pudo conectar al servidor {SERVER_HOST}:{SERVER_PORT}")
        return

    print(f"Conexión establecida al servidor {SERVER_HOST}:{SERVER_PORT}")
    filename = "network/log.txt"
    with open(filename, "wb") as file:
        while True:
            bytes_read = socket_s.recv(BUFFER_SIZE)
            if not bytes_read:
                break
            file.write(bytes_read)
    print(f"Archivo recibido.")

    socket_s.close()
