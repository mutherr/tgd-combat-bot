#bookkeeping for card plays in combat and keeping track of turn count
#
#Author: Isabel Muther

class Game:

    players = {}
    turnCount = 0

    def __init__(self):
        pass

    def choose_card(player,card):
        return f"{player} will play {card}"
    
    def show_hand(player):
        return "Placeholder hand representation"
    
    def end_turn():
        return "Turn ended"
    
    def reset():
        return "Reset game state"
    