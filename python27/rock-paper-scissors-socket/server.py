import socket               # Import socket module

winDict = {"rock" : "paper" , "paper" : "scissors" , "scissors" : "rock"}


def getPlayerInput():
    choiceVal = {1:"rock" , 2 : "paper" , 3 : "scissors"}
    while True:
        print """
        1.rock
        2.paper
        3.scissors"""
        choice = input("enter choice:")
        if choice in [1,2,3]:
            break
        else:
            print "Invalid input"

    return choiceVal[choice]

def winnerDecide(serverChoice,clientChoice):
    if serverChoice == clientChoice:
        return "its a tie!"
    if winDict[serverChoice] == clientChoice:
        return "Client wins"
    else:
        return "Server wins"
        
    
        
        

playerServerChoice = getPlayerInput()
s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12341                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
c = None
while True:
   if c is None:       
       print '[Waiting for connection...]'
       c, addr = s.accept()
       print 'Got connection from', addr
   else:
       # Halts
       #print '[Waiting for response...]'
       playerClientChoice = c.recv(1024)
       
       result = winnerDecide(playerServerChoice,playerClientChoice)
       print result
       
       c.send(result)
       break

