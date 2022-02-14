#multicast transmisson
import socket
import time
from contextlib import closing
def main():
    local_address = '127.0.0.1'
    multicast_group = '239.0.0.1'
    port = 4000
    with closing(socket.socket(socket.AF_INET, socket.SOCK_DGRAM)) as sock:
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_IF, socket.inet_aton(local_address))
        count = 0
        while True:
            message = 'From Py Server : {0}'.format(count).encode('utf-8')
            print(message)
            sock.sendto(message, (multicast_group, port))
            count += 1
            time.sleep(1)
if __name__ == '__main__':
    main()
