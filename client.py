import discord
from discord import app_commands
from discord.ext import commands
from cogs.utilities import Utility
from cogs.music import Music

class SunShine(commands.Bot):
    bot = commands
    async def on_ready(self):
        await self.add_cog(Utility(self))
        await self.add_cog(Music(self))
        await self.tree.sync()
        print(f'{self.user} is online!')

    async def on_message(self, message):
        if message.author == self.user:
            return
        await self.process_commands(message)
    