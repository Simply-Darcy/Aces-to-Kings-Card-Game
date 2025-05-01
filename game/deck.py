import random
from game.card import Card

SUITS = ['♠', '♥', '♦', '♣']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

class Deck:
    def __init__(self): # Create the 52-card deck
        self.cards = [Card(rank, suit) for suit in SUITS for rank in RANKS]
        random.shuffle(self.cards)

    def draw(self): #draw a card from the top of the deck
        return self.cards.pop() if self.cards else None
    
    def is_empty(self): # Check if the deck is empty
        return len(self.cards) == 0
    
    def __len__(self): #see how many cards are left in the deck
        return len(self.cards)