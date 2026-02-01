from .FantasyCardFactory import FantasyCardFactory
from .AggressiveStrategy import AggressiveStrategy
from .GameEngine import GameEngine

print("=== DataDeck Game Engine ===")

factory = FantasyCardFactory()
strategy = AggressiveStrategy()

engine = GameEngine()
engine.configure_engine(factory, strategy)

print("Configuring Fantasy Card Game...")
print("Factory:", factory.__class__.__name__)
print("Strategy:", strategy.get_strategy_name())
print("Available types:", factory.get_supported_types())
print()
print("Simulating aggressive turn...")
result = engine.simulate_turn()
hand = [
    factory.create_creature(),
    factory.create_creature(),
    factory.create_spell()
]
print("Player hand:", [str(card) for card in hand])
print("\nTurn execution:")
print("Strategy:", strategy.get_strategy_name())
print("Actions:", result)

print("\nGame Report:")
print(engine.get_engine_status())

print("\nAbstract Factory + Strategy Pattern: Maximum flexibility achieved!")
