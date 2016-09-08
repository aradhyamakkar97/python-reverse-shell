import socket
import sys

#create socket (allows two computers to connect)

def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print('socket creation error '+str(msg))

# bind socket to port and wait for connection from client
def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to port: "+str(port))
        s.bind((host,port))
        s.listen(5)
    except socket.error as msg:
        print('socket binding error: '+str(msg))
        print('retrying...')
        socket_bind()

# establishing a connection with client (socket must be listening for them)

def socket_accept():
    conn,address = s.accept()
    print("Connection has been established | " +"IP "+address[0]+" | Port "+str(address[1]))
