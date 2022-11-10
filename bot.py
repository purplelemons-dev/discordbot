
import discord

with open(".env",'r') as f: TOKEN=f.read()

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")

@client.event
async def on_message(message:discord.Message):

    if message.author == client.user: return

    if message.content == "ping":
        await message.reply("pong", mention_author=False)

client.run(TOKEN)
