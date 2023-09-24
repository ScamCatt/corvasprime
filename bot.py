import discord
import responses

URL = "https://discord.com/api/oauth2/authorize?client_id=1150433259788968016&permissions=414464698368&scope=bot"
TOKEN = ""

async def sendMessage(message, userMessage, serverID, user):
    try:
        response = responses.handleResponse(userMessage, serverID, user, message.guild.name)
        if (response != None):
            await message.channel.send(response)
    except Exception as e:
        print(e)

def runBot():
    client = discord.Client(intents=discord.Intents.all())

    @client.event
    async def on_ready():
        print(f'{client.user} is running!')
    
    @client.event
    async def on_message(message):
        if (message.author == client.user):
            return
        user_message = str(message.content)
        serverID = message.guild.id
        user = str(message.author)
        await sendMessage(message, user_message, serverID, user)
    client.run(TOKEN)
