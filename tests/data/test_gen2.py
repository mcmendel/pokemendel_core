"""Tests for Generation 2 Pokemon data."""

import pytest
from pokemendel_core.data.gen2 import PokemonGen2, NAME_TO_POKEMON
from pokemendel_core.utils.definitions.types import Types
from pokemendel_core.utils.definitions.colors import Colors
from pokemendel_core.utils.definitions.categories import Categories
from pokemendel_core.utils.definitions.genders import Genders
from pokemendel_core.models.evolution import Evolution


def test_pokemon_count():
    """Test that there are exactly 251 Pokemon (Gen 1 + Gen 2)."""
    pokemon_names = [
        value for name, value in vars(PokemonGen2).items()
        if not name.startswith('_') and isinstance(value, str)
    ]
    assert len(pokemon_names) == 251, "There should be exactly 251 Pokemon (Gen 1 + Gen 2)"
    assert len(NAME_TO_POKEMON) == 251, "There should be exactly 251 Pokemon instances"


def test_name_to_pokemon_keys():
    """Test that each Pokemon's name matches its key in NAME_TO_POKEMON."""
    for key, pokemon in NAME_TO_POKEMON.items():
        assert key == pokemon.name, f"Pokemon {pokemon.name} has mismatched key {key}"


def test_pokemon_name_formatting():
    """Test that Pokemon names are properly formatted."""
    pokemon_names = [
        value for name, value in vars(PokemonGen2).items()
        if not name.startswith('_') and isinstance(value, str) and name.isupper()
    ]
    
    # Special cases where the second part should be lowercase
    special_cases = {
        "Ho-oh": ["Ho", "oh"],  # Second part should be lowercase
    }
    
    for name in pokemon_names:
        # Names should be properly capitalized
        assert name[0].isupper(), f"Pokemon name {name} should start with uppercase"
        # Rest of the name should be lowercase, except after hyphen or space
        parts = name.replace('-', ' ').split()
        
        if name in special_cases:
            assert parts == special_cases[name], f"Special case {name} should be formatted as specified"
        else:
            for part in parts:
                assert part[0].isupper(), f"Each word in {name} should start with uppercase"
                if len(part) > 1:
                    assert part[1:].islower() or part == "Mr.", f"Rest of {name} should be lowercase"


def test_special_pokemon_names():
    """Test special Pokemon names specific to Gen 2."""
    assert PokemonGen2.HO_OH == "Ho-oh", "Ho-oh should be properly formatted"
    assert PokemonGen2.PORYGON2 == "Porygon2", "Porygon2 should include the number"
    assert PokemonGen2.WOOPER == "Wooper", "Regular names should be unchanged"


def test_starter_pokemon():
    """Test Gen 2 starter Pokemon."""
    starters = {
        PokemonGen2.CHIKORITA: [PokemonGen2.BAYLEEF, PokemonGen2.MEGANIUM],
        PokemonGen2.CYNDAQUIL: [PokemonGen2.QUILAVA, PokemonGen2.TYPHLOSION],
        PokemonGen2.TOTODILE: [PokemonGen2.CROCONAW, PokemonGen2.FERALIGATR],
    }
    
    for starter, evolutions in starters.items():
        pokemon = NAME_TO_POKEMON[starter]
        assert pokemon.gen == 2, f"{starter} should be Gen 2"
        assert len(pokemon.evolves_to) == 1, f"{starter} should have one evolution"
        assert pokemon.evolves_to[0].name == evolutions[0], f"{starter} should evolve to {evolutions[0]}"
        
        mid_evolution = NAME_TO_POKEMON[evolutions[0]]
        assert mid_evolution.gen == 2, f"{evolutions[0]} should be Gen 2"
        assert len(mid_evolution.evolves_to) == 1, f"{evolutions[0]} should have one evolution"
        assert mid_evolution.evolves_to[0].name == evolutions[1], f"{evolutions[0]} should evolve to {evolutions[1]}"
        
        final_evolution = NAME_TO_POKEMON[evolutions[1]]
        assert final_evolution.gen == 2, f"{evolutions[1]} should be Gen 2"
        assert not final_evolution.evolves_to, f"{evolutions[1]} should not evolve further"


