import discord
from discord.ext import commands
import requests

class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.description = "A bunch of useful utility commands!"
    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(color=discord.Colour.yellow(), title="Ping", description=f':green_apple: Finding ping to bot...\n:alarm_clock: Your ping is {round(self.bot.latency*1000)} ms')
        await ctx.send(embed=embed)
    @commands.command()
    async def quote(self, ctx):
        json = requests.get("https://api.quotable.io/random").json()
        await ctx.send(f'"{json["content"]}" -{json["author"]}')
    @commands.command()
    async def help(self, ctx):
        await ctx.send(f'potato')