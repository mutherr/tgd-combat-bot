#Initial commit of TDG combat bot
#
# Author: Isabel Muther

from dotenv import load_dotenv
import os

from modules.bot.Client import CombatClient

#load in secrets
load_dotenv()

#instantiate client
client = CombatClient()

#let it run
api_key = os.getenv("DISCORD_SECRET")
client.run(api_key)