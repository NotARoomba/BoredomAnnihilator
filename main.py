import discord
import os
from dotenv import load_dotenv
#from keep_alive import keep_alive
from client import SunShine
PREFIX='!'

load_dotenv()

intents = discord.Intents.all()

client = SunShine(intents=intents, command_prefix=PREFIX, help_command=None)

client.run(os.getenv('TOKEN'))