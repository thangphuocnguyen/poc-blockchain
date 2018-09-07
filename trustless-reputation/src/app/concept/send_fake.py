from app.socket_connection.socket_client import SocketClient

def fake_send(data):

    sock = SocketClient()

    sock.send(data)
