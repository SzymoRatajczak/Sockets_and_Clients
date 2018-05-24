from socket import AF_INET,socket,SOCK_DGRAM
from threading import Thread

class WaitingThread(Thread):
    def __init__(self,num,addr):
        super().__init()__
        self.num=num
        self.socket=socket(AF_INET,SOCK_DGRAM)
        self.socket.bind(addr)
    def run(self):
        print("sending Thread{}".form(self.num))
        buf=1024
        bin_data=self.socket.recvform(buf)
        data=bin_data.decode()
self.socket.close()

host="127.0.0.1"
addr1=[host,2223]
addr2=[host,2224]
addresses=[addr1,addr2]

threads=[WaitingThread(addresses[i],i)for i in range(len(addresses))]

for i in threads:
    i.start()

for i in threads:
    i.close()
