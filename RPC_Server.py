from xmlrpc.server import SimpleXMPRPCServer

def funkcja(x):
    print("dummy function")

    
if __name__=="__main__":
    server=SimpleRPCServer((localhost,8003))
    server.register_introspection_function()
    server_regiset_function(funkcja)
    server.serve_forever()
