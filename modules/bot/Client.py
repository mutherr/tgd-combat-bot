#Defines the bot for TGD combat bot
#
# Author: Isabel Muther

import discord

from ..game.DeckFunctions import *
from modules.bot.Interactions import Interactions

class CombatClient(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="/", intents=discord.Intents.default())
        self.synced = False
    
    async def setup_hook(self) -> None:
        await self.add_cog(Interactions())
        await self.tree.sync()
    
    async def on_ready(self):
        print(f"We have logged in as {self.user}.")