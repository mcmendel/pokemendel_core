"""
Tests for the Categories class.
"""
import pytest
from pokemendel_core.utils.definitions.categories import Categories


def test_categories_constants():
    """Test that Categories class has all the required category constants."""
    expected_categories = {
        "PREHISTORIC": "Prehistoric",
        "WING": "Wing",
        "PLANT": "Plant",
        "BIRD": "Bird",
        "BUG": "Bug",
        "MAMMAL": "Mammal",
        "RODENT": "Rodent",
        "REPTILE": "Reptile",
        "CRAB": "Crab",
        "ITEM": "Item",
        "WATERMON": "Watermon",
        "FANTASY": "Fantasy",
        "FOOD": "Food",
        "CATTLE": "Cattle",
        "DOG": "Dog",
        "CAT": "Cat",
        "FISH": "Fish",
        "MOUSE": "Mouse",
        "BUNNY": "Bunny",
        "SLOTH": "Sloth",
        "HORSE": "Horse",
        "HUMAN": "Human",
        "APE": "Ape",
        "DUCK": "Duck",
        "SNAKE": "Snake",
        "BEAR": "Bear",
        "TURTLE": "Turtle",
        "WEAPON": "Weapon",
        "DRAGON": "Dragon",
        "FROG": "Frog",
        "COW": "Cow",
        "PIG": "Pig"
    }
    
    # Test individual category constants
    for category_name, expected_value in expected_categories.items():
        actual_value = getattr(Categories, category_name)
        assert actual_value == expected_value, f"Wrong value for {category_name}: expected {expected_value}, got {actual_value}"


def test_categories_immutability():
    """Test that Categories constants cannot be modified."""
    with pytest.raises(AttributeError):
        Categories.BIRD = "Changed"


def test_categories_list_all_order():
    """Test that list_all returns categories in a consistent order."""
    first_call = Categories.list_all()
    second_call = Categories.list_all()
    assert first_call == second_call


def test_categories_completeness():
    """Test that all categories are present."""
    all_categories = Categories.list_all()
    assert len(all_categories) == 32  # We should have exactly 32 categories


def test_categories_case_consistency():
    """Test that category names follow proper capitalization."""
    for category in Categories.list_all():
        assert category.istitle(), f"Category name '{category}' should be properly capitalized"


def test_categories_uniqueness():
    """Test that all categories are unique."""
    categories = Categories.list_all()
    assert len(categories) == len(set(categories)), "Duplicate categories found"


def test_categories_values():
    """Test that category values match their names in proper case."""
    for name in dir(Categories):
        if not name.startswith('_') and not callable(getattr(Categories, name)):
            value = getattr(Categories, name)
            expected = name.capitalize()
            assert value == expected, f"Category {name} should have value {expected}, got {value}" 