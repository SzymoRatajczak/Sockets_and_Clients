from socket import socket,AF_INET,SOCK_DGRAM

host="127.0.0.1"
port=2223
buf=1024
addr=(host,port)

UDPSocket=socket(AF_INET,SOCK_DGRAM)
UDPSocket.bind(addr)

while True:
    bin_data,addr=UDPSocket.recvform(buf)
    data=bin_data.decode()
    if(data=="\quit"):
        print("Quiting")
        break
    else:
        print("recived")
UDPSocekt.close()
