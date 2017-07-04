import socket
from threading import Thread
#from SocketServer import ThreadingMixIn

TCP_IP = '218.150.181.229'
TCP_PORT = 9001
BUFFER_SIZE = 1024

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((TCP_IP, TCP_PORT))
threads = []


class ClientThread(Thread):

    def __init__(self,ip,port,sock):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        print ("   New thread started for "+ip+":"+str(port))

while True:
    tcpsock.listen(5)
    print ("Waiting for incoming connections...")
    (conn, (ip,port)) = tcpsock.accept()
    print ('   Got connection from ', (ip,port))
    newthread = ClientThread(ip,port,conn)
    newthread.start()
    fname = 'recv_pic' + str(port) + '.jpg'
    with open(fname, 'wb') as f:
        print('receiving data...')
        while True:
            data = conn.recv(BUFFER_SIZE)
            if not data:
                print('file recieved')
                f.close()
                break
            # write data to a file
            f.write(data)
    threads.append(newthread)

for t in threads:
    t.join()
