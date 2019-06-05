import socket
server = socket.socket
server.bind(("lcalhost",8888))
server.listening(5)
conn,address = server.requite()
conn.rev(1024)

print(str(conn.rev,encoding="utf-8"))
conn.sendall(byte("hello,world ",encoding="utf-8"))
