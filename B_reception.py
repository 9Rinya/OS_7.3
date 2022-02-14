#bloadcast reception
import socket
HOST_NAME = ''
PORT = 8080
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST_NAME, PORT))
while True:
    rcv_data, addr = sock.recvfrom(1024)
    print("receive data : [{}]  from {}".format(rcv_data,addr))
sock.close()
