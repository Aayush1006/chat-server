import socket
import threading
import re

def userThread(conn,addr):
    start_message = "Hello, I am going to ask you few questions that will help me know you better?"
    sendMessage(start_message)
    
    question1 = "What is your name?"
    sendMessage(question1)
    name = receiveMessage()
    
    question2 = "Are you Male or Female?"
    sendMessage(question2)
    gender = receiveMessage()
    
    
    question3 = "When were you born?[dd-mm-yyyy]"
    sendMessage(question3)
    birthDate = receiveMessage()
    while not re.match(r'[0-9]{2}-[0-9]{2}-[0-9]{4}',birthDate):
        message = "Please Enter Date of birth in the following format: {}".format('dd-mm-yyyy')
        sendMessage(message)
        birthDate = receiveMessage()
    
    question4 = "Are you a smoker?[Yes/No]"
    sendMessage(question4)
    smoke = receiveMessage()
    
    
    confirmation = "Thank you. Enter 'Done' for results."
    sendMessage(confirmation)
    confirmation = receiveMessage()
    if confirmation.lower() == 'done':
        output(name,gender,birthDate,smoke)
   
def sendMessage(message):
    message = message.encode()
    conn.send(message)
    
def receiveMessage():
    value = conn.recv(2048)
    value = value.decode()
    return value

def output(name,gender,birthDate,smoke):
    if smoke == 'No':
        output = (name + " was born on " + birthDate + " and is a " + gender + " " + "non-smoker")
    else:
        output = (name + " was born on " + birthDate + " and is a " + gender + " " + "smoker")
    sendMessage(output)
    
s = socket.socket()
host = socket.gethostname()
print(host)
port = 8090
s.bind((host,port))
s.listen(10)

    
while True:
    
    conn,addr = s.accept()
    
    print(addr," has been connected")
    
    threading.Thread(target=userThread,args=(conn,addr)).start()
    
conn.close()
s.close()
