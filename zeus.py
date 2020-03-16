from card import *
from hand import *
import random

class Zeus():
    
    def __init__(self):
        self.olympus = 0
        self.zeus = -1
        self.gods = {"Poseidon": self.Poseidon, "Aphrodite": self.Aphrodite,"Apollo": self.Apollo, "Ares": self.Ares,
                     "Artemis": self.Artemis, "Athena": self.Athena, "Hermes": self.Hermes, "Hera": self.Hera}
        self.library = self.createLibrary()
        self.discard = []
        self.players = []
        self.currentCard = None
        self.prevCard = None
        self.turnCount = 0
        self.currentPlayerNum = -1
        self.currentPlayer = None


    def play(self):
        self.initialize()

        #---------------------------------Turn-----------------------------------
        winner = -1
        while(winner == -1):
            self.currentPlayerNum = self.turnCount%len(self.players)
            self.currentPlayer = self.players[self.currentPlayerNum]

            print("Your current hand is: " + str(self.currentPlayer))

            print("Mt.Olympus value = "+str(self.olympus))
            if (self.zeus == self.currentPlayerNum):
                print("You have Zeus.")
            else:
                print("You do not have Zeus.")
            
            cardSelected = False
            cardPlayed = -1
            while(not cardSelected):
                try:
                    cardPlayed = int(input("Which card will you play? "))
                    if not (0 <= cardPlayed < self.currentPlayer.len()):
                        raise ValueError
                    cardSelected = True
                except:
                    print("Pick a valid card location, you goob.")
            
            self.currentCard = self.currentPlayer.cards[cardPlayed]

            self.playCard(cardPlayed)

            if(self.olympus % 10 == 0 or self.olympus == 69):
                self.zeus = self.currentPlayerNum
            
            if(self.prevCard == str(self.currentCard)):
                self.zeus = self.currentPlayerNum
            
            self.prevCard = self.currentCard

            if(self.olympus >= 100):
                winner = self.currentPlayerNum
            
            self.turnCount += 1
            self.draw(self.currentPlayer, 1)
            
        print("Congratulations, Player " + str(winner) + "! You have won the game. Scream your victory into the heavens my boy, declare your superiority.")
            
            

        #------------------------------------------------------------------------


    def initialize(self):
        random.shuffle(self.library)
        while (True):
            try:
                nPlayers = int(input("How many players? "))
                if (nPlayers > 10):
                    raise OverflowError
                break
            except:
                print("This won't work, you raggamuffin. Give me an integer number between 2 and 10.")
        for i in range(nPlayers):
            self.players.append(Hand())
        
        for i in self.players:
            self.draw(i, 4)


    def draw(self, player, num):
        for i in range(num):
            if(len(self.library) == 0):
                self.library = random.shuffle(self.discard)
                self.discard = []
            player.drawCard(self.library.pop())


    def createLibrary(self):
        list_of_cards = []
        
        for i in range(1,11):
            for j in range(4):
                newCard = numCard(i)
                list_of_cards.append(newCard)

        godcount = 0

        for i in range(3):
            newCard = godCard(list(self.gods.keys())[godcount])
            list_of_cards.append(newCard)

        godcount = 1

        for i in range(6):
            for j in range(2):
                newCard = godCard(list(self.gods.keys())[godcount])
                list_of_cards.append(newCard)
            godcount += 1

        newCard = godCard(list(self.gods.keys())[godcount])
        list_of_cards.append(newCard)

        return list_of_cards


    def playCard(self,card):
        self.currentPlayer.playCard(card)
        if (isinstance(self.currentCard,numCard)):
            self.olympus += self.currentCard.value
        else:
            self.gods[self.currentCard.value]()


    def Poseidon(self):
        self.olympus -= 10
        self.zeus == self.currentPlayerNum
    

    def Aphrodite(self):
        self.olympus = int(round(self.olympus, -1))
        self.zeus = self.currentPlayerNum


    def Apollo(self):
        self.zeus = self.currentPlayerNum


    def Ares(self):
        self.olympus = 50
        self.zeus = self.currentPlayerNum
    

    def Artemis(self):
        self.zeus = self.currentPlayerNum
    

    def Athena(self):
        self.turnCount +=1
        
        while (True):
            try:
                see = int(input("Which player's hand would you like to see? "))
                if (see == self.currentPlayer):
                    raise ValueError
                print("Their hand is: " + str(self.players[see]))
                break
            except:
                print("This won't work, you rascal. Give me an integer number that isn't yourself.")


    def Hermes(self):
        number = str(self.olympus)
        negative = (self.olympus < 0)
        if (not negative and len(number) == 1):
            number = '0' + number
        elif (negative and len(number) == 2):
            number = '0' + number[1]
        elif (negative and len(number) > 2):
            number = number[1:]
        self.olympus = int(number[::-1]) if not negative else int("-" + number[::-1])


    def Hera(self):
        self.olympus = 99
