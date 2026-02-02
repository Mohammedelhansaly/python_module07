from ex0.Card import Card
from ex2.Combatable import Combatable
from .Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str,
                 damage: int, defense_damage: int, card_id: str, rating: int):
        Card.__init__(self, name, cost, rarity)
        Combatable.__init__(self, damage, defense_damage)
        self.card_id = card_id
        self.wins = 0
        self.losses = 0
        self.rating = rating

    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Tournament card played'
        }

    def attack(self, target) -> dict:
        target_name = target if isinstance(target, str) else str(target)
        return {
            "attacker": self.name,
            "target": target_name,
            "damage": self.damage,
            "combat_type": 'tournament'
        }

    def defend(self, damage):
        actual_damage = max(0, damage - self.defense_damage)
        return {
            "defender": self.name,
            "incoming_damage": damage,
            "defense_damage": self.defense_damage,
            "actual_damage_taken": actual_damage
        }

    def get_combat_stats(self):
        return {
            "damage": self.damage,
            "defense_damage": self.defense_damage
        }

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating += 16 * wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.rating -= 16 * losses

    def get_rank_info(self) -> dict:
        return {
            "rating": self.calculate_rating(),
            "record": f"{self.wins}-{self.losses}"
        }

    def calculate_rating(self) -> int:
        return self.rating + (self.wins * 16) - (self.losses * 16)

    def get_tournament_stats(self) -> dict:
        return {
            "id": self.card_id,
            "name": self.name,
            "rating": self.calculate_rating(),
            "wins": self.wins,
            "losses": self.losses
        }

    def __str__(self):
        return f"{self.name} (ID: {self.card_id})"
