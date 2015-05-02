#!/usr/bin/env python 

""" 
A simple echo client 
Taken from: http://ilab.cs.byu.edu/python/socket/echoclient.html
""" 

import socket 

host = 'localhost' 
port = 50000 
size = 1024 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((host,port)) 
s.send('Hello, world') 
data = s.recv(size) 
s.close() 
print 'Received:', data