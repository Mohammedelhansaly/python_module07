from ex0.CreatureCard import CreatureCard
from .ArtifactCard import ArtifactCard
from .SpellCard import SpellCard
from .Deck import Deck


def main():
    print("=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")
    creature = CreatureCard("Fire Dragon", 5, "legedary", 7, 5)
    spell = SpellCard("Lightning Bolt", 3, "rare", "damage")
    artifact = ArtifactCard("Mana Crystal", 2, "Legendary", 3, "heal")
    deck = Deck()
    deck.add_card(creature)
    deck.add_card(spell)
    deck.add_card(artifact)
    print(f"Deck stats: {deck.get_deck_state()}")
    print("\nDrawing and playing cards:\n")
    deck.shuffle()
    for _ in range(len(deck.cards)):
        draw_card = deck.draw_card()
        if isinstance(draw_card, CreatureCard):
            category = "Creature"
        elif isinstance(draw_card, SpellCard):
            category = "Spell"
        else:
            category = "Artifact"
        print(f"Drew: {draw_card.name} ({category})")
        game_state = draw_card.play({})
        print(f"Play result: {game_state}\n")
    print("\nPolymorphism in action: Same interface, different card "
          "behaviors!")


if __name__ == "__main__":
    main()
