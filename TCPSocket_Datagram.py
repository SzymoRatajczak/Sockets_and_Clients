from socket import socket,AF_INET,SOCK_STREAM
host="127.0.0.1"
port=2223
buf=1024
addr=(host,port)

TCPSocket=socket(AF_INET,SOCK_STREAM)
TCPSocket.bind(addr)
TCPSocket.listening(10)

client_socket,addr=TCPSocket.accept()

while True:
    data=client_socket.recv(buf)
    bin_data=data.decode()
    if(bin_data=="\quit"):
        print("quiting")
    else:
        print("Receiving")
TCPSocket.close()
        
