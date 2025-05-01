# test/test_basic_game.py
print("This file is running.")
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

print("Python path:", sys.path)

from game.card import Card
from game.deck import Deck
from game.player import Player

def run_tests():
    print("Creating a deck and shuffling...")
    deck = Deck()
    print(f"Deck has {len(deck)} cards.\n")

    print("Creating two players: Alice and Bob")
    alice = Player("Alice")
    bob = Player("Bob")

    print("Dealing 7 cards to each player...")
    for _ in range(7):
        alice.draw_card(deck.draw())
        bob.draw_card(deck.draw())

    print("\nAlice's hand:")
    print(alice.hand)

    print("\nBob's hand:")
    print(bob.hand)

    print("\nAlice plays a set of 3 cards (mocked for now):")
    example_set = alice.hand[:3]
    alice.play_set(example_set)
    print("Played set:", example_set)

    print("\nAlice's remaining hand:")
    print(alice.hand)

    print("\nChecking Alice's points in a round where 'A' is the trump:")
    trump_rank = 'A'
    print("Points from played cards:", alice.get_played_points(trump_rank))
    print("Penalty from hand:", alice.get_hand_penalty(trump_rank))

    print("\nTest complete.")

if __name__ == "__main__":
    print("About to run tests...")
    run_tests()
    print("Tests completed.")