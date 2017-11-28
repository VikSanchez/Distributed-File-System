import os.path
import socket
import select
import sys
from thread import *
import threading


def lock():
    s = socket.socket()         # Create a socket object
    host = socket.gethostname() 
    port = 9009                
    s.bind(('', port))        
    print 'server started'
    s.listen(5)
    files = {'test.png':'unlock'}
    c, addr = s.accept()
    file_name = c.recv(1024)
    print(file_name)
    
    if file_name in files.keys():
        value = files.get(file_name)
        c.send(value.encode())
    else:
        files[file_name]='unlock'
        value = files.get(file_name)
        
        c.send(value.encode())
        f2 = c.recv(1024)
        print(f2)
        if f2 in files.keys():
            files[f2] = 'locked'
            print(files)
        f3 = c.recv(1024)
        if f3=='done':
            files[f2]= 'unlock'
            print(files)
    
        

if __name__ == '__main__':
    lock()
    
    
