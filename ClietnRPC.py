from xmlrpc.client import ServerProxy

if __init__=="__main__":
    server=ServerProxy("http://localhost:8003")
    print("List of methods")
    print(server.system.listMethods())
    print("Infomration ")
    print(server.system.methodHelp())
    
