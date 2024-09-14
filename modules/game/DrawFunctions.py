#Defines basic functions for drawing tarot cards, mostly taken from 
# the currently used TGD bot from LORP.
#
# Author: Isabel Muther

import discord
import random

# list of major arcana
cards = ["The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor", "The Hierophant", "The Lovers", "The Chariot", "Strength", "The Hermit", "**Wheel of Fortune** :ferris_wheel:", "Justice", "The Hanged Man", "Death", "Temperance", "The Devil", "**The Tower** :tokyo_tower:", "The Star", "The Moon", "The Sun", "Judgement", "The World"]

#Helper function to randomly draw a card.
def draw_card():
    drawResult = random.randint(0,22)
    #add 1 to adjust for zero indexing
    return drawResult + 1

#send a randomly drawn card to bot
def random_draw():
    drawResult = draw_card()
    return "You drew %s! (%d)"%(cards[drawResult], drawResult)

# send a trait drawn card result to bot
def random_draw_with_trait(traitValue):
    drawResult = draw_card()
    finalResult = drawResult + traitValue
    return "You drew %s! (%d)"%(cards[drawResult], finalResult)

# send a trait, blessed and cursed drawn card result to bot
def random_draw_with_modifier(traitValue, modifier):
    drawResult = draw_card()
    if modifier.lower() == "b":
        mod = 3
    elif modifier.lower() == "c":
        mod = -3
    else:
        return "Unknown modifier. Enter b for blessed or c for cursed. For a standard trait draw, use `/drawtrait`"
    finalResult = drawResult + traitValue + mod
    return "You drew %s! (%d)"%(cards[drawResult], finalResult)

