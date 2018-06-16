from asyncore import dispatcher
from sys import argv
from socket import AF_INET,SOCK_STREAM

if(len(argv)<2):
    print("No data")
port=argv[1]
address=('localhost',port)
disp=dispatcher()
disp.connect(address)
wynik=disp.send("Hello World")

if(wynik):
    print("I go yourm essage")

disp.close()
