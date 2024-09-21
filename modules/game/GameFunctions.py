#bookkeeping for card plays in combat and keeping track of turn count
#
#Author: Isabel Muther

class Game:
    suits = ["cups","wands","swords","pentacles"]

    playerChoices = {}
    turnCount = 0

    def __init__(self):
        pass

    def choose_card(self,player,suit):
        if suit.lower() not in self.suits:
            return "invalid Suit Specificed"
        return f"{player} will play {suit}"
    
    def show_hand(self,player):
        return "Placeholder hand representation"
    
    def end_turn(self):
        return "Turn ended"
    
    def reset(self):
        return "Reset game state"
    