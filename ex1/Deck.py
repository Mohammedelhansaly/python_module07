from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
import random


class Deck():
    def __init__(self):
        self.cards:list[Card] = []
    def add_card(self,card:Card):
        self.cards.append(card)
    def remove_card(self,card_name:str):
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
    def shuffle(self):
        random.shuffle(self.cards)
    def draw_card(self)->Card:
        return self.cards.pop(0)
    def get_deck_state(self):
        avg = sum(card.cost for card in self.cards) / len(self.cards) if len(self.cards) else 0
        return {
            'total cards': len(self.cards),
            'creatures' : sum(isinstance(card,CreatureCard) for card in self.cards),
            'spells':sum(isinstance(card,SpellCard) for card in self.cards),
            'artifacts' : sum(isinstance(card,ArtifactCard) for card in self.cards),
            'avg_cost' : avg
        }
    
    