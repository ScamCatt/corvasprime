import time
import mysql.connector
import json

keyWords = ["corvas", "prime"]
servers = {}

timeoutAmount = 60

with open("database.json") as file:
    creds = json.load(file)


def createConnection():
    """ Generate a database connection.
    Returns a usable database connection.
    """
    connection = mysql.connector.connect(
            host = creds["host"],
            port = creds["port"],
            user = creds["user"],
            password = creds["password"],
            database = creds["database"]
        )
    return connection

# Increase counter in the database
def addRecord(user, serverName):
    connection = createConnection()
    cursor = connection.cursor()
    pStatement = """IF NOT EXISTS(SELECT 1 FROM primers WHERE dcName = %s AND dcServer = %s)
                    THEN INSERT INTO primers (dcName, primeMentions, dcServer) VALUES (%s, 1, %s);
                    ELSE UPDATE primers
                    SET primeMentions = primeMentions + 1
                    WHERE dcName = %s AND dcServer = %s;
                    END IF"""
    sParams = (user, serverName, user, serverName, user, serverName)
    cursor.execute(pStatement, sParams)
    connection.commit()
    cursor.close()
    connection.close()

def handleResponse(message, serverID, user, serverName) -> str:
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
        print(f"Corvas Prime mentioned by {user}!")
        addRecord(user, serverName)
        if (curTime - lastTime >= timeoutAmount):
            servers[curServer] = curTime
            return "https://www.youtube.com/watch?v=VvGG9xdmAwE"
    return None