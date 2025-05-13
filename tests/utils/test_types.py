"""
Tests for the Types class.
"""
import pytest
from pokemendel_core.utils.definitions.types import Types, get_generation_types


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


def test_generation_types_validation():
    """Test that get_generation_types validates generation number."""
    with pytest.raises(ValueError, match="Generation must be between 1 and 9"):
        get_generation_types(0)
    with pytest.raises(ValueError, match="Generation must be between 1 and 9"):
        get_generation_types(10)


def test_generation_one_types():
    """Test that generation 1 returns correct types."""
    gen1_types = get_generation_types(1)
    expected_types = [
        "Normal", "Fire", "Water", "Electric", "Grass", "Ice",
        "Fighting", "Poison", "Ground", "Flying", "Psychic",
        "Bug", "Rock", "Ghost", "Dragon"
    ]
    assert sorted(gen1_types) == sorted(expected_types)
    assert len(gen1_types) == 15


def test_generation_two_types():
    """Test that generation 2 includes both gen 1 and 2 types."""
    gen2_types = get_generation_types(2)
    expected_new_types = ["Dark", "Steel"]
    
    # Should include all gen 1 types
    assert all(type in gen2_types for type in get_generation_types(1))
    # Should include new gen 2 types
    assert all(type in gen2_types for type in expected_new_types)
    assert len(gen2_types) == 17  # 15 (gen1) + 2 (gen2)


def test_generation_six_types():
    """Test that generation 6 includes all types up to Fairy."""
    gen6_types = get_generation_types(6)
    assert "Fairy" in gen6_types
    assert len(gen6_types) == 18  # All types should be present


def test_intermediate_generations():
    """Test that generations between type introductions return correct counts."""
    # Gen 3-5 should have same types as gen 2
    for gen in range(3, 6):
        assert get_generation_types(gen) == get_generation_types(2)
    
    # Gen 7-9 should have same types as gen 6
    for gen in range(7, 10):
        assert get_generation_types(gen) == get_generation_types(6) 