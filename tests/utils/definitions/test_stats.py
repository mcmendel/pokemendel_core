"""Tests for the stats module."""

import pytest
from pokemendel_core.utils.definitions.stats import Stats


def test_stats_creation():
    """Test creating a Stats instance with valid values."""
    stats = Stats(
        attack=100,
        defence=80,
        special_attack=120,
        special_defence=90
    )
    assert stats.attack == 100
    assert stats.defence == 80
    assert stats.special_attack == 120
    assert stats.special_defence == 90


def test_stats_equality():
    """Test that two Stats instances with the same values are equal."""
    stats1 = Stats(
        attack=100,
        defence=80,
        special_attack=120,
        special_defence=90
    )
    stats2 = Stats(
        attack=100,
        defence=80,
        special_attack=120,
        special_defence=90
    )
    assert stats1 == stats2


def test_stats_inequality():
    """Test that two Stats instances with different values are not equal."""
    stats1 = Stats(
        attack=100,
        defence=80,
        special_attack=120,
        special_defence=90
    )
    stats2 = Stats(
        attack=90,  # Different attack value
        defence=80,
        special_attack=120,
        special_defence=90
    )
    assert stats1 != stats2


def test_stats_type_validation():
    """Test that stats values must be integers."""
    with pytest.raises(TypeError):
        Stats(
            attack="100",  # String instead of int
            defence=80,
            special_attack=120,
            special_defence=90
        )
    
    with pytest.raises(TypeError):
        Stats(
            attack=100,
            defence=80.5,  # Float instead of int
            special_attack=120,
            special_defence=90
        )


def test_stats_repr():
    """Test the string representation of Stats."""
    stats = Stats(
        attack=100,
        defence=80,
        special_attack=120,
        special_defence=90
    )
    repr_str = repr(stats)
    assert "Stats" in repr_str
    assert "attack=100" in repr_str
    assert "defence=80" in repr_str
    assert "special_attack=120" in repr_str
    assert "special_defence=90" in repr_str


def test_stats_attribute_modification():
    """Test that Stats attributes can be modified after creation."""
    stats = Stats(
        attack=100,
        defence=80,
        special_attack=120,
        special_defence=90
    )
    
    # Modify attributes
    stats.attack = 110
    stats.defence = 85
    stats.special_attack = 125
    stats.special_defence = 95
    
    # Verify modifications
    assert stats.attack == 110
    assert stats.defence == 85
    assert stats.special_attack == 125
    assert stats.special_defence == 95
    
    # Test type validation on modification
    with pytest.raises(TypeError):
        stats.attack = "invalid"  # Should raise TypeError 