class Card():
    def __init__(self, value):
        self.value = value

    def __eq__(self,other):
        if not isinstance(other,Card):
            return NotImplemented
        else:
            return (self.value == other.value)
    
    def __str__(self):
        return(str(self.value))

class numCard(Card):
    def __init__(self, value):
        self.value = value

class godCard(Card):
    def __init__(self, value):
        self.value = value

