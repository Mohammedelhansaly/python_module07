class AggressiveStrategy():
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        cards_to_play = []
        mana_used = 0
        damage = 0
        hand_sorted = sorted(hand, key=lambda c: c.cost)
        for card in hand_sorted:
            if mana_used + card.cost <= 10:
                cards_to_play.append(card.name)
                mana_used += card.cost
                damage += getattr(card, 'power', 1)
        targets = self.prioritize_targets("Enemy Player")
        return {
            "cards_played": cards_to_play,
            "mana_used": mana_used,
            "targets_attacked": targets,
            "damage_dealt": damage
        }

    def get_strategy_name(self) -> str:
        return "Aggressive Strategy"

    def prioritize_targets(self, available_targets: list) -> list:
        if "Enemy Player" in available_targets:
            return ["Enemy Player"]
        return available_targets
