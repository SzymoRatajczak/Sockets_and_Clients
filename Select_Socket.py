from socket import *
from select import select

localhost="127.0.0.1"
buf=1024
addr1=(host,2223)
addr2=(host,2224)
sock1=socket(AF_INET,SOCK_DGRAM)
sock2=socket(AF_INET,SOCK_DGRAM)

socket1.bind(addr1)
socket2.bind(addr2)

socketlist=(socket1,socket2)

rdset,wrset,exset=select(socketlist,(),())

for i in rdset:
    bin_data,addr=i.recvfrom(buf)
    print("Recived message")


for sock in socklist:
    sock.close()
    
