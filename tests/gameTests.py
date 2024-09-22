from modules.game.GameFunctions import Game

import pytest

@pytest.fixture
def game():
    yield Game()

def setup_game(game):
    game.choose_suit("Isabel","swords")
    game.choose_suit("Laila","wands")
    game.choose_suit("Ivy","cups")
    game.choose_suit("Freya","pentacles")

class Test:
    def test_suit_selection(self, game):
        #check that we're getting back the right response
        assert(game.choose_suit("Isabel","swords")=="Isabel will play swords")
        assert(game.choose_suit("Laila","wands")=="Laila will play wands")
        assert(game.choose_suit("Ivy","cups")=="Ivy will play cups")
        assert(game.choose_suit("Freya","pentacles")=="Freya will play pentacles")

        #check we're updating internal state
        assert(game.playerChoices["Isabel"]=="swords")
        assert(game.playerChoices["Laila"]=="wands")
        assert(game.playerChoices["Ivy"]=="cups")
        assert(game.playerChoices["Freya"]=="pentacles")

        #check that changing a choice alters the internal state
        game.choose_suit("Isabel","cups")
        assert(game.playerChoices["Isabel"]=="cups")

    def test_suit_rejection(self,game):
        setup_game(game)

        assert(game.choose_suit("Ivy","adorable void kitty")=="Invalid Suit Specified")