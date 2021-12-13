import discord
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
load_dotenv()

bot = commands.Bot(command_prefix=".")
client = discord.Client()

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author==client.user:
        return
    if message.content.startswith(".tell me a joke"):
        await message.channel.send("Roopjith!!")

@bot.command()
async def hello(ctx):
    await ctx.reply("Hello!")

client.run(getenv("TOKEN"))