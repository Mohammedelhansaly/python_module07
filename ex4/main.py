from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main():
    print("=== DataDeck Tournament Platform ===\n")

    platform = TournamentPlatform()

    dragon = TournamentCard("Fire Dragon", 5, "Legendary",
                            4, 10, "dragon_001", 1200)
    wizard = TournamentCard("Ice Wizard", 4, "Epic",
                            7, 5, "wizard_001", 1150)

    print("Registering Tournament Cards...\n")
    for card in [dragon, wizard]:
        platform.register_card(card)
        print(f"{card.name} (ID: {card.card_id}):")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {card.rating}")
        print(f"- Record: {card.wins}-{card.losses}")
        print()
    print("Creating tournament match...")
    result = platform.create_match("dragon_001", "wizard_001")
    print("Match result:", result)
    print()
    print("Tournament Leaderboard:")
    for i, card in enumerate(platform.get_leaderboard(), start=1):
        info = card.get_rank_info()
        print(f"{i}. {card.name} - Rating: {info['rating']} "
              f"({info['record']})")
    print()
    print("Platform Report:")
    print(platform.generate_tournament_report())
    print()
    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
