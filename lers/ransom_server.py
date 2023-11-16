import socket
import os

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST='127.0.0.1'
PORT=444
server.bind((HOST,PORT))
server.listen(5)

print(f"Running TCP server on {HOST}:{PORT}")

client, address = server.accept()
print(f"Received connection from {HOST}")
while True:
    filename = client.recv(1024).decode()
    print("filename recv")
    client.send("Check".encode())
    if filename == "done":
        print("break")
        break
    filecontent = client.recv(1024)
    print("filecontent recv")

    with open(filename, 'wb') as f:
        f.write(filecontent)
        print("printing filecontent")
    client.send("Lesgo".encode())
client.close()
print(f"Connection from {HOST} closed")