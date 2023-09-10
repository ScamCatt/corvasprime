import discord
import responses

URL = "https://discord.com/api/oauth2/authorize?client_id=1150433259788968016&permissions=414464698368&scope=bot"
TOKEN = "MTE1MDQzMzI1OTc4ODk2ODAxNg.GvPLQO.Uh6xLM8edXnRGDZ3PnKW7T0i7wrhE_TEbn9rkc"

async def sendMessage(message, userMessage):
    print("what I said" + userMessage)
    print(message)
    try:
        response = responses.handleResponse(userMessage)
        if (response != None):
            await message.channel.send(response)
    except Exception as e:
        print(e)

def runBot():
    client = discord.Client(intents=discord.Intents.all())

    @client.event
    async def on_ready():
        print(f'{client.user} is detecting idiots!')
    
    @client.event
    async def on_message(message):
        if (message.author == client.user):
            return
        user_message = str(message.content)
        await sendMessage(message, user_message)
    client.run(TOKEN)
