#bookkeeping for card plays in combat and keeping track of turn count
#
#Author: Isabel Muther

class Game:
    suits = ["cups","wands","swords","pentacles"]

    playerChoices = {}
    turnCount = 0

    def __init__(self):
        pass

    def choose_suit(self,player,suit):
        #check if the played suit is an option
        if suit.lower() not in self.suits:
            return "Invalid Suit Specified"
        
        #if we've not seen a move from this player before, add an entry to the choices table
        if player not in self.playerChoices:
            self.playerChoices[player] = ""
        self.playerChoices[player] = suit

        return f"{player} will play {suit}"
    
    def end_turn(self):
        turnDescription = f"Ending turn {self.turnCount}, with chosen suits:\n\n"

        for player,suit in self.playerChoices.items():
            turnDescription += f"{player}: {suit}\n"
            self.playerChoices[player] = ""

        self.turnCount += 1
        return turnDescription.strip()
    
    def reset(self):
        self.turnCount = 1
        self.playerChoices = {}
        return "Reset game state"
    