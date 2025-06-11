"""
Tests for Pokemon evolution utilities.
"""
import pytest
from pokemendel_core.utils.evolutions import (
    _find_base_pokemons,
    _trace_pokemon_evolutions,
    iterate_gen_evolution_lines,
)
from pokemendel_core.data import list_gen_pokemons
from pokemendel_core.models.pokemon import Pokemon


@pytest.fixture
def gen1_pokemon_map():
    """Fixture providing a map of Gen 1 Pokemon names to Pokemon objects."""
    return {pokemon.name: pokemon for pokemon in list_gen_pokemons(1)}


@pytest.fixture
def gen2_pokemon_map():
    """Fixture providing a map of Gen 2 Pokemon names to Pokemon objects."""
    return {pokemon.name: pokemon for pokemon in list_gen_pokemons(2)}


def test_find_base_pokemons_gen1(gen1_pokemon_map):
    """Test finding base Pokemon in Gen 1."""
    base_pokemon = _find_base_pokemons(gen1_pokemon_map)
    # Check that some key Gen 1 base Pokémon are present
    for name in [
        'Bulbasaur', 'Charmander', 'Squirtle', 'Pikachu', 'Eevee', 'Dratini', 'Snorlax', 'Mewtwo', 'Mew'
    ]:
        assert name in base_pokemon


def test_find_base_pokemons_gen2(gen2_pokemon_map):
    """Test finding base Pokemon in Gen 2."""
    base_pokemon = _find_base_pokemons(gen2_pokemon_map)
    # Check that some key Gen 2 base Pokémon are present
    for name in [
        'Chikorita', 'Cyndaquil', 'Totodile', 'Pichu', 'Togepi', 'Mareep', 'Marill', 'Larvitar', 'Celebi'
    ]:
        assert name in base_pokemon


def test_trace_pokemon_evolutions_gen1(gen1_pokemon_map):
    """Test tracing evolution chains in Gen 1."""
    # Test a three-stage evolution
    bulbasaur_chains = _trace_pokemon_evolutions(gen1_pokemon_map, 'Bulbasaur')
    assert len(bulbasaur_chains) == 1
    assert bulbasaur_chains[0] == ['Bulbasaur', 'Ivysaur', 'Venusaur']
    
    # Test a two-stage evolution
    pikachu_chains = _trace_pokemon_evolutions(gen1_pokemon_map, 'Pikachu')
    assert len(pikachu_chains) == 1
    assert pikachu_chains[0] == ['Pikachu', 'Raichu']
    
    # Test a Pokemon with no evolutions
    tauros_chains = _trace_pokemon_evolutions(gen1_pokemon_map, 'Tauros')
    assert len(tauros_chains) == 1
    assert tauros_chains[0] == ['Tauros']


def test_trace_pokemon_evolutions_gen2(gen2_pokemon_map):
    """Test tracing evolution chains in Gen 2."""
    # Test a three-stage evolution
    chikorita_chains = _trace_pokemon_evolutions(gen2_pokemon_map, 'Chikorita')
    assert len(chikorita_chains) == 1
    assert chikorita_chains[0] == ['Chikorita', 'Bayleef', 'Meganium']
    
    # Test a two-stage evolution
    marill_chains = _trace_pokemon_evolutions(gen2_pokemon_map, 'Marill')
    assert len(marill_chains) == 1
    assert marill_chains[0] == ['Marill', 'Azumarill']
    
    # Test a Pokemon with no evolutions
    dunsparce_chains = _trace_pokemon_evolutions(gen2_pokemon_map, 'Dunsparce')
    assert len(dunsparce_chains) == 1
    assert dunsparce_chains[0] == ['Dunsparce']


def test_iterate_gen_evolution_lines_gen1():
    """Test iterating through evolution lines in Gen 1."""
    # Test forward evolution (base to final)
    chains = list(iterate_gen_evolution_lines(1, reversed=False))
    
    # Verify some known evolution chains
    assert ['Bulbasaur', 'Ivysaur', 'Venusaur'] in chains
    assert ['Charmander', 'Charmeleon', 'Charizard'] in chains
    assert ['Pikachu', 'Raichu'] in chains
    assert ['Tauros'] in chains
    
    # Test reverse evolution (final to base)
    reverse_chains = list(iterate_gen_evolution_lines(1, reversed=True))
    
    # Verify the same chains in reverse
    assert ['Venusaur', 'Ivysaur', 'Bulbasaur'] in reverse_chains
    assert ['Charizard', 'Charmeleon', 'Charmander'] in reverse_chains
    assert ['Raichu', 'Pikachu'] in reverse_chains
    assert ['Tauros'] in reverse_chains  # Single Pokemon chains stay the same


def test_iterate_gen_evolution_lines_gen2():
    """Test iterating through evolution lines in Gen 2."""
    # Test forward evolution (base to final)
    chains = list(iterate_gen_evolution_lines(2, reversed=False))
    
    # Verify some known evolution chains
    assert ['Chikorita', 'Bayleef', 'Meganium'] in chains
    assert ['Cyndaquil', 'Quilava', 'Typhlosion'] in chains
    assert ['Marill', 'Azumarill'] in chains
    assert ['Dunsparce'] in chains
    
    # Test reverse evolution (final to base)
    reverse_chains = list(iterate_gen_evolution_lines(2, reversed=True))
    
    # Verify the same chains in reverse
    assert ['Meganium', 'Bayleef', 'Chikorita'] in reverse_chains
    assert ['Typhlosion', 'Quilava', 'Cyndaquil'] in reverse_chains
    assert ['Azumarill', 'Marill'] in reverse_chains
    assert ['Dunsparce'] in reverse_chains  # Single Pokemon chains stay the same


def test_invalid_generation():
    """Test that invalid generation numbers raise appropriate errors."""
    with pytest.raises(ValueError):
        list(iterate_gen_evolution_lines(0))  # Generation 0 doesn't exist
    
    with pytest.raises(ValueError):
        list(iterate_gen_evolution_lines(3))  # Only Gen 1 and 2 are supported 