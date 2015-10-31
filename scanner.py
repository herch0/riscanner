#41.87.128.0	41.87.159.255

import socket
from threading import Thread, active_count
import time

def ip_range(debut, fin):
    x1, x2, x3, x4 = [int(x) for x in debut.split('.')]
    y1, y2, y3, y4 = [int(y) for y in fin.split('.')]
    ip_list = list()
    while True:
        if [x1, x2, x3, x4] == [y1, y2, y3, y4]:
            break
        ip_list.append('%d.%d.%d.%d' % (x1, x2, x3, x4))
        if x4 >= 255 or x4 == 0:
            x4 = 1
            if x3 >= 255 or x3 == 0:
                x3 = 1
                if x2 >= 255 or x2 == 0:
                    x2 = 1
                    x1 += 1
                else:
                    x2 += 1
            else:
                x3 += 1
        else:
            x4 += 1
    return ip_list

class Scanner(Thread):
    def __init__(self, ip):
        Thread.__init__(Thread)
        self.ports = range(80, 9999)
        self.ip = ip
    #end constructor

    def run(self):
        for port in self.ports:
            ouvert = self.check_port(port)
            if ouvert:
                print(self.ip, port, ouvert)
    #end run

    def check_port(self, port):
        ouvert = True
        #AF_INET: adresse ipv4 ou nom de domaine
        #SOCK_STREAM: TCP
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            try:
                sock.connect((self.ip, port))
            except OSError as e:
                ouvert = False
        return ouvert
    #end check_port
#end class Scanner

ips = ip_range("41.87.128.1", "41.87.159.255")

socket.setdefaulttimeout(15)

MAX_THREADS = 500

for ip in ips:
    while active_count() >= MAX_THREADS:
        time.sleep(5)
    Scanner(ip).start()
