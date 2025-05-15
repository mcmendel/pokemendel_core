"""Tests for the Categories enum."""

import pytest
from pokemendel_core.utils.definitions.categories import Categories


def test_categories_constants():
    """Test that category constants are defined correctly."""
    assert Categories.BIRD == "Bird"
    assert Categories.DRAGON == "Dragon"
    assert Categories.PLANT == "Plant"


def test_categories_immutability():
    """Test that category values cannot be modified."""
    with pytest.raises(AttributeError):
        Categories.BIRD = "NewBird"


def test_categories_list_all_order():
    """Test that categories are listed in alphabetical order."""
    all_categories = sorted(Categories.list_all())
    assert all_categories == sorted(all_categories)


def test_categories_completeness():
    """Test that all categories are present."""
    all_categories = Categories.list_all()
    assert len(all_categories) == 32  # We should have exactly 34 categories


def test_categories_case_consistency():
    """Test that category names follow consistent casing."""
    for category in Categories.list_all():
        # Category names should be title case
        assert category == category.title()


def test_categories_uniqueness():
    """Test that all category values are unique."""
    all_categories = Categories.list_all()
    assert len(all_categories) == len(set(all_categories))


def test_categories_values():
    """Test that category values match their names."""
    for category in Categories.list_all():
        assert getattr(Categories, category.upper()) == category 