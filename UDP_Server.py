from socketserver import BaseRequestHandler,UDPServer

class Server(baseRequestHandler):
    def handle(self):
        bin_data=self.request[0]
        data=bin_data.decode()

if __name__=="__main__":
    localhost,port="127.0.0.1",2223
    server=UDPServer((localhost,server),Server)
    server.serve_forever()
