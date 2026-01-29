from .Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        if not isinstance(attack, int) and attack < 0:
            raise ValueError("Attack must be a non-negative integer")
        if not isinstance(health, int) and health < 0:
            raise ValueError("Health must be a non-negative integer")
        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        game_state = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        }
        return game_state

    def attack_target(self, target) -> dict:
        target_name = target if isinstance(target, str) else str(target)
        return {
            "attacker": self.name,
            "target": target_name,
            "damage_dealt": self.attack,
            "combat_resolved": True
        }

    def get_info(self) -> dict:
        info = super().get_card_info()
        info.update({
            "type": "Creature",
            "attack": self.attack,
            "health": self.health
        })
        return info
