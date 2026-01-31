from ex0.Card import Card
from .Combatable import Combatable
from .Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: str,
                 damage: int, defense_damage: int, mana_cost: int,
                 spell_power: int):
        Card.__init__(self, name, cost, rarity)
        Combatable.__init__(self, damage, defense_damage)
        Magical.__init__(self, mana_cost, spell_power)

    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Elite card summoned to battlefield'
        }

    def attack(self, target):
        target_name = target if isinstance(target, str) else str(target)
        return {
            "attacker": self.name,
            "target": target_name,
            "damage": self.damage,
            "combat_type": 'melee'
        }

    def defend(self, incoming_damage: int):
        return {
            'defender': self.name,
            'damage_taken': incoming_damage - self.defense_damage,
            'damage_blocked': self.defense_damage,
            'still_alive': (incoming_damage - self.defense_damage) < 0
        }

    def get_combat_stats(self):
        return {
            'damage': self.damage,
            'defense_damage': self.defense_damage
        }

    def cast_spell(self, spell_name: str, targets: list):
        target_names = [target if isinstance(target, str) else str(target)
                        for target in targets]
        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': target_names,
            'mana_used': self.mana_cost,
        }

    def channel_mana(self, amount: int):
        return {
                'channeled': amount,
                'total_mana': self.mana_cost + amount
            }

    def get_magic_stats(self) -> dict:
        return {
            'spell_power': self.spell_power,
            'mana_cost': self.mana_cost
        }
