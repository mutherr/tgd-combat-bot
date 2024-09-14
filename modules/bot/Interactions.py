#defines the commands used to interact with the bot
#
# Author: Isabel Muther
import discord
from discord.ext import commands
from modules.game import DrawFunctions

class Interactions(commands.Cog):
    def __init__(self):
        pass
        
    @discord.app_commands.command(name = "draw", description = "Randomly draw a tarot card")
    async def draw(self,interaction: discord.Interaction):
      await interaction.response.send_message(DrawFunctions.random_draw())

    @discord.app_commands.command(name = "drawblessed", description = "Randomly draw a tarot card with trait value and blessing or curse.")
    async def draw_with_mod(self,interaction: discord.Interaction, trait:int, bless:str):
      await interaction.response.send_message(DrawFunctions.random_draw_with_modifier(trait, bless))

    @discord.app_commands.command(name = "drawtrait", description = "Randomly draw a tarot card with a trait value. (Use the trait value)")
    async def draw_with_trait(self,interaction: discord.Interaction, trait:int):
      await interaction.response.send_message(DrawFunctions.random_draw_with_trait(trait))
  