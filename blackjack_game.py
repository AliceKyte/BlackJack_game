import random 
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
playing = True

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
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

          
    def shuffle(self):
        random.shuffle(self.deck)
                
    def __str__(self):
        actual_deck = ""
        for card in self.deck :
            actual_deck += "\n" +card.__str__()
        return f" The deck is: {actual_deck}"
            
    def deal(self):
        last_card = self.deck.pop()
        return last_card
    
class Hand ():
    def __init__ (self):
        self.card = []
        self.value = 0
        self.aces = 0
      
    def adjust_aces(self):
            while self.value > 21 and self.aces > 0:
                self.value -= 10
                self.aces -= 1         
            
    def add_card(self, card):
        self.card.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces += 1
            self.adjust_aces()
            
class Chip ():
    def __init__(self, total = 100):
        self.total = total
        self.bet = 0
        
    def win(self):
        self.total += self.bet
    
    def lose(self):
        self.total -= self.bet
                
def new_bet (chips):
    while chips.bet == 0 or chips.bet > chips.total:
        try:
            chips.bet = int(input("Cuál es tu apuesta? "))
            if chips.bet > chips.total:
                print (f"No hay pasta, te queda {chips.total}")
        except:
            print ("Escribe bien, coño!!!")
    return chips.bet
            
class Game():
    def __init__(self):
        self.new_deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.player_chip = Chip()

    def game_setup(self):
        self.new_deck = Deck()
        self.new_deck.shuffle()
        new_bet(self.player_chip)
        self.player_hand.add_card(self.new_deck.deal())
        self.player_hand.add_card(self.new_deck.deal())
        self.dealer_hand.add_card(self.new_deck.deal())
        self.dealer_hand.add_card(self.new_deck.deal())
        print("\nPlayer")
        print(self.player_hand.value)
        for cards in self.player_hand.card:
            print(cards)
        print("\nDealer")
        print(self.dealer_hand.value)
        for cards in self.dealer_hand.card[1:]:
            print(cards)
            print("\n")
        
        
    def start_game_player(self):
        while self.ask_new_card == "Y":  
            self.player_hand.add_card(self.new_deck.deal())  
            self.print_table(turno = "player")  
            self.check_continue()    
                     
            
    def start_game_dealer(self):
        while self.dealer_hand.value <= 17:       
            self.dealer_hand.add_card(self.new_deck.deal())     
            self.print_table(turno = "dealer")  
        self.check_continue()   
     
     
    def print_table(self,turno):
        print("\nPlayer")
        print(self.player_hand.value)
        for cards in self.player_hand.card:
            print(cards)
        print("\nDealer")
        print(self.dealer_hand.value)
        if turno == "player":
            for cards in self.dealer_hand.card[1:]:
                print(cards)
        else:
            for cards in self.dealer_hand.card:
                print(cards)
        print("\n")

            
    def ask_new_card(self):
            response = ""
            while self.player_hand.value < 21:
                
                response = input("Quieres una nueva carta? S/N ")
                
                if response.upper() == "S":
                    self.player_hand.add_card(self.new_deck.deal())
                    print(self.player_hand.value)
                    for cards in self.player_hand.card:
                        print(cards)
                    print("\nDealer")
                    for cards in self.dealer_hand.card[1:]:
                        print(cards)
                    print("\n")
            
                elif response.upper() == "N":
                    while self.dealer_hand.value < 17:
                        self.dealer_hand.add_card(self.new_deck.deal())
                        print(self.player_hand.value)
                        for cards in self.player_hand.card:
                            print(cards)
                        print("\nDealer")
                        print(self.dealer_hand.value)
                        for cards in self.dealer_hand.card:
                            print(cards)
                        print("\n")       
                        break    
                    
    def check_continue(self):
                
                if self.player_hand.value > 21:
                    print("Te has pasado. La máquina gana")
                    self.player_chip.lose()
                    return False
                
                elif self.dealer_hand.value == 21:
                    print("La máquina gana")
                    self.player_chip.lose()
                    return False 
                
                elif self.player_hand.value == 21:
                    print("Has ganado")
                    self.player_chip.win()
                    return False         
                
                elif self.dealer_hand.value > 21:
                    print("Has ganado")
                    self.player_chip.win()               
                    return False 
                
                elif self.player_hand.value > self.dealer_hand.value and self.dealer_hand.value >= 17:
                    print("Has ganado")
                    self.player_chip.win()   
                    return False 
                
                elif self.dealer_hand.value > self.player_hand.value:
                    print("La máquina gana")
                    self.player_chip.win()
                    return False 
                
                print(f"Tu nuevo saldo es: {self.player_chip.total}")    
                self.new_deck = Deck()
                self.new_deck.shuffle()
                self.player_hand = Hand()
                self.dealer_hand = Hand()            
                            
                    
"""-------Juego---------"""

new_game = Game()
new_game.game_setup()
