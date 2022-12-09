import discord
import os
from dotenv import load_dotenv
from keep_alive import keep_alive
import asyncpraw
from discord.ext import commands

bot = commands.Bot(
    command_prefix="s!",
    case_insensitive=True
)

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} is online!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


@bot.event #First Command, CAn be used as a simple command reference.
async def test(ctx):
  await ctx.send("Hello World")






client.run(os.getenv('TOKEN'))