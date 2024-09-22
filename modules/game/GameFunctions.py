#bookkeeping for card plays in combat and keeping track of turn count
#
#Post-beltane this will require a lot of reworking as players will have individual decks and hands.
# We'll need a player class with its own deck object instantiated for each player rather than a
# simple table of strings
#
#Author: Isabel Muther

class Game:
    suits = ["cups","wands","swords","pentacles"]

    playerChoices = {}
    turnCount = 0

    def __init__(self):
        pass

    def choose_suit(self,player: str,suit: str) -> str:
        #check if the played suit is an option
        if suit.lower() not in self.suits:
            return "Invalid Suit Specified"
        
        #if we've not seen a move from this player before, add an entry to the choices table
        if player not in self.playerChoices:
            self.playerChoices[player] = ""
        self.playerChoices[player] = suit

        return f"{player} will play {suit}"
    
    def end_turn(self) -> str:
        turnDescription = f"Ending turn {self.turnCount}, with chosen suits:\n\n"

        for player,suit in self.playerChoices.items():
            turnDescription += f"{player}: {suit}\n"
            self.playerChoices[player] = ""

        self.turnCount += 1
        return turnDescription.strip()
    
    def reset(self) -> None:
        self.turnCount = 1
        self.playerChoices = {}
    