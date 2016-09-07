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
