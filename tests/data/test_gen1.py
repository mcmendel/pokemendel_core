"""Tests for Generation 1 Pokemon data."""

import pytest
from pokemendel_core.data.gen1 import PokemonGen1, NAME_TO_POKEMON
from pokemendel_core.utils.definitions.types import Types
from pokemendel_core.utils.definitions.colors import Colors
from pokemendel_core.utils.definitions.categories import Categories
from pokemendel_core.models.evolution.evolution import Evolution
from pokemendel_core.models.evolution.evolution_type import EvolutionType
from pokemendel_core.models.evolution.items import Item


def test_pokemon_count():
    """Test that there are exactly 151 Generation 1 Pokemon."""
    pokemon_names = [
        value for name, value in vars(PokemonGen1).items()
        if not name.startswith('_') and isinstance(value, str)
    ]
    assert len(pokemon_names) == 151, "There should be exactly 151 Generation 1 Pokemon"
    assert len(NAME_TO_POKEMON) == 151, "There should be exactly 151 Pokemon instances"


def test_name_to_pokemon_keys():
    """Test that each key in NAME_TO_POKEMON matches the corresponding Pokemon's name."""
    for key, pokemon in NAME_TO_POKEMON.items():
        assert key == pokemon.name, f"Pokemon with key '{key}' has mismatched name '{pokemon.name}'"


def test_pokemon_name_formatting():
    """Test that Pokemon names are properly formatted."""
    pokemon_names = [
        value for name, value in vars(PokemonGen1).items()
        if not name.startswith('_') and isinstance(value, str)
    ]
    
    for name in pokemon_names:
        # Names should start with a capital letter
        assert name[0].isupper(), f"Pokemon name '{name}' should start with a capital letter"
        
        # Rest of the name should be lowercase, except after hyphen or space
        parts = name.replace('-', ' ').split()
        for part in parts:
            assert part[0].isupper(), f"Each word in '{name}' should start with a capital letter"
            # Skip validation for single-letter parts (like 'F' in 'Nidoran-F')
            if len(part) > 1:
                assert part[1:].islower(), f"Rest of word '{part}' in '{name}' should be lowercase"


def test_special_pokemon_names():
    """Test special cases in Pokemon names."""
    # Test Nidoran gender forms
    assert PokemonGen1.NIDORAN_F == "Nidoran-F"
    assert PokemonGen1.NIDORAN_M == "Nidoran-M"
    
    # Test Pokemon with special characters
    assert PokemonGen1.FARFETCHD == "Farfetch'd"
    assert PokemonGen1.MR_MIME == "Mr. Mime"
    
    # Test evolution families with special naming
    assert all(name in [
        getattr(PokemonGen1, attr) for attr in dir(PokemonGen1)
        if not attr.startswith('_')
    ] for name in [
        PokemonGen1.NIDORAN_F, PokemonGen1.NIDORINA, PokemonGen1.NIDOQUEEN,
        PokemonGen1.NIDORAN_M, PokemonGen1.NIDORINO, PokemonGen1.NIDOKING,
    ])


def test_starter_pokemon():
    """Test that starter Pokemon and their evolutions are present."""
    starters = {
        # Grass starter family
        PokemonGen1.BULBASAUR: "Bulbasaur",
        PokemonGen1.IVYSAUR: "Ivysaur",
        PokemonGen1.VENUSAUR: "Venusaur",
        # Fire starter family
        PokemonGen1.CHARMANDER: "Charmander",
        PokemonGen1.CHARMELEON: "Charmeleon",
        PokemonGen1.CHARIZARD: "Charizard",
        # Water starter family
        PokemonGen1.SQUIRTLE: "Squirtle",
        PokemonGen1.WARTORTLE: "Wartortle",
        PokemonGen1.BLASTOISE: "Blastoise",
    }
    
    for constant, name in starters.items():
        assert constant == name


