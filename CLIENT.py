import os
import socket
import time
import sys



cport = 22222
server_host = input('[SYSTEM]** Enter the server IP for connection: ')
# cport = input('[SYSTEM]** Enter the sever port for connection: ')
client_name = socket.gethostname()
client_IP = socket.gethostbyname(client_name)
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def client_conn():
    try:
        socket.connect((server_host, 22221))
        print(f'[SYSTEM][C ONNECTING..]{server_host} : {cport}')
        print(f'Hello {client_name}, you are connected on: {client_IP}')

    except:
        print(f'[SYSTEM]*[ERROR] Unable to connect to: {server_host}')
        exit(0)  # signifies clean exit
    if socket.connect:
        recv_file()

def recv_file():
    ## receive file paramaters
    file_name = socket.recv(100).decode('utf-8')  # ('utf-8')
    file_size = socket.recv(100).decode('utf-8')  # ('utf-8')
    print(
        f'[SYSTEM]** {file_name} is : {file_size} bytes \n [SYSTEM].. Initiating File Transfer. ')

    # print(f'{file_name} is {file_size}')\\\
    with open("./rec/" + file_name, 'wb') as file:
        receive_count = 0
        #
        start_time = time.time()
        #print(start_time) # or start_time()
        ##
        while receive_count <= int(file_size):
            data = socket.recv(8192)
            if not (data):  # may be unecessary.
                break
            file.write(data)
            receive_count += len(data)

        end_time = time.time()
    time_to_complete = end_time - start_time
    print(f'[SYSTEM] File Transfer Complete in {time_to_complete}')
    socket.close()

def main():
    client_conn()
if __name__ == '__main__':
    main()
