# tdg-combat-bot
Code for a WIP bot for running combat in an online session of [The Gloaming Diaries](https://timorjack.itch.io/gloaming-diaries)

The code for the bot interaction is stored in `/modules/bot`, while game related logic is stored in `modules/game`

# Running the bot

To start up the bot, simply run `python main.py` from the main project directory.

# Config

To run the bot, a secret key for the discord bot is needed in `.env`, along the lines of
`DISCORD_SECRET = "<secret here>"`

# Backend Tests

To test the bot's backend, run `pytest .\tests\gameTests.py -vv` from the root directory.