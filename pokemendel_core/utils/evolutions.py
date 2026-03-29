"""
Utility functions for working with Pokemon evolution chains.

This module provides functions to analyze and iterate through Pokemon evolution chains,
supporting both forward (base to final) and reverse (final to base) traversal.
It also provides utilities for identifying "marked" Pokemon within evolution families
and formatting evolution path details.
"""
from pokemendel_core.models.pokemon import Pokemon
from pokemendel_core.models.evolution.evolution import Evolution
from pokemendel_core.models.evolution.evolution_type import EvolutionType
from pokemendel_core.data import list_gen_pokemons, map_gen_pokemons, fetch_pokemon
from pokemendel_core.data.utils.names import PokemonNames
from typing import Dict, Set, List, Generator, Tuple
from dataclasses import dataclass

EEVEE_FAMILY_BASES = {PokemonNames.EEVEE}


def _find_base_pokemons(pokemon_map: dict[str, Pokemon]) -> set[str]:
    """Find all base/root Pokemon that don't evolve from any other Pokemon.
    
    Args:
        pokemon_map: Dictionary mapping Pokemon names to Pokemon objects
        
    Returns:
        A set of Pokemon names that are base forms (don't evolve from any other Pokemon)
    """
    all_names = set(pokemon_map.keys())
    evolved_names = {evo.name for p in pokemon_map.values() for evo in p.evolves_to}
    roots = all_names - evolved_names
    return roots


def _trace_pokemon_evolutions(pokemon_map: dict[str, Pokemon], start: str) -> list[list[str]]:
    """Trace all possible evolution chains from a starting Pokemon using depth-first search.
    
    This function finds all possible evolution paths from a given Pokemon to its final forms.
    For example, for Bulbasaur it would return [['Bulbasaur', 'Ivysaur', 'Venusaur']].
    
    Args:
        pokemon_map: Dictionary mapping Pokemon names to Pokemon objects
        start: Name of the Pokemon to start tracing from
        
    Returns:
        A list of evolution chains, where each chain is a list of Pokemon names
        
    Example:
        >>> pokemon_map = {name: pokemon for name, pokemon in ...}
        >>> for root in _find_base_pokemons(pokemon_map):
        ...     for chain in _trace_pokemon_evolutions(pokemon_map, root):
        ...         print(" -> ".join(chain))
        Bulbasaur -> Ivysaur -> Venusaur
        Charmander -> Charmeleon -> Charizard
    """
    chains = []

    def dfs(path):
        last = path[-1]
        if not pokemon_map[last].evolves_to:
            chains.append(path)
            return
        for evo in pokemon_map[last].evolves_to:
            dfs(path + [evo.name])

    dfs([start])
    return chains


def iterate_gen_evolution_lines(gen: int, reversed: bool = False) -> Generator[List[str], None, None]:
    """Iterate through all evolution chains in a given generation.
    
    This function yields evolution chains for all Pokemon in the specified generation.
    Each chain is a list of Pokemon names representing a complete evolution line.
    
    Args:
        gen: The generation number to get evolution chains for (1 or 2)
        reversed: If True, chains are returned from final form to base form.
                 If False (default), chains are returned from base form to final form.
    
    Yields:
        Lists of Pokemon names representing evolution chains
        
    Example:
        >>> # Get all evolution chains in Gen 1 from base to final form
        >>> for chain in iterate_gen_evolution_lines(1, reversed=False):
        ...     print(" -> ".join(chain))
        Bulbasaur -> Ivysaur -> Venusaur
        Charmander -> Charmeleon -> Charizard
        
        >>> # Get all evolution chains in Gen 1 from final to base form
        >>> for chain in iterate_gen_evolution_lines(1, reversed=True):
        ...     print(" -> ".join(chain))
        Venusaur -> Ivysaur -> Bulbasaur
        Charizard -> Charmeleon -> Charmander
    """
    pokemon_map = {pokemon.name: pokemon for pokemon in list_gen_pokemons(gen)}
    for base_pokemon in _find_base_pokemons(pokemon_map):
        for evolution_chain in _trace_pokemon_evolutions(pokemon_map, base_pokemon):
            yield evolution_chain[::-1] if reversed else evolution_chain


@dataclass
class MarkedPokemonEntry:
    name: str
    base: str
    evolution_details: str


