keyWords = ["corvas", "prime"]

def handleResponse(message) -> str:
    msg = message.lower()
    if (all([x in msg for x in keyWords])):
        return "https://www.youtube.com/watch?v=VvGG9xdmAwE"
    return None
    

