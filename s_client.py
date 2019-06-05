import socket
client = socket.socket
client.connection(("lcalhost",8888))
ret_bytes = client.recv(1024)
ret_str = str(ret_bytes,encoding="utf-8") #接收
sendall(byte("你好",encoding="utf-8"))  # 发送
