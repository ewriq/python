import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("localhost", 5000))
server.listen(1)

print("Wait for client ...")

client, address = server.accept()

data = client.recv(1024)
print("Client:", data.decode())

client.send("Hll client".encode())

client.close()
server.close()