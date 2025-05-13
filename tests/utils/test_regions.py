"""
Tests for the Regions class.
"""
import pytest
from pokemendel_core.utils.definitions.regions import Regions


def test_regions_constants():
    """Test that Regions class has the correct region constants."""
    expected_regions = {"Kanto", "Johto"}
    
    # Test that list_all contains all expected regions
    assert set(Regions.list_all()) == expected_regions


def test_regions_immutability():
    """Test that Regions constants cannot be modified."""
    with pytest.raises(AttributeError):
        Regions.KANTO = "Changed"


def test_regions_list_all_order():
    """Test that list_all returns regions in a consistent order."""
    first_call = Regions.list_all()
    second_call = Regions.list_all()
    assert first_call == second_call


def test_regions_completeness():
    """Test that all configured regions are present."""
    all_regions = Regions.list_all()
    assert len(all_regions) == 2  # Currently only Kanto and Johto are configured


def test_regions_case_consistency():
    """Test that region names follow proper capitalization."""
    for region in Regions.list_all():
        assert region.istitle(), f"Region name '{region}' should be properly capitalized" 