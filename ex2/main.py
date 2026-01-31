from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from ex2.EliteCard import EliteCard


def main():
    print("=== DataDeck Ability System ===\n")
    print("EliteCard capabilities:")
    methods = [
        func for func in dir(Card)
        if callable(getattr(Card, func)) and not func.startswith("_")
    ]
    print(f"- Card methods: {methods}")
    methods = [
        func for func in dir(Combatable)
        if callable(getattr(Combatable, func)) and not func.startswith("_")
    ]
    print(f"- Combatable methods: {methods}")
    methods = [
        func for func in dir(Magical)
        if callable(getattr(Magical, func)) and not func.startswith("_")
    ]
    print(f"- Magical methods: {methods}")

    elite = EliteCard("Arcane Warrior", 4, "Epic", 8, 8, 4, 7)
    print(f"\nPlaying {elite.name} (Elite Card):\n")
    print("Combat phase:")
    print(f"Attack result: {elite.attack('Enemy')}")
    print(f"Defend result: {elite.defend(4)}")
    print("\nMagic phase:")
    print(f"Spell cast:: {elite.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}")
    print(f"Mana channel: {elite.channel_mana(3)}")
    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
