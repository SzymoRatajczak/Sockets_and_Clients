from socket import *
from struct import pack

group_addr="224.13.13.13"
port=2223
addr1=(group_addr,port)

sock=socket(AF_INET,SOCK_DGRAM)

sock.setsockopt(IPPROTO_IP,IP_MULTICAST_TTL,32)
sock.bind((' ',port))
group=inet_aton(group_addr)
mreq=pack("4sl",group,INADDR_ANY)
sock.setsockopt(IPPROTO_IP,IP_ADD_MEMBERSHIP,mreq)

bin_data,address=sock.ecvfrom(1024)

print("Recived message")

sock.close()
