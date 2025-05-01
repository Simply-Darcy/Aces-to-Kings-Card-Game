from game.card import Card

class Player: 
    def __init__(self, name: str):
        self.name = name
        self.hand: list[Card] = []
        self.played_sets: list[list[Card]] = []
        self.score: int = 0

    def draw_card(self, card: Card):
        if card:
            self.hand.append(card)

    def discard_card(self, card: Card):
        if card in self.hand:
            self.hand.remove(card)
            return card
        return None
    
    def play_set(self, cards: list[Card]):
        for card in cards:
            if card not in self.hand:
                raise ValueError(f"{self.name} cannot play cards they dont have.")
        for card in cards:
            self.hand.remove(card)
        self.played_sets

    def get_played_points(self, trump_rank: str) -> int:
        total = 0
        for card_set in self.played_sets:
            for card in card_set:
                total += card.point_value(trump_rank)
        return total
    
    def get_hand_penalty(self, trump_rank: str) -> int:
        penalty = 0
        for card in self.hand:
            value = card.point_value(trump_rank)
            if card.rank == trump_rank:
                penalty += value * 2  # trump cards are double-penalty
            else:
                penalty += value
        return penalty
    
    def __repr__(self):
        return f"{self.name} - Hand: {self.hand} | Played: {self.played_sets} | Score: {self.score}" 