import discord
from discord import app_commands
from discord.ext import commands
import requests
import Paginator
from urllib.parse import urlparse
import re

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.description = "Music commands!"

    @commands.command(description="Play music!")
    async def play(self, ctx, *, args):
        print(args)
        if re.match(r"http(?:s?):\/\/(?:www\.)?youtu(?:be\.com\/watch\?v=|\.be\/)([\w\-\_]*)(&(amp;)?‌​[\w\?‌​=]*)?", args):
            print("yt")
        else:
            pass