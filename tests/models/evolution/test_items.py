"""Tests for the items module."""

import pytest
from pokemendel_core.models.evolution import Item, InvalidItemError


def test_item_values():
    """Test that all items have the expected string values."""
    assert Item.WATER_STONE.value == "Water Stone"
    assert Item.FIRE_STONE.value == "Fire Stone"
    assert Item.LEAF_STONE.value == "Leaf Stone"
    assert Item.THUNDER_STONE.value == "Thunder Stone"
    assert Item.MOON_STONE.value == "Moon Stone"
    assert Item.SUN_STONE.value == "Sun Stone"
    assert Item.KINGS_ROCK.value == "Kings Rock"
    assert Item.METAL_COAT.value == "Metal Coat"
    assert Item.DRAGON_SCALE.value == "Dragon Scale"
    assert Item.UPGRADE.value == "Upgrade"


def test_item_from_str_valid_cases():
    """Test successful conversion from strings to Item."""
    # Test with original format (spaces)
    assert Item.from_str("Water Stone") == Item.WATER_STONE
    assert Item.from_str("Kings Rock") == Item.KINGS_ROCK
    
    # Test with underscore format
    assert Item.from_str("WATER_STONE") == Item.WATER_STONE
    assert Item.from_str("KINGS_ROCK") == Item.KINGS_ROCK
    
    # Test with lowercase and mixed case
    assert Item.from_str("water stone") == Item.WATER_STONE
    assert Item.from_str("WaTeR sToNe") == Item.WATER_STONE
    assert Item.from_str("water_stone") == Item.WATER_STONE


def test_item_from_str_invalid_item():
    """Test that invalid items raise appropriate exceptions."""
    with pytest.raises(InvalidItemError) as exc_info:
        Item.from_str("Invalid Stone")
    
    # Verify the error message contains all valid items
    error_msg = str(exc_info.value)
    for item in Item:
        assert item.value in error_msg


def test_item_from_str_invalid_input_type():
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
            Item.from_str(invalid_input)
        assert f"must be a string, got {type(invalid_input).__name__}" in str(exc_info.value)


def test_item_enum_membership():
    """Test that we can check if a value is a valid item."""
    # Test valid enum members
    assert Item.WATER_STONE in Item
    assert Item.DRAGON_SCALE in Item
    
    # Test that non-members are handled appropriately
    class FakeItem:
        def __init__(self, value):
            self.value = value
    
    fake_item = FakeItem("Water Stone")
    
    # In Python 3.11, this raises TypeError
    # In Python 3.12+, this returns False
    try:
        result = fake_item in Item
        assert not result  # Python 3.12+
    except TypeError:  # Python 3.11
        pass  # This is also acceptable 