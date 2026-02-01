from ex0.Card import Card
from .CardFactory import CardFactory
import random


class basicCard(Card):
    def __init__(self, name, cost, rarity):
        super().__init__(name, cost, rarity)

    def play(self, game_state: dict):
        print(f"{self.name} card played.")

    def __str__(self):
        return f"{self.name} ({self.cost})"


class FantasyCardFactory(CardFactory):
    def __init__(self):
        self.creature = {
                        "dragon": lambda: basicCard("Fire Dragon", 8,
                                                    "Legendary"),
                        "goblin": lambda: basicCard("Goblin Warrior", 2,
                                                    "Common")
        }
        self.spell = {"fireball": lambda: basicCard("Fireball", 5, "Rare"),
                      "lightning": lambda: basicCard("Lightning Bolt", 3,
                                                     "Uncommon")}
        self.artifact = {"mana_ring": lambda: basicCard("Mana Ring", 4,
                                                        "Rare")}

    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        return random.choice(list(self.creature.values()))()

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        return random.choice(list(self.spell.values()))()

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        return random.choice(list(self.artifact.values()))()

    def create_themed_deck(self, size: int) -> dict:
        deck = []
        for _ in range(size):
            deck.append(random.choice([
                self.create_creature(),
                self.create_spell(),
                self.create_artifact()
            ]))
        return {"deck": deck}

    def get_supported_types(self) -> dict:
        return {
            "creatures": list(self.creature.keys()),
            "spells": list(self.spell.keys()),
            "artifacts": list(self.artifact.keys()),
        }
