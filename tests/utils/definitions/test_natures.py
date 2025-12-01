"""
Tests for Pokemon natures functionality.
"""
import pytest
from pokemendel_core.utils.definitions.natures import (
    Natures,
    InvalidNatureError,
    get_nature_effects,
    from_str,
    get_neutral_natures,
    get_attack_natures,
    get_defense_natures,
    get_speed_natures,
    get_sp_atk_natures,
    get_sp_def_natures,
)


def test_all_natures_present():
    """Test that all 25 natures are defined."""
    all_natures = Natures.list_all()
    assert len(all_natures) == 25
    
    # Check that all expected natures exist
    expected_natures = {
        # Neutral natures
        'Hardy', 'Docile', 'Serious', 'Bashful', 'Quirky',
        # Attack-increasing natures
        'Lonely', 'Brave', 'Adamant', 'Naughty',
        # Defense-increasing natures
        'Bold', 'Relaxed', 'Impish', 'Lax',
        # Speed-increasing natures
        'Timid', 'Hasty', 'Jolly', 'Naive',
        # Special Attack-increasing natures
        'Modest', 'Mild', 'Quiet', 'Rash',
        # Special Defense-increasing natures
        'Calm', 'Gentle', 'Sassy', 'Careful',
    }
    
    actual_natures = set(all_natures)
    assert actual_natures == expected_natures


def test_neutral_natures():
    """Test neutral natures have no stat effects."""
    neutral_natures = get_neutral_natures()
    
    for nature in neutral_natures:
        increased, decreased = get_nature_effects(nature)
        assert increased is None
        assert decreased is None


def test_attack_natures():
    """Test Attack-increasing natures."""
    attack_natures = get_attack_natures()
    expected_attack_natures = [
        Natures.LONELY,
        Natures.BRAVE,
        Natures.ADAMANT,
        Natures.NAUGHTY,
    ]
    
    assert set(attack_natures) == set(expected_attack_natures)
    
    # Test specific effects
    assert get_nature_effects(Natures.LONELY) == ("Attack", "Defense")
    assert get_nature_effects(Natures.BRAVE) == ("Attack", "Speed")
    assert get_nature_effects(Natures.ADAMANT) == ("Attack", "Sp.Atk")
    assert get_nature_effects(Natures.NAUGHTY) == ("Attack", "Sp.Def")


def test_defense_natures():
    """Test Defense-increasing natures."""
    defense_natures = get_defense_natures()
    expected_defense_natures = [
        Natures.BOLD,
        Natures.RELAXED,
        Natures.IMPISH,
        Natures.LAX,
    ]
    
    assert set(defense_natures) == set(expected_defense_natures)
    
    # Test specific effects
    assert get_nature_effects(Natures.BOLD) == ("Defense", "Attack")
    assert get_nature_effects(Natures.RELAXED) == ("Defense", "Speed")
    assert get_nature_effects(Natures.IMPISH) == ("Defense", "Sp.Atk")
    assert get_nature_effects(Natures.LAX) == ("Defense", "Sp.Def")


def test_speed_natures():
    """Test Speed-increasing natures."""
    speed_natures = get_speed_natures()
    expected_speed_natures = [
        Natures.TIMID,
        Natures.HASTY,
        Natures.JOLLY,
        Natures.NAIVE,
    ]
    
    assert set(speed_natures) == set(expected_speed_natures)
    
    # Test specific effects
    assert get_nature_effects(Natures.TIMID) == ("Speed", "Attack")
    assert get_nature_effects(Natures.HASTY) == ("Speed", "Defense")
    assert get_nature_effects(Natures.JOLLY) == ("Speed", "Sp.Atk")
    assert get_nature_effects(Natures.NAIVE) == ("Speed", "Sp.Def")


