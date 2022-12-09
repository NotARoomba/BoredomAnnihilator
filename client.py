import discord
from discord.ext import commands
from cogs.utilities import *

class SunShine(commands.Bot):
    bot = commands
    async def on_ready(self):
        await self.add_cog(Utilities(self))
        print(f'{self.user} is online!')

    async def on_message(self, message):
        if message.author == self.user:
            return
        await self.process_commands(message)
    