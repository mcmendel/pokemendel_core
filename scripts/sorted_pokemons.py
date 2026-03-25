"""Print all Pokemon in a generation, ordered by evolution chains.

Usage:
    python -m scripts.sorted_pokemons <generation>

Example:
    python -m scripts.sorted_pokemons 1
"""
import argparse

from pokemendel_core.utils.evolutions import get_marked_pokemon_entries, is_eevee_family


def main():
    parser = argparse.ArgumentParser(
        description="Print Pokemon sorted by evolution chains for a given generation.",
    )
    parser.add_argument("generation", type=int, help="Generation number (e.g. 1)")
    args = parser.parse_args()

    for entry in get_marked_pokemon_entries(args.generation):
        parts: list[str] = [entry.name]
        if entry.base != entry.name and not is_eevee_family(entry.name, entry.base):
            parts.append(f"[{entry.base}]")
        if entry.evolution_details:
            parts.append(entry.evolution_details)
        print(" ".join(parts))


if __name__ == "__main__":
    main()
