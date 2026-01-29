from Card import Card
from CreatureCard import CreatureCard


def main():
    card = Card(name="Fire Dragon", cost=5, rarity="Legendary")
    print("=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")
    print("CreatureCard Info:")
    creature = CreatureCard(card, attack=7, health=5)
    print(creature.get_info())
    mana_available = 6
    print(f"Playing {creature.name} with {mana_available} mana available:")
    print(f"Playable: {creature.is_playable(mana_available)}")
    print(f"Play result: {creature.play({})}\n")
    target = "Goblin Warrior"
    print(f"{creature.name} attacks {target}:")
    print(f"Attack result: {creature.attack_target(target)}\n")
    mana_available = 3
    print(f"Testing insufficient mana ({mana_available} available):")
    print(f"Playable: {creature.is_playable(mana_available)}\n")
    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
