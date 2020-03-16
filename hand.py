class Hand():
    def __init__(self):
        self.cards = []
    
    def drawCard(self,newCard):
        self.cards.append(newCard)
    
    def playCard(self,playCard):
        return self.cards.pop(playCard)

    def stealZeus(self):
        self.zeus = True
    
    def loseZeus(self):
        self.zeus = False
    
    def len(self):
        return len(self.cards)

    def __str__(self):
        toreturn = ""
        for card in self.cards:
            toreturn = toreturn + str(card)+", "
        return toreturn[:len(toreturn)-2]