def test_sp_atk_natures():
    """Test Special Attack-increasing natures."""
    sp_atk_natures = get_sp_atk_natures()
    expected_sp_atk_natures = [
        Natures.MODEST,
        Natures.MILD,
        Natures.QUIET,
        Natures.RASH,
    ]
    
    assert set(sp_atk_natures) == set(expected_sp_atk_natures)
    
    # Test specific effects
    assert get_nature_effects(Natures.MODEST) == ("Sp.Atk", "Attack")
    assert get_nature_effects(Natures.MILD) == ("Sp.Atk", "Defense")
    assert get_nature_effects(Natures.QUIET) == ("Sp.Atk", "Speed")
    assert get_nature_effects(Natures.RASH) == ("Sp.Atk", "Sp.Def")


def test_sp_def_natures():
    """Test Special Defense-increasing natures."""
    sp_def_natures = get_sp_def_natures()
    expected_sp_def_natures = [
        Natures.CALM,
        Natures.GENTLE,
        Natures.SASSY,
        Natures.CAREFUL,
    ]
    
    assert set(sp_def_natures) == set(expected_sp_def_natures)
    
    # Test specific effects
    assert get_nature_effects(Natures.CALM) == ("Sp.Def", "Attack")
    assert get_nature_effects(Natures.GENTLE) == ("Sp.Def", "Defense")
    assert get_nature_effects(Natures.SASSY) == ("Sp.Def", "Speed")
    assert get_nature_effects(Natures.CAREFUL) == ("Sp.Def", "Sp.Atk")


def test_from_str_valid():
    """Test converting valid strings to natures."""
    test_cases = [
        ("Hardy", "Hardy"),
        ("Adamant", "Adamant"),
        ("Timid", "Timid"),
        ("Modest", "Modest"),
        ("Calm", "Calm"),
    ]
    
    for nature_str, expected_nature in test_cases:
        result = from_str(nature_str)
        assert result == expected_nature


def test_from_str_invalid():
    """Test that invalid strings raise InvalidNatureError."""
    invalid_inputs = [
        "InvalidNature",
        "adamant",  # lowercase
        "ADAMANT",  # uppercase
        "Adamant ",  # trailing space
        " Adamant",  # leading space
        "",
        None,
        123,
        [],
        {},
    ]
    
    for invalid_input in invalid_inputs:
        with pytest.raises(InvalidNatureError):
            from_str(invalid_input)


def test_from_str_error_message():
    """Test that InvalidNatureError provides helpful error messages."""
    with pytest.raises(InvalidNatureError) as exc_info:
        from_str("InvalidNature")
    
    error_message = str(exc_info.value)
    assert "Invalid nature 'InvalidNature'" in error_message
    assert "Valid natures:" in error_message


def test_nature_effects_all_natures():
    """Test that all natures have defined effects."""
    for nature in Natures.list_all():
        increased, decreased = get_nature_effects(nature)
        
        # Neutral natures should have None for both
        if nature in get_neutral_natures():
            assert increased is None
            assert decreased is None
        else:
            # Non-neutral natures should have exactly one increased and one decreased stat
            assert increased is not None
            assert decreased is not None
            assert increased != decreased
            
            # Stats should be valid stat names
            valid_stats = {"Attack", "Defense", "Speed", "Sp.Atk", "Sp.Def"}
            assert increased in valid_stats
            assert decreased in valid_stats


def test_nature_categories_mutually_exclusive():
    """Test that nature categories are mutually exclusive."""
    neutral = set(get_neutral_natures())
    attack = set(get_attack_natures())
    defense = set(get_defense_natures())
    speed = set(get_speed_natures())
    sp_atk = set(get_sp_atk_natures())
    sp_def = set(get_sp_def_natures())
    
    all_categories = [neutral, attack, defense, speed, sp_atk, sp_def]
    
    # Check that no nature appears in multiple categories
    for i, category1 in enumerate(all_categories):
        for j, category2 in enumerate(all_categories):
            if i != j:
                intersection = category1 & category2
                assert len(intersection) == 0, f"Categories {i} and {j} share natures: {intersection}"
    
    # Check that all natures are accounted for
    all_natures = set(Natures.list_all())
    union = neutral | attack | defense | speed | sp_atk | sp_def
    assert union == all_natures 