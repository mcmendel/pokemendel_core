"""Tests for the evolution_type module."""

import pytest
from pokemendel_core.models.evolution import EvolutionType, InvalidEvolutionTypeError


def test_evolution_type_values():
    """Test that all evolution types have the expected string values."""
    assert EvolutionType.STONE.value == "stone"
    assert EvolutionType.MOVE.value == "move"
    assert EvolutionType.TRADE.value == "trade"
    assert EvolutionType.FRIENDSHIP.value == "friendship"
    assert EvolutionType.RANDOM.value == "Random"
    assert EvolutionType.TIME.value == "time"


def test_from_str_valid_cases():
    """Test successful conversion from strings to EvolutionType."""
    # Test with lowercase
    assert EvolutionType.from_str("stone") == EvolutionType.STONE
    assert EvolutionType.from_str("time") == EvolutionType.TIME
    
    # Test with uppercase
    assert EvolutionType.from_str("MOVE") == EvolutionType.MOVE
    assert EvolutionType.from_str("TRADE") == EvolutionType.TRADE
    
    # Test with mixed case
    assert EvolutionType.from_str("FrIeNdShIp") == EvolutionType.FRIENDSHIP
    assert EvolutionType.from_str("RaNdOm") == EvolutionType.RANDOM


def test_from_str_invalid_type():
    """Test that invalid evolution types raise appropriate exceptions."""
    with pytest.raises(InvalidEvolutionTypeError) as exc_info:
        EvolutionType.from_str("invalid_type")
    
    # Verify the error message contains all valid types
    error_msg = str(exc_info.value)
    for evolution_type in EvolutionType:
        assert evolution_type.name.lower() in error_msg


def test_from_str_invalid_input_type():
    """Test that non-string inputs raise TypeError."""
    invalid_inputs = [
        None,
        123,
        1.23,
        [],
        {},
        True
    ]
    
    for invalid_input in invalid_inputs:
        with pytest.raises(TypeError) as exc_info:
            EvolutionType.from_str(invalid_input)
        assert f"must be a string, got {type(invalid_input).__name__}" in str(exc_info.value)


def test_enum_membership():
    """Test that we can check if a value is a valid evolution type."""
    # Test valid enum members
    assert EvolutionType.STONE in EvolutionType
    assert EvolutionType.TIME in EvolutionType
    
    # Test that non-members are handled appropriately
    class FakeEnum:
        def __init__(self, value):
            self.value = value
    
    fake_evolution = FakeEnum("stone")
    
    # In Python 3.11, this raises TypeError
    # In Python 3.12+, this returns False
    try:
        result = fake_evolution in EvolutionType
        assert not result  # Python 3.12+
    except TypeError:  # Python 3.11
        pass  # This is also acceptable 