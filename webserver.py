#!/usr/bin/env python3

import socket
import os
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
mydb = mysql.connector.connect(

  host="localhost",

  user="javatar",

  passwd="1",

  database="javatar_db"

)
TCP_IP = '192.168.1.205'
TCP_PORT = 900
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

while True:

    conn, addr = s.accept()

    print(" Connection address {} ".format(addr))
#    conn.send(b'ls')
    while True:
        data = conn.recv(BUFFER_SIZE)
        if not data: break
        komut = str.format(data.decode("utf-8"))
        f = os.popen(komut).read()
#        print (f)
#        a = print("command output {} ".format(f))
        mydb = mysql.connector.connect(

              host="localhost",

              user="javatar",

              passwd="1",

             database="javatar_db"

         )

        mycursor = mydb.cursor()
        sql = "UPDATE proje  SET command =  '" +   f  + "' WHERE id = '3'"
        print (sql)
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")
        btyrArr = str.encode(f)
        conn.send(btyrArr)  # echo


print(" closing Connection    ")

