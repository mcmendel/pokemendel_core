"""Test script to verify pokemendel_core package installation and usage."""

from pokemendel_core import (
    PokemonGen2,
    NAME_TO_POKEMON,
    Types,
    Genders,
)

def main():
    # Test accessing a Gen 2 Pokémon
    tyranitar = NAME_TO_POKEMON[PokemonGen2.TYRANITAR]
    print(f"\nTesting Tyranitar data:")
    print(f"Name: {tyranitar.name}")
    print(f"Types: {[t.value for t in tyranitar.types]}")
    print(f"Generation: {tyranitar.gen}")
    print(f"Stats: Attack={tyranitar.stats.attack}, Defence={tyranitar.stats.defence}")
    print(f"Genders: {[g.value for g in tyranitar.supported_genders]}")

    # Test accessing a Dark-type Pokémon
    umbreon = NAME_TO_POKEMON[PokemonGen2.UMBREON]
    print(f"\nTesting Umbreon data:")
    print(f"Name: {umbreon.name}")
    print(f"Types: {[t.value for t in umbreon.types]}")
    print(f"Special Defence: {umbreon.stats.special_defence}")

    # Test evolution chain
    houndour = NAME_TO_POKEMON[PokemonGen2.HOUNDOUR]
    evolution = houndour.evolves_to[0]
    print(f"\nTesting evolution chain:")
    print(f"{houndour.name} evolves to {evolution.name}")

if __name__ == "__main__":
    main() 