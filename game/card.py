class Card: 
    def __init__(self, rank: str, suit: str):
        self.rank = rank #eg. 'A', '2', '3', ..., '10', 'J', 'Q', 'K'
        self.suit = suit #eg. '♠', '♥', '♦', '♣'

    def __repr__(self):
        return f"{self.rank}{self.suit}"
    
    def point_value(self, trump_rank: str) -> int:
        if self.rank == trump_rank:
            return 25
        if self.rank == 'A':
            return 15
        if self.rank in ['10', 'J', 'Q', 'K']:
            return 10
        return 5