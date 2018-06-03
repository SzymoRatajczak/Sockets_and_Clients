from socket import socket,AF_INET,SOCK_DGRAM
host="127.0.0.1"
port=2223
buf=1024
addr=(host,port)

UDPSocket=socket(AF_INET,SOCK_DGRAM)

while True:
    data=input('<<')
    bin_data=data.encode()
    if not data:
        break
    else:
        if(UDPSocket.sendto(bin_data,addr)):
            print("Sending")
UDPSocket.close()
