from socket import *

group_addr="224.13.13.13"
port=2223

addr1=(group_addr,port)
sock=socket(AF_INET,SOCK_DGRAM)

sock.setsockopt(IPPROTO_IP,IP_MULTICAST_TTL,32)
sock.setsockopt(IPPROTO_IP,IP_MULTICAST_LOOP,1)

data="Grretings"
sock.sendto(data,addr1)

sock.close()

