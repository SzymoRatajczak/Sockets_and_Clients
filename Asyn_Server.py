from asyncore import dispatcher,loop

class MyServer(dispatcher):
    def __init__(self,port):
        dispatcher.__init__()
        self.createsocket()
        adress=(' ',port)
        self.bind(adress)
        self.listen(4)
    def handle_accepted(self,socket,adress):
        print("Information")
        CommunicateHandler(socket)


class CommunicateHandler(dispatcher):
    def handle_read(self):
        bin_data=self,recv(1024)
        print("I got:"+bin_data.decode())

if __name__=="__main__":
    server=MyServer(2222)
    loop()
