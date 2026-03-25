"""Print all Pokemon in a generation, ordered by evolution chains.

Usage:
    python -m scripts.sorted_pokemons <generation>

Example:
    python -m scripts.sorted_pokemons 1
"""
import argparse

from pokemendel_core.data import map_gen_pokemons
from pokemendel_core.data.utils.names import PokemonNames
from pokemendel_core.models.evolution.evolution import Evolution
from pokemendel_core.models.evolution.evolution_type import EvolutionType
from pokemendel_core.models.pokemon import Pokemon
from pokemendel_core.utils.evolutions import _find_base_pokemons

EEVEE_FAMILY_BASES = {PokemonNames.EEVEE}


def _find_marked_pokemons(pokemon_map: dict[str, Pokemon]) -> dict[str, str]:
    """Determine which Pokemon should be marked and map them to their base.

    - No split: mark the base Pokemon.
    - Split exists: mark the Pokemon immediately after each branching point.
    - Eevee is always marked in addition to its evolutions.

    Returns:
        dict mapping marked Pokemon name -> its base Pokemon name.
    """
    marked: dict[str, str] = {}

    for base in _find_base_pokemons(pokemon_map):
        has_branch = False
        stack = [base]
        while stack:
            name = stack.pop()
            evolutions = pokemon_map[name].evolves_to
            if len(evolutions) > 1:
                has_branch = True
                for evo in evolutions:
                    marked[evo.name] = base
            for evo in evolutions:
                stack.append(evo.name)

        if not has_branch:
            marked[base] = base

    for name in EEVEE_FAMILY_BASES:
        if name in pokemon_map:
            marked[name] = name

    return marked


def _get_evolution_path(pokemon_map: dict[str, Pokemon], base: str, target: str) -> list[Evolution]:
    """Find the evolution path from base to target using BFS."""
    queue: list[tuple[str, list[Evolution]]] = [(base, [])]
    while queue:
        current, path = queue.pop(0)
        for evo in pokemon_map[current].evolves_to:
            new_path = path + [evo]
            if evo.name == target:
                return new_path
            queue.append((evo.name, new_path))
    return []


def _get_path_to_final(pokemon_map: dict[str, Pokemon], start: str) -> list[Evolution]:
    """Get evolutions from start down to its final (non-branching) form."""
    path: list[Evolution] = []
    current = start
    while pokemon_map[current].evolves_to:
        evos = pokemon_map[current].evolves_to
        if len(evos) > 1:
            break
        path.append(evos[0])
        current = evos[0].name
    return path


def _format_single_evolution(evo: Evolution) -> str:
    if evo.evolution_type == EvolutionType.LEVEL:
        return "(level)"
    parts: list[str] = []
    if evo.level is not None:
        parts.append(str(evo.level))
    type_str = evo.evolution_type.value
    if evo.item is not None:
        type_str += f"-{evo.item.value.lower()}"
    parts.append(type_str)
    if evo.special_information is not None:
        parts.append(evo.special_information)
    return f"({' '.join(parts)})"


def _format_evolution_path(evolutions: list[Evolution]) -> str:
    return " -> ".join(_format_single_evolution(evo) for evo in evolutions)


def main():
    parser = argparse.ArgumentParser(
        description="Print Pokemon sorted by evolution chains for a given generation.",
    )
    parser.add_argument("generation", type=int, help="Generation number (e.g. 1)")
    args = parser.parse_args()

    pokemon_map = map_gen_pokemons(args.generation)
    marked = _find_marked_pokemons(pokemon_map)

    lines: list[str] = []
    for name in sorted(marked):
        base = marked[name]
        is_eevee_family = base in EEVEE_FAMILY_BASES or name in EEVEE_FAMILY_BASES

        if is_eevee_family:
            lines.append(name)
            continue

        if base == name:
            label = name
        else:
            label = f"{name} [{base}]"

        path_to_marked = _get_evolution_path(pokemon_map, base, name) if base != name else []
        path_from_marked = _get_path_to_final(pokemon_map, name)
        full_path = path_to_marked + path_from_marked

        all_level = full_path and all(e.evolution_type == EvolutionType.LEVEL for e in full_path)
        if full_path and not all_level:
            lines.append(f"{label} {_format_evolution_path(full_path)}")
        else:
            lines.append(label)

    for line in lines:
        print(line)


if __name__ == "__main__":
    main()
