from discord.ext import commands
from ..main import bot
@bot.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(bot.latency, 1)}')