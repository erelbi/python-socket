# python-socket
 it can send commands between the server and the client and process them into the database.

[SERVER](Pardus 17.1)
pip3 install mysql.connector
pip3 install sockets

[Client](Ubuntu)
pip install sockets


[MySQL]

Table from proje

+----------+-----------------+------+-----+---------+----------------+
| Field    | Type            | Null | Key | Default | Extra          |
+----------+-----------------+------+-----+---------+----------------+
| id       | int(6) unsigned | NO   | PRI | NULL    | auto_increment |
| hostname | varchar(30)     | NO   |     | NULL    |                |
| ip       | varchar(30)     | NO   |     | NULL    |                |
| command  | varchar(9050)   | YES  |     | NULL    |                |
+----------+-----------------+------+-----+---------+----------------+

