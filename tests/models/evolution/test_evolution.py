"""Tests for the evolution module."""

import pytest
from pokemendel_core.models.evolution import Evolution, EvolutionType, Item


def test_evolution_creation_with_defaults():
    """Test creating an Evolution instance with minimal parameters."""
    evolution = Evolution(name="Charmeleon")
    assert evolution.name == "Charmeleon"
    assert evolution.evolution_type == EvolutionType.LEVEL
    assert evolution.level is None
    assert not evolution.should_hold
    assert evolution.item is None
    assert evolution.special_information is None


def test_evolution_level_based():
    """Test creating a level-based evolution."""
    evolution = Evolution(
        name="Charmeleon",
        level=16
    )
    assert evolution.name == "Charmeleon"
    assert evolution.evolution_type == EvolutionType.LEVEL
    assert evolution.level == 16
    assert not evolution.should_hold
    assert evolution.item is None


def test_evolution_stone_based():
    """Test creating a stone-based evolution."""
    evolution = Evolution(
        name="Vaporeon",
        evolution_type=EvolutionType.STONE,
        item=Item.WATER_STONE
    )
    assert evolution.name == "Vaporeon"
    assert evolution.evolution_type == EvolutionType.STONE
    assert evolution.item == Item.WATER_STONE
    assert not evolution.should_hold
    assert evolution.level is None


def test_evolution_trade_with_item():
    """Test creating a trade evolution that requires holding an item."""
    evolution = Evolution(
        name="Scizor",
        evolution_type=EvolutionType.TRADE,
        should_hold=True,
        item=Item.METAL_COAT
    )
    assert evolution.name == "Scizor"
    assert evolution.evolution_type == EvolutionType.TRADE
    assert evolution.should_hold
    assert evolution.item == Item.METAL_COAT
    assert evolution.level is None


def test_evolution_with_special_info():
    """Test creating an evolution with special information."""
    evolution = Evolution(
        name="Shedinja",
        level=20,
        special_information="Must have empty slot in party and a Pokeball in bag"
    )
    assert evolution.name == "Shedinja"
    assert evolution.evolution_type == EvolutionType.LEVEL
    assert evolution.level == 20
    assert evolution.special_information == "Must have empty slot in party and a Pokeball in bag"


def test_evolution_friendship():
    """Test creating a friendship-based evolution."""
    evolution = Evolution(
        name="Espeon",
        evolution_type=EvolutionType.FRIENDSHIP,
        special_information="Must level up during the day with high friendship"
    )
    assert evolution.name == "Espeon"
    assert evolution.evolution_type == EvolutionType.FRIENDSHIP
    assert evolution.special_information == "Must level up during the day with high friendship"


def test_evolution_time():
    """Test creating a time-based evolution."""
    evolution = Evolution(
        name="Umbreon",
        evolution_type=EvolutionType.TIME,
        special_information="Must level up at night with high friendship"
    )
    assert evolution.name == "Umbreon"
    assert evolution.evolution_type == EvolutionType.TIME
    assert evolution.special_information == "Must level up at night with high friendship"


def test_evolution_equality():
    """Test that two evolutions with the same attributes are equal."""
    evolution1 = Evolution(
        name="Charmeleon",
        level=16
    )
    evolution2 = Evolution(
        name="Charmeleon",
        level=16
    )
    assert evolution1 == evolution2


def test_evolution_repr():
    """Test the string representation of an Evolution instance."""
    evolution = Evolution(
        name="Charmeleon",
        level=16
    )
    repr_str = repr(evolution)
    assert "Evolution" in repr_str
    assert "name='Charmeleon'" in repr_str
    assert "evolution_type=<EvolutionType.LEVEL" in repr_str
    assert "level=16" in repr_str 