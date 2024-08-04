import socket

target_host = "0.0.0.0"
target_port = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))

data = "GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n"

client.sendto(data.encode(), (target_host, target_port))
response = client.recv(4096)
print(response.decode())