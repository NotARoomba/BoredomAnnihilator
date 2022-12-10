import discord
from discord.ext import commands
import requests
import Paginator


class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.description = "A bunch of useful utility commands!"
    @commands.command(description="Find your ping to SunShine!")
    async def ping(self, ctx):
        embed = discord.Embed(color=discord.Colour.yellow(), title="Ping", description=f':green_apple: Finding ping to bot...\n:alarm_clock: Your ping is {round(self.bot.latency*1000)} ms')
        await ctx.send(embed=embed)
    @commands.command(description="Get a random quote from someone!")
    async def quote(self, ctx):
        json = requests.get("https://api.quotable.io/random").json()
        await ctx.send(f'"{json["content"]}" -{json["author"]}')
    @commands.command(description="Shows my commands!")
    async def help(self, ctx):
        embeds = []
        for i in self.bot.cogs:
            cog = self.bot.get_cog(i)
            embed = discord.embeds.Embed(color=discord.Colour.yellow(), title=f'{i} Commands:')
            for c in cog.get_commands():
                print(c)
            embeds.push_back(embed)
        await Paginator.Simple().start(ctx, pages=embeds)

