"""BlackJack Game"""

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7,
          'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}


#Create cards

class Card():
    """Clase qué define las cartas utilizadas"""
    def __init__ (self, suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__ (self):
        return f"{self.rank} of {self.suit}"

    def __len__(self):
        return len(self.suit * self.rank)

#Create a deck of 52 cards

class Deck():
    """Prepara la baraja para el juego actual"""
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))


    def shuffle(self):
        """Mezcla las cartas para comenzar el juego"""
        random.shuffle(self.deck)

    def __str__(self):
        actual_deck = ""
        for card in self.deck :
            actual_deck += "\n" +card.__str__()
        return f" The deck is: {actual_deck}"

    def deal(self):
        """Extrae una carta de la baraja para poder repartir"""
        last_card = self.deck.pop()
        return last_card

class Hand ():
    """Define la mano del jugador"""
    def __init__ (self):
        self.card = []
        self.value = 0
        self.aces = 0

    def adjust_aces(self):
        """Ajusta el valor del As en función de la mano"""
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

    def add_card(self, card):
        """Añade la carta a la mano del jugador"""
        self.card.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces += 1
            self.adjust_aces()

class Chip ():
    """Define las fichas y la mecánica de apuesta"""
    def __init__(self, total = 100):
        self.total = total
        self.bet = 0

    def win(self):
        """Calcula crédito al ganar"""
        self.total += self.bet

    def lose(self):
        """Calcula crédito al perder"""
        self.total -= self.bet


def new_bet (chips):
    """Solicita al usuario la apuesta"""
    while chips.bet == 0 or chips.bet > chips.total:
        try:
            chips.bet = int(input("Cuál es tu apuesta? "))
            if chips.bet > chips.total:
                print (f"Saldo insuficiente. Te queda {chips.total}")
        except TypeError:
            print ("La cantidad no es correcta")
    return chips.bet

class Game():
    """Define la mecánica del juego"""
    def __init__(self, response = None, deck = None, player_hand = None, dealer_hand = None):
        self.response = response
        self.player_hand = player_hand
        self.dealer_hand = dealer_hand
        self.deck = deck
        self.player_chip = Chip()
        self.winner = False

    def game_setup(self):
        """Muestra la mano inicial del jugador y de la banca"""
        self.winner = False
        self.deck= Deck()
        self.deck.shuffle()

        self.player_hand = Hand()
        self.dealer_hand = Hand()

        new_bet(self.player_chip)

        self.player_hand.add_card(self.deck.deal())
        self.player_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())

        self.print_table("player")

    def start_game_player(self):
        """Evalua la continuidad del juego en funcion
        de la decisión del jugador"""
        self.player_hand.value = 21
        if self.player_hand.value == 21:
            self.check_winner()
        else:
            self.response = input("Quieres una nueva carta? S/N ")
            while self.response.upper() == "S":
                self.player_hand.add_card(self.deck.deal())
                self.print_table(turno = "player")
                if self.player_hand.value >= 21:
                    self.check_winner()
                    if self.winner is True:
                        break
                self.response = input("Quieres una nueva carta? S/N ")

    def start_game_dealer(self):
        """Inicia la mano de la banca"""
        while self.dealer_hand.value <= 17:
            self.dealer_hand.add_card(self.deck.deal())
            self.print_table(turno = "dealer")
            self.check_winner()

    def print_table(self,turno):
        """Muestra la situación actual de la mesa"""
        print("\nPlayer")
        print(self.player_hand.value)

        for cards in self.player_hand.card:
            print(cards)
        print("\nDealer")

        if turno == "player":
            for cards in self.dealer_hand.card[1:]:
                print(cards)
        else:
            print(self.dealer_hand.value)
            for cards in self.dealer_hand.card:
                print(cards)
        print("\n")

    def check_winner(self):
        """Comprueba si existe ganador"""
        while self.winner is False:
            if self.player_hand.value > 21:
                print("Te has pasado. La máquina gana")
                self.player_chip.lose()
                self.winner = True

            elif self.dealer_hand.value == 21:
                print("La máquina gana")
                self.player_chip.lose()
                self.winner = True

            elif self.player_hand.value == 21:
                print("Has ganado")
                self.player_chip.win()
                self.winner = True

            elif self.dealer_hand.value > 21:
                print("Has ganado")
                self.player_chip.win()
                self.winner = True

            elif self.player_hand.value > self.dealer_hand.value and self.dealer_hand.value >= 17:
                print("Has ganado")
                self.player_chip.win()
                self.winner = True

            elif self.dealer_hand.value > self.player_hand.value:
                print("La máquina gana")
                self.player_chip.lose()
                self.winner = True

            elif self.dealer_hand.value == self.player_hand.value:
                print("Empate")
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
