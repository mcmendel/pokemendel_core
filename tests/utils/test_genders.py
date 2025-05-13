"""
Tests for the Genders class.
"""
import pytest
from pokemendel_core.utils.definitions.genders import Genders


def test_genders_constants():
    """Test that Genders class has all the required gender constants."""
    expected_genders = {
        "MALE": "Male",
        "FEMALE": "Female",
        "GENDERLESS": "Genderless"
    }
    
    # Test individual gender constants
    for gender_name, expected_value in expected_genders.items():
        actual_value = getattr(Genders, gender_name)
        assert actual_value == expected_value, f"Wrong value for {gender_name}: expected {expected_value}, got {actual_value}"


def test_genders_immutability():
    """Test that Genders constants cannot be modified."""
    with pytest.raises(AttributeError):
        Genders.MALE = "Changed"


def test_genders_list_all_order():
    """Test that list_all returns genders in a consistent order."""
    first_call = Genders.list_all()
    second_call = Genders.list_all()
    assert first_call == second_call


def test_genders_completeness():
    """Test that all genders are present."""
    all_genders = Genders.list_all()
    assert len(all_genders) == 3  # We should have exactly 3 genders


def test_genders_case_consistency():
    """Test that gender names follow proper capitalization."""
    for gender in Genders.list_all():
        assert gender.istitle(), f"Gender name '{gender}' should be properly capitalized"


def test_genders_uniqueness():
    """Test that all genders are unique."""
    genders = Genders.list_all()
    assert len(genders) == len(set(genders)), "Duplicate genders found"


def test_genders_values():
    """Test that gender values match their names in proper case."""
    for name in dir(Genders):
        if not name.startswith('_') and not callable(getattr(Genders, name)):
            value = getattr(Genders, name)
            expected = name.capitalize()
            assert value == expected, f"Gender {name} should have value {expected}, got {value}" 