import time

keyWords = ["corvas", "prime"]
servers = {}

timeoutAmount = 10

def handleResponse(message, serverID) -> str:
    msg = message.lower()
    curServer = serverID

    # Check if server already in dict, if not add it.
    if (curServer not in servers):
        servers[curServer] = -120

    # Get the last time the command was triggered in the specific server.    
    lastTime = servers[curServer]

    curTime = time.time()

    # Check if the message contains the right keywords.
    if (all([x in msg for x in keyWords])):
        if (curTime - lastTime >= timeoutAmount):
            servers[curServer] = curTime
            return "https://www.youtube.com/watch?v=VvGG9xdmAwE"
    return None
    

