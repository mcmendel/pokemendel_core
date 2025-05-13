"""
Tests for the EnumList base class.
"""
import pytest
from pokemendel_core.utils.enum_list import EnumList


def test_enum_list_empty():
    """Test that an empty EnumList subclass returns an empty list."""
    class EmptyEnum(EnumList):
        pass
    
    assert EmptyEnum.list_all() == []


def test_enum_list_with_values():
    """Test that EnumList correctly lists string constants."""
    class TestEnum(EnumList):
        FIRST = "First"
        SECOND = "Second"
        THIRD = "Third"
    
    expected = ["First", "Second", "Third"]
    assert sorted(TestEnum.list_all()) == sorted(expected)


def test_enum_list_ignores_non_strings():
    """Test that EnumList only includes string values."""
    class MixedEnum(EnumList):
        STRING = "String"
        NUMBER = 42
        FLOAT = 3.14
        BOOL = True
        LIST = ["not", "included"]
        
    assert MixedEnum.list_all() == ["String"]


def test_enum_list_ignores_private_attributes():
    """Test that EnumList ignores private attributes."""
    class PrivateEnum(EnumList):
        _PRIVATE = "Private"
        __VERY_PRIVATE = "Very Private"
        PUBLIC = "Public"
        
    assert PrivateEnum.list_all() == ["Public"] 