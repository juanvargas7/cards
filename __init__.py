import random

class deck:
    """
    Solitaire deck class
    """
    def __init__(self,a=1):
        types = 'Spade','Diamond','Hearts','Clover'
        numbers = 2,3,4,5,6,7,8,9,10,'J','Q','K','A'
        deck = list()
        for j in types:
            for i in numbers:
                deck.append([j,i])
        self.deck = deck * a
        self.len = len(deck)
        
    def shuffle(self):
        random.shuffle(self.deck)

    def draw(self,t = 1):
        if t == 1:
            if self.len <= 0:
                print('Empty deck')
                return None
            else:
                card = self.deck[0]
                del self.deck[0]
                self.len = self.len -1
                return card
        else:
            return [self.draw() for i in range(t)]
        
    def reset(self):
        types = 'Spade','Diamond','Hearts','Clover'
        numbers = 2,3,4,5,6,7,8,9,10,'J','Q','K','A'
        deck = list()
        for j in types:
            for i in numbers:
                deck.append([j,i])
        self.deck = deck
        self.len = len(deck)
        
    def ready(self):
        self.reset()
        self.shuffle()
