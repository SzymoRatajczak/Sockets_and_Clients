from socket import socket,AF_INET,SOCK_STREAM
host="127.0.0.1"
port=2223
buf=1024
addr=(host,port)

TCPSocket=socket(AF_INET,SOCK_STREAM)
TCPSocket.connect(addr)

while True:
    data=input('<<')
    bin_data=data.encode()
    if not data:
        break
    else:
        if(TCPSocket.send(bin_data)):
            print("Sending:")
TCPSocket.close()
