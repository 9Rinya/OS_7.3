#bloadcast transmission
import socket
HOST_NAME = ''
PORT = 8080
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.sendto(b"Hello, UDP BroadCast", (HOST_NAME, PORT))
sock.close()
