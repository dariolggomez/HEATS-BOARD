#include "server.h"

Server::Server(QObject *parent) : QObject(parent)
{
    server = new QTcpServer(this);
    connect(server, SIGNAL(newConnection()), this, SLOT(newConnection()));

    if(!server->listen(QHostAddress::Any, 1234))
    {
        qDebug() << "El servidor no pudo iniciar.";
    }else
    {
        qDebug() << "Servidor iniciado.";
    }
}

void Server::newConnection()
{
    QTcpSocket *socket = server->nextPendingConnection();
    QFile file("logs/heats-net.log");
    file.open(QIODevice::ReadOnly);
    QByteArray q = file.readAll();
    socket->write(q);
    socket->flush();
    socket->waitForBytesWritten(3000);
    socket->close();
}
