suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
deck = []


#Create cards

class Card():
    def __init__ (self, suit,rank):
        self.suit = suit
        self.rank = rank
        
    def __str__ (self):
        return f"{self.rank} of {self.suit}"

#Create a deck of 52 cards

class Deck():
    def __init__(self):
        for suit in suits:
            for rank in ranks:
                deck.append(Card(suit,rank))
                
    def __str__(self):
        return f"The deck is: {deck}"
    

        
new_deck = Deck()
print(new_deck)
print(deck[8])