def test_legendary_pokemon():
    """Test that all legendary Pokemon are present."""
    legendaries = {
        PokemonGen1.ARTICUNO: "Articuno",
        PokemonGen1.ZAPDOS: "Zapdos",
        PokemonGen1.MOLTRES: "Moltres",
        PokemonGen1.MEWTWO: "Mewtwo",
        PokemonGen1.MEW: "Mew",
    }
    
    for constant, name in legendaries.items():
        assert constant == name


def test_pokemon_instances():
    """Test that Pokemon instances are properly created with correct data."""
    # Test Bulbasaur's complete data
    bulbasaur = next(p for p in NAME_TO_POKEMON.values() if p.name == PokemonGen1.BULBASAUR)
    assert bulbasaur.gen == 1
    assert bulbasaur.types == [Types.GRASS, Types.POISON]
    assert len(bulbasaur.evolves_to) == 1
    assert bulbasaur.evolves_to[0].name == PokemonGen1.IVYSAUR
    assert bulbasaur.colors == [Colors.GREEN, Colors.BLUE]
    assert Categories.PLANT in bulbasaur.categories
    assert bulbasaur.num_legs == 4

    # Test Charizard's complete data
    charizard = next(p for p in NAME_TO_POKEMON.values() if p.name == PokemonGen1.CHARIZARD)
    assert charizard.gen == 1
    assert charizard.types == [Types.FIRE, Types.FLYING]
    assert len(charizard.evolves_to) == 0  # Final evolution
    assert Colors.ORANGE in charizard.colors
    assert Categories.DRAGON in charizard.categories
    assert charizard.num_legs == 2

    # Test Eevee's evolution data
    eevee = next(p for p in NAME_TO_POKEMON.values() if p.name == PokemonGen1.EEVEE)
    assert len(eevee.evolves_to) == 3
    eeveelutions = {e.name: e for e in eevee.evolves_to}
    assert PokemonGen1.VAPOREON in eeveelutions
    assert PokemonGen1.JOLTEON in eeveelutions
    assert PokemonGen1.FLAREON in eeveelutions
    assert eeveelutions[PokemonGen1.VAPOREON].evolution_type == EvolutionType.STONE
    assert eeveelutions[PokemonGen1.VAPOREON].item == Item.WATER_STONE


def test_pokemon_evolution_chains():
    """Test that evolution chains are properly defined."""
    # Test Charmander evolution chain
    charmander = next(p for p in NAME_TO_POKEMON.values() if p.name == PokemonGen1.CHARMANDER)
    assert len(charmander.evolves_to) == 1
    assert charmander.evolves_to[0].name == PokemonGen1.CHARMELEON
    
    charmeleon = next(p for p in NAME_TO_POKEMON.values() if p.name == PokemonGen1.CHARMELEON)
    assert len(charmeleon.evolves_to) == 1
    assert charmeleon.evolves_to[0].name == PokemonGen1.CHARIZARD
    
    charizard = next(p for p in NAME_TO_POKEMON.values() if p.name == PokemonGen1.CHARIZARD)
    assert len(charizard.evolves_to) == 0  # Final evolution

    # Test trade evolution
    haunter = next(p for p in NAME_TO_POKEMON.values() if p.name == PokemonGen1.HAUNTER)
    assert len(haunter.evolves_to) == 1
    assert haunter.evolves_to[0].name == PokemonGen1.GENGAR
    assert haunter.evolves_to[0].evolution_type == EvolutionType.TRADE


def test_pokemon_types():
    """Test that Pokemon types are correctly assigned."""
    type_counts = {}
    for pokemon in NAME_TO_POKEMON.values():
        for type_ in pokemon.types:
            type_counts[type_] = type_counts.get(type_, 0) + 1
    
    # Verify some type distributions
    assert type_counts[Types.NORMAL] > 20  # Normal was a common type
    assert type_counts[Types.DRAGON] < 5   # Dragon was a rare type
    assert Types.STEEL not in type_counts  # Steel type wasn't introduced until Gen 2
    assert Types.DARK not in type_counts   # Dark type wasn't introduced until Gen 2 