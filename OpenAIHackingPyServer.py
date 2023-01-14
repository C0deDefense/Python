import socket

# IP and port to bind the server to
IP = "192.168.56.7"
PORT = 7777

# create a socket object
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to a specific address and port
server.bind((IP, PORT))

# listen for incoming connections
server.listen(1)
print("[*] Listening on %s:%d" % (IP, PORT))

# accept a connection
client, addr = server.accept()
print("[*] Connection from: %s:%d" % (addr[0], addr[1]))

# enter an infinite loop to receive commands
while True:
    # receive the command from the server
    command = input("Shell> ")
    if command == "exit":
        break
    # send the command to the client
    client.send(command.encode())
    # receive the result from the client
    result = client.recv(1024)
    # print the result
    print(result.decode())

# close the connection
client.close()
server.close()
