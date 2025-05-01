# Aces-to-Kings-Card-Game
Time to recreate my favourite card game in code

Be the player to score the most points over 13 rounds, climbing from Aces to Kings. In each round, players try to lay down valid card sets to score points and minimise the penalty score for cards left in their hand.

Game Setup
    Players: 2 or more
    Deck: Standard 52-card deck (no jokers)
    Starting hand size: 7 cards per player
    Trump: Each round has a specific trump starting at Ace (round 1), then progressing to 2, 3, ..., King.

Gameplay Flow
1. Deal
    Shuffle the deck.
    Deal 7 cards to each player.
    Create a draw pile with the remaining cards.
    Flip 1 card face-up to start the discard pile.

2. Turns (per player, clockwise)
On your turn, do the following:
A. Draw Phase
Choose one:
    Draw 1 card from the draw pile,
    OR
    Take the entire discard pile, but you must immediately use at least one card from it in a valid set.
   
B. Play Sets (optional)
You may play any number of valid sets from your hand:
    Valid Set Types:
        Run: 3+ consecutive cards of the same suit (e.g. 4♥, 5♥, 6♥)
        Group: 3+ cards of the same rank (e.g. 7♦, 7♣, 7♠)
    Trump cards (cards matching the round’s rank, e.g. Aces in round 1) can substitute any card in a valid set.
    
C. Discard Phase
    Discard 1 card to the discard pile to end your turn.
