from colorama import Fore, Back, Style
from termcolor import colored


import random 
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
winner = False

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
                print (f"Saldo insuficiente. Te queda {chips.total}")
        except:
            print ("La cantidad no es correcta")
    return chips.bet
            
class Game():
    def __init__(self):
        self.player_chip = Chip()
        self.winner = False

    def game_setup(self):
        self.winner = False
        self.new_deck = Deck()
        self.new_deck.shuffle()
        
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        
        new_bet(self.player_chip)
        
        self.player_hand.add_card(self.new_deck.deal())
        self.player_hand.add_card(self.new_deck.deal())
        self.dealer_hand.add_card(self.new_deck.deal())
        self.dealer_hand.add_card(self.new_deck.deal())

        self.print_table("player")
        return

            

    def start_game_player(self):
        self.player_hand.value = 21
        if self.player_hand.value == 21:
            self.check_winner()
        else:
            self.response = input("Quieres una nueva carta? S/N ")
            while self.response.upper() == "S":
                self.player_hand.add_card(self.new_deck.deal())
                self.print_table(turno = "player")  
                if self.player_hand.value >= 21:
                    self.check_winner()
                    if self.winner == True:
                        break
                self.response = input("Quieres una nueva carta? S/N ")
                     
            
    def start_game_dealer(self):

        while self.dealer_hand.value <= 17:       
            self.dealer_hand.add_card(self.new_deck.deal())     
            self.print_table(turno = "dealer")  
            self.check_winner()
     
     
    def print_table(self,turno):
        print(colored("\nPlayer", 'red'))
        print(colored(self.player_hand.value, 'yellow'))
        
        for cards in self.player_hand.card:
            print(cards)
        print(colored("\nDealer", 'green'))
        
        if turno == "player":
            for cards in self.dealer_hand.card[1:]:
                print(cards)
        else:
            print(colored(self.dealer_hand.value,'yellow'))
            for cards in self.dealer_hand.card:
                print(cards)
        print("\n")
        return


                    
    def check_winner(self):
        while self.winner == False:
            if self.player_hand.value > 21:
                print(colored ("Te has pasado. La máquina gana", 'light_magenta'))
                self.player_chip.lose()
                self.winner = True
            
            elif self.dealer_hand.value == 21:
                print(colored ("La máquina gana", 'light_magenta'))
                self.player_chip.lose()
                self.winner = True
            
            elif self.player_hand.value == 21:
                print(colored ("Has ganado", 'light_magenta'))
                self.player_chip.win()
                self.winner = True        
            
            elif self.dealer_hand.value > 21:
                print(colored ("Has ganado", 'light_magenta'))
                self.player_chip.win()               
                self.winner = True
            
            elif self.player_hand.value > self.dealer_hand.value and self.dealer_hand.value >= 17:
                print(colored ("Has ganado", 'light_magenta'))
                self.player_chip.win()   
                self.winner = True
            
            elif self.dealer_hand.value > self.player_hand.value:
                print(colored ("La máquina gana", 'light_magenta'))
                self.player_chip.lose()
                self.winner = True
                
            elif self.dealer_hand.value == self.player_hand.value:
                print(colored ("Empate", 'light_magenta'))
                self.winner = True
            else:
                return
        print(f"Tu nuevo saldo es: {self.player_chip.total}")    

             
                        
new_game = Game()

while new_game.player_chip.total>0:
    new_game.game_setup()
    new_game.start_game_player()
    new_game.start_game_dealer()
    new_game.player_chip.bet = 0
 


                    





    
