#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

def getPlayerInput():
    choiceVal = {1:"rock" , 2:"paper" , 3:"scissors"}
    while True:
        print """
        1: Rock
        2: Paper
        3: Scissors """
        choice = input("Enter Choice : ")
        if choice in [1,2,3]:
            break
        else:
            print "Invalid Input"
    return choiceVal[choice]

a = getPlayerInput()
s = socket.socket()         # Create a socket object
#host = socket.gethostname() # Get local machine name
host = "10.10.18.75"
port = 12341                # Reserve a port for your service.

s.connect((host, port))
a = getPlayerInput()
s.send(a)

print s.recv(1024)
s.close                     # Close the socket when done
