"""
Tests for the Colors class.
"""
import pytest
from pokemendel_core.utils.definitions.colors import Colors


def test_colors_constants():
    """Test that Colors class has all the required color constants."""
    expected_colors = {
        "RED": "Red",
        "BLUE": "Blue",
        "GREEN": "Green",
        "YELLOW": "Yellow",
        "PURPLE": "Purple",
        "BROWN": "Brown",
        "BLACK": "Black",
        "WHITE": "White",
        "GRAY": "Gray",
        "ORANGE": "Orange",
        "PINK": "Pink"
    }
    
    # Test individual color constants
    for color_name, expected_value in expected_colors.items():
        actual_value = getattr(Colors, color_name)
        assert actual_value == expected_value, f"Wrong value for {color_name}: expected {expected_value}, got {actual_value}"


def test_colors_immutability():
    """Test that Colors constants cannot be modified."""
    with pytest.raises(AttributeError):
        Colors.RED = "Changed"


def test_colors_list_all_order():
    """Test that list_all returns colors in a consistent order."""
    first_call = Colors.list_all()
    second_call = Colors.list_all()
    assert first_call == second_call


def test_colors_completeness():
    """Test that all basic colors are present."""
    all_colors = Colors.list_all()
    assert len(all_colors) == 11  # We should have exactly 11 basic colors


def test_colors_case_consistency():
    """Test that color names follow proper capitalization."""
    for color in Colors.list_all():
        assert color.istitle(), f"Color name '{color}' should be properly capitalized"


def test_colors_uniqueness():
    """Test that all colors are unique."""
    colors = Colors.list_all()
    assert len(colors) == len(set(colors)), "Duplicate colors found" 