def test_legendary_pokemon():
    """Test Gen 2 legendary Pokemon."""
    legendaries = [
        PokemonGen2.RAIKOU,
        PokemonGen2.ENTEI,
        PokemonGen2.SUICUNE,
        PokemonGen2.LUGIA,
        PokemonGen2.HO_OH,
        PokemonGen2.CELEBI,
    ]
    
    for legendary in legendaries:
        pokemon = NAME_TO_POKEMON[legendary]
        assert pokemon.gen == 2, f"{legendary} should be Gen 2"
        assert not pokemon.evolves_to, f"{legendary} should not evolve"
        assert pokemon.supported_genders == [Genders.GENDERLESS], f"{legendary} should be genderless"


def test_baby_pokemon():
    """Test Gen 2 baby Pokemon and their evolutions."""
    babies = {
        PokemonGen2.PICHU: PokemonGen2.PIKACHU,
        PokemonGen2.CLEFFA: PokemonGen2.CLEFAIRY,
        PokemonGen2.IGGLYBUFF: PokemonGen2.JIGGLYPUFF,
        PokemonGen2.TOGEPI: PokemonGen2.TOGETIC,
        PokemonGen2.TYROGUE: [PokemonGen2.HITMONLEE, PokemonGen2.HITMONCHAN, PokemonGen2.HITMONTOP],
        PokemonGen2.SMOOCHUM: PokemonGen2.JYNX,
        PokemonGen2.ELEKID: PokemonGen2.ELECTABUZZ,
        PokemonGen2.MAGBY: PokemonGen2.MAGMAR,
    }
    
    for baby, evolution in babies.items():
        pokemon = NAME_TO_POKEMON[baby]
        assert pokemon.gen == 2, f"{baby} should be Gen 2"
        if isinstance(evolution, list):
            evolution_names = [e.name for e in pokemon.evolves_to]
            assert set(evolution_names) == set(evolution), f"{baby} should evolve to {evolution}"
        else:
            assert len(pokemon.evolves_to) == 1, f"{baby} should have one evolution"
            assert pokemon.evolves_to[0].name == evolution, f"{baby} should evolve to {evolution}"


def test_new_types():
    """Test Gen 2 Pokemon with new types (Dark and Steel)."""
    dark_pokemon = [name for name, pokemon in NAME_TO_POKEMON.items()
                   if Types.DARK in pokemon.types]
    steel_pokemon = [name for name, pokemon in NAME_TO_POKEMON.items()
                    if Types.STEEL in pokemon.types]
    
    assert PokemonGen2.UMBREON in dark_pokemon, "Umbreon should be Dark type"
    assert PokemonGen2.HOUNDOUR in dark_pokemon, "Houndour should be Dark type"
    assert PokemonGen2.HOUNDOOM in dark_pokemon, "Houndoom should be Dark type"
    assert PokemonGen2.TYRANITAR in dark_pokemon, "Tyranitar should be Dark type"
    
    assert PokemonGen2.STEELIX in steel_pokemon, "Steelix should be Steel type"
    assert PokemonGen2.SCIZOR in steel_pokemon, "Scizor should be Steel type"
    assert PokemonGen2.SKARMORY in steel_pokemon, "Skarmory should be Steel type"


def test_new_evolutions():
    """Test new evolutions of Gen 1 Pokemon introduced in Gen 2."""
    new_evolutions = {
        PokemonGen2.GOLBAT: PokemonGen2.CROBAT,
        PokemonGen2.GLOOM: PokemonGen2.BELLOSSOM,
        PokemonGen2.POLIWHIRL: PokemonGen2.POLITOED,
        PokemonGen2.SLOWPOKE: PokemonGen2.SLOWKING,
        PokemonGen2.ONIX: PokemonGen2.STEELIX,
        PokemonGen2.SCYTHER: PokemonGen2.SCIZOR,
        PokemonGen2.EEVEE: [PokemonGen2.ESPEON, PokemonGen2.UMBREON],
        PokemonGen2.PORYGON: PokemonGen2.PORYGON2,
    }
    
    for base, evolution in new_evolutions.items():
        pokemon = NAME_TO_POKEMON[base]
        if isinstance(evolution, list):
            evolution_names = {e.name for e in pokemon.evolves_to}
            for evo in evolution:
                assert evo in evolution_names, f"{base} should be able to evolve into {evo}"
                assert NAME_TO_POKEMON[evo].gen == 2, f"{evo} should be Gen 2"
        else:
            evolution_names = {e.name for e in pokemon.evolves_to}
            assert evolution in evolution_names, f"{base} should be able to evolve into {evolution}"
            assert NAME_TO_POKEMON[evolution].gen == 2, f"{evolution} should be Gen 2" 