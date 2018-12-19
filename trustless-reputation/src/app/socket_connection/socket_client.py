# load additional Python modules
import socket  
import time

# retrieve local hostname
local_hostname = socket.gethostname()

# get fully qualified hostname
local_fqdn = socket.getfqdn()

class SocketClient(object):

    def __init__(self):
        # create TCP/IP socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # get the according IP address
        ip_address = socket.gethostbyname(local_hostname)

        # bind the socket to the port 23456, and connect
        server_address = (ip_address, 23456)  
        self.sock.connect(server_address)  
        print ("connecting to %s (%s) with %s" % (local_hostname, local_fqdn, ip_address))
    
    def send(self, data):
        print ("Send data: %s" % data)
        # new_data = str("temperature: %s\n" % data).encode("utf-8")
        encoded_data = str(data).encode('utf-8')
        self.sock.sendall(encoded_data)
    
    def close(self):
        self.sock.close()