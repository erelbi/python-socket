
#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import socket
import os

TCP_IP = '192.168.1.205'
TCP_PORT = 900
BUFFER_SIZE = 1024
MESSAGE = 'BEYAZ TAVŞANI, tAKiP et!'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
"""s.send(MESSAGE)"""
#s.send(b'ls')
while True:
    cmd= raw_input ( ' komutu giriniz')
    s.send(cmd)
    data = s.recv(BUFFER_SIZE)
    print("client received data    {} ".format(data))
    print "got: %s" %data
    
s.close()