def find_marked_pokemons(pokemon_map: dict[str, Pokemon]) -> dict[str, str]:
    """Determine which Pokemon should be marked and map them to their base.

    Marking rules:
    - No split in evolution family: mark the base Pokemon.
    - Split exists: mark the Pokemon immediately after each branching point.
    - Eevee is always marked in addition to its evolutions.

    Args:
        pokemon_map: Dictionary mapping Pokemon names to Pokemon objects

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


def get_evolution_path(pokemon_map: dict[str, Pokemon], base: str, target: str) -> list[Evolution]:
    """Find the evolution path from base to target using BFS.

    Args:
        pokemon_map: Dictionary mapping Pokemon names to Pokemon objects
        base: Name of the base Pokemon to start from
        target: Name of the target Pokemon to reach

    Returns:
        List of Evolution objects representing each step from base to target.
    """
    queue: list[tuple[str, list[Evolution]]] = [(base, [])]
    while queue:
        current, path = queue.pop(0)
        for evo in pokemon_map[current].evolves_to:
            new_path = path + [evo]
            if evo.name == target:
                return new_path
            queue.append((evo.name, new_path))
    return []


def get_path_to_final(pokemon_map: dict[str, Pokemon], start: str) -> list[Evolution]:
    """Get evolutions from start down to its final (non-branching) form.

    Follows the evolution chain as long as each Pokemon has exactly one evolution.
    Stops at branching points or final forms.

    Args:
        pokemon_map: Dictionary mapping Pokemon names to Pokemon objects
        start: Name of the Pokemon to start from

    Returns:
        List of Evolution objects from start to its final linear descendant.
    """
    path: list[Evolution] = []
    current = start
    while pokemon_map[current].evolves_to:
        evos = pokemon_map[current].evolves_to
        if len(evos) > 1:
            break
        path.append(evos[0])
        current = evos[0].name
    return path


def get_full_evolution_path(pokemon_map: dict[str, Pokemon], name: str, base: str) -> list[Evolution]:
    """Get the full evolution path for a marked Pokemon: base -> marked -> final.

    Args:
        pokemon_map: Dictionary mapping Pokemon names to Pokemon objects
        name: The marked Pokemon name
        base: The base Pokemon name for this evolution family

    Returns:
        List of Evolution objects covering the entire path.
    """
    path_to_marked = get_evolution_path(pokemon_map, base, name) if base != name else []
    path_from_marked = get_path_to_final(pokemon_map, name)
    return path_to_marked + path_from_marked


def is_eevee_family(name: str, base: str) -> bool:
    """Check whether a Pokemon belongs to the Eevee evolution family."""
    return base in EEVEE_FAMILY_BASES or name in EEVEE_FAMILY_BASES


def get_marked_pokemon_entries(gen: int) -> list[MarkedPokemonEntry]:
    """Build a sorted list of marked Pokemon entries for a generation.

    Each entry contains the Pokemon name, its base form, and a formatted
    string describing the evolution path (empty when all-level or Eevee family).

    Args:
        gen: The generation number (e.g. 1, 2, 3, 4)

    Returns:
        Alphabetically sorted list of MarkedPokemonEntry.
    """
    pokemon_map = map_gen_pokemons(gen)
    marked = find_marked_pokemons(pokemon_map)

    entries: list[MarkedPokemonEntry] = []
    for name in sorted(marked):
        base = marked[name]

        if is_eevee_family(name, base):
            entries.append(MarkedPokemonEntry(name=name, base=base, evolution_details=""))
            continue

        full_path = get_full_evolution_path(pokemon_map, name, base)
        all_level = full_path and all(e.evolution_type == EvolutionType.LEVEL for e in full_path)
        has_special = any(e.special_information for e in full_path)

        if full_path and (not all_level or has_special):
            details = format_evolution_path(full_path)
        else:
            details = ""

        entries.append(MarkedPokemonEntry(name=name, base=base, evolution_details=details))

    return entries


def format_single_evolution(evo: Evolution) -> str:
    """Format a single evolution step.

    If the evolution type is LEVEL, returns "(level)".
    Otherwise returns "(<level if exists> <type>-<item if exists> <special info if exists>)".

    Args:
        evo: The Evolution object to format

    Returns:
        Formatted string for this evolution step.
    """
    if evo.evolution_type == EvolutionType.LEVEL and not evo.special_information:
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


def format_evolution_path(evolutions: list[Evolution]) -> str:
    """Format a full evolution path as a string.

    Args:
        evolutions: List of Evolution objects

    Returns:
        Formatted string like "(level) -> (stone-water stone)".
    """
    return " -> ".join(format_single_evolution(evo) for evo in evolutions)
