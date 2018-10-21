import socket 

s = socket.socket()
host = input(str("Enter the name of the host: "))
port = 8090
s.connect((host,port))
print("connected to server")
start = 0

while True:
    incoming_message = s.recv(2048)
    incoming_message = incoming_message.decode()
    print("BOT:",incoming_message)
    start += 1
    if start > 1:
        value = input(str("User: "))
        value = value.encode()
        s.send(value)

s.close()