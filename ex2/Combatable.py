from abc import ABC, abstractmethod


class Combatable(ABC):
    def __init__(self, damage: int, defense_damage: int):
        self.damage = damage
        self.defense_damage = defense_damage

    @abstractmethod
    def attack(self, target) -> dict:
        pass

    @abstractmethod
    def defend(self, damage) -> dict:
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict:
        pass
