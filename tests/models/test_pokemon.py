"""Tests for the Pokemon class."""

import pytest
from pokemendel_core.models.pokemon import Pokemon
from pokemendel_core.utils.definitions.types import Types
from pokemendel_core.utils.definitions.colors import Colors
from pokemendel_core.utils.definitions.genders import Genders
from pokemendel_core.utils.definitions.categories import Categories
from pokemendel_core.utils.definitions.stats import Stats
from pokemendel_core.models.evolution import Evolution


def test_pokemon_creation_minimal():
    """Test creating a Pokemon with minimal required attributes."""
    pokemon = Pokemon(
        name="Bulbasaur",
        gen=1,
        types=[Types.GRASS, Types.POISON]
    )
    assert pokemon.name == "Bulbasaur"
    assert pokemon.gen == 1
    assert pokemon.types == [Types.GRASS, Types.POISON]
    assert pokemon.stats is None
    assert pokemon.evolves_to == []
    assert pokemon.colors == []
    assert pokemon.supported_genders == []
    assert pokemon.categories == []
    assert pokemon.num_legs == -1


def test_pokemon_creation_full():
    """Test creating a Pokemon with all attributes."""
    stats = Stats(attack=49, defence=49, special_attack=65, special_defence=65)
    evolution = Evolution(name="Ivysaur")
    
    pokemon = Pokemon(
        name="Bulbasaur",
        gen=1,
        types=[Types.GRASS, Types.POISON],
        stats=stats,
        evolves_to=[evolution],
        colors=[Colors.GREEN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        categories=[Categories.PLANT],
        num_legs=4
    )
    
    assert pokemon.name == "Bulbasaur"
    assert pokemon.gen == 1
    assert pokemon.types == [Types.GRASS, Types.POISON]
    assert pokemon.stats == stats
    assert pokemon.evolves_to == [evolution]
    assert pokemon.colors == [Colors.GREEN]
    assert pokemon.supported_genders == [Genders.MALE, Genders.FEMALE]
    assert pokemon.categories == [Categories.PLANT]
    assert pokemon.num_legs == 4


def test_pokemon_evolution():
    """Test evolving a Pokemon into another Pokemon."""
    # Create initial Pokemon (Charmander)
    charmander = Pokemon(
        name="Charmander",
        gen=1,
        types=[Types.FIRE],
        stats=Stats(attack=52, defence=43, special_attack=60, special_defence=50),
        colors=[Colors.RED],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        categories=[Categories.DRAGON],
        num_legs=2
    )
    
    # Create evolved Pokemon (Charmeleon)
    charmeleon = Pokemon(
        name="Charmeleon",
        gen=1,
        types=[Types.FIRE],
        stats=Stats(attack=64, defence=58, special_attack=80, special_defence=65),
        colors=[Colors.RED],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        categories=[Categories.DRAGON],
        num_legs=2
    )
    
    # Evolve Charmander to Charmeleon
    charmander.evolve_pokemon(charmeleon)
    
    # Verify all attributes were updated
    assert charmander.name == "Charmeleon"
    assert charmander.types == [Types.FIRE]
    assert charmander.stats == charmeleon.stats
    assert charmander.colors == [Colors.RED]
    assert charmander.supported_genders == [Genders.MALE, Genders.FEMALE]
    assert charmander.categories == [Categories.DRAGON]
    assert charmander.num_legs == 2
    assert charmander.evolves_to == []


def test_pokemon_equality():
    """Test that two Pokemon instances with the same attributes are equal."""
    stats = Stats(attack=49, defence=49, special_attack=65, special_defence=65)
    
    pokemon1 = Pokemon(
        name="Bulbasaur",
        gen=1,
        types=[Types.GRASS, Types.POISON],
        stats=stats,
        colors=[Colors.GREEN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        categories=[Categories.PLANT],
        num_legs=4
    )
    
    pokemon2 = Pokemon(
        name="Bulbasaur",
        gen=1,
        types=[Types.GRASS, Types.POISON],
        stats=stats,
        colors=[Colors.GREEN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        categories=[Categories.PLANT],
        num_legs=4
    )
    
    assert pokemon1 == pokemon2


def test_pokemon_inequality():
    """Test that two Pokemon instances with different attributes are not equal."""
    pokemon1 = Pokemon(
        name="Bulbasaur",
        gen=1,
        types=[Types.GRASS, Types.POISON]
    )
    
    pokemon2 = Pokemon(
        name="Ivysaur",  # Different name
        gen=1,
        types=[Types.GRASS, Types.POISON]
    )
    
    assert pokemon1 != pokemon2


def test_pokemon_list_field_independence():
    """Test that list fields are independent between instances."""
    pokemon1 = Pokemon(
        name="Bulbasaur",
        gen=1,
        types=[Types.GRASS, Types.POISON]
    )
    
    pokemon2 = Pokemon(
        name="Bulbasaur",
        gen=1,
        types=[Types.GRASS, Types.POISON]
    )
    
    # Modify lists in pokemon1
    pokemon1.colors.append(Colors.GREEN)
    pokemon1.supported_genders.append(Genders.MALE)
    pokemon1.categories.append(Categories.PLANT)
    pokemon1.evolves_to.append(Evolution(name="Ivysaur"))
    
    # Verify pokemon2's lists are unaffected
    assert pokemon2.colors == []
    assert pokemon2.supported_genders == []
    assert pokemon2.categories == []
    assert pokemon2.evolves_to == [] 