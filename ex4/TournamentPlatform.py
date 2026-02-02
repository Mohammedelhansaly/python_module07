from .TournamentCard import TournamentCard
import random


class TournamentPlatform:
    def __init__(self):
        self.cards: dict[str, TournamentCard] = {}
        self.match_played = 0

    def register_card(self, card: TournamentCard) -> str:
        self.cards[card.card_id] = card
        return card.card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]
        winner, loser = random.sample([card1, card2], 2)
        winner.update_wins(1)
        loser.update_losses(1)
        self.match_played += 1
        return {
            "winner": winner.name,
            "loser": loser.name,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating()
        }

    def get_leaderboard(self) -> list:
        return sorted(
            self.cards.values(),
            key=lambda c: c.rating,
            reverse=True
        )

    def generate_tournament_report(self) -> dict:
        ratings = [c.rating for c in self.cards.values()]
        return {
            "total_cards": len(self.cards),
            "matches_played": self.match_played,
            "avg_rating": sum(ratings) // len(ratings),
            "platform_status": "active"
        }
