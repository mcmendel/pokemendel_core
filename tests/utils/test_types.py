"""
Tests for the Types class.
"""
import pytest
from pokemendel_core.utils.definitions.types import Types


def test_types_constants():
    """Test that Types class has the correct type constants."""
    expected_types = {
        "Normal", "Fire", "Water", "Electric", "Grass", "Ice",
        "Fighting", "Poison", "Ground", "Flying", "Psychic",
        "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"
    }
    
    # Test individual type constants
    assert Types.NORMAL == "Normal"
    assert Types.FIRE == "Fire"
    assert Types.WATER == "Water"
    assert Types.ELECTRIC == "Electric"
    assert Types.GRASS == "Grass"
    assert Types.ICE == "Ice"
    assert Types.FIGHTING == "Fighting"
    assert Types.POISON == "Poison"
    assert Types.GROUND == "Ground"
    assert Types.FLYING == "Flying"
    assert Types.PSYCHIC == "Psychic"
    assert Types.BUG == "Bug"
    assert Types.ROCK == "Rock"
    assert Types.GHOST == "Ghost"
    assert Types.DRAGON == "Dragon"
    assert Types.DARK == "Dark"
    assert Types.STEEL == "Steel"
    assert Types.FAIRY == "Fairy"
    
    # Test that list_all contains all expected types
    assert set(Types.list_all()) == expected_types


def test_types_immutability():
    """Test that Types constants cannot be modified."""
    with pytest.raises(AttributeError):
        Types.NORMAL = "Changed"


def test_types_list_all_order():
    """Test that list_all returns types in a consistent order."""
    first_call = Types.list_all()
    second_call = Types.list_all()
    assert first_call == second_call


def test_types_completeness():
    """Test that all Pokemon types are present."""
    all_types = Types.list_all()
    assert len(all_types) == 18  # There should be exactly 18 Pokemon types 