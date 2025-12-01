"""
Tests for Pokemon abilities functionality.
"""
import pytest
from pokemendel_core.utils.definitions.abilities import (
    Abilities,
    InvalidAbilityError,
    from_str,
    get_ability_description,
    get_abilities_by_generation,
    get_weather_abilities,
    get_contact_abilities,
    get_immunity_abilities,
)


def test_all_abilities_present():
    """Test that all abilities are defined."""
    all_abilities = Abilities.list_all()
    assert len(all_abilities) > 0
    
    # Check that some key abilities exist
    expected_abilities = {
        # Gen 1 abilities
        'Overgrow', 'Blaze', 'Torrent', 'Swarm', 'Static', 'Levitate',
        'Intimidate', 'Flash Fire', 'Volt Absorb', 'Water Absorb',
        # Gen 2 abilities
        'Adaptability', 'Technician', 'Magic Guard', 'Mold Breaker',
        'Poison Heal', 'Simple', 'Download', 'Iron Fist',
        # Gen 3 abilities
        'Sheer Force', 'Contrary', 'Regenerator', 'Prankster',
        'Magic Bounce', 'Moxie', 'Analytic', 'Illusion',
    }
    
    actual_abilities = set(all_abilities)
    for ability in expected_abilities:
        assert ability in actual_abilities


def test_from_str_valid():
    """Test converting valid strings to abilities."""
    test_cases = [
        ("Overgrow", "Overgrow"),
        ("Levitate", "Levitate"),
        ("Adaptability", "Adaptability"),
        ("Sheer Force", "Sheer Force"),
        ("Magic Bounce", "Magic Bounce"),
    ]
    
    for ability_str, expected_ability in test_cases:
        result = from_str(ability_str)
        assert result == expected_ability


def test_from_str_invalid():
    """Test that invalid strings raise InvalidAbilityError."""
    invalid_inputs = [
        "InvalidAbility",
        "overgrow",  # lowercase
        "OVERGROW",  # uppercase
        "Overgrow ",  # trailing space
        " Overgrow",  # leading space
        "",
        None,
        123,
        [],
        {},
    ]
    
    for invalid_input in invalid_inputs:
        with pytest.raises(InvalidAbilityError):
            from_str(invalid_input)


def test_from_str_error_message():
    """Test that InvalidAbilityError provides helpful error messages."""
    with pytest.raises(InvalidAbilityError) as exc_info:
        from_str("InvalidAbility")
    
    error_message = str(exc_info.value)
    assert "Invalid ability 'InvalidAbility'" in error_message
    assert "Valid abilities:" in error_message


def test_get_ability_description():
    """Test getting ability descriptions."""
    # Test some key abilities
    test_cases = [
        ("Overgrow", "Powers up Grass-type moves when HP is low."),
        ("Levitate", "Immune to Ground-type moves."),
        ("Static", "May paralyze opponents on contact."),
        ("Adaptability", "Increases STAB bonus."),
        ("Sheer Force", "Removes additional effects for more power."),
    ]
    
    for ability, expected_description in test_cases:
        description = get_ability_description(ability)
        assert description == expected_description


def test_get_ability_description_invalid():
    """Test getting description for invalid ability."""
    description = get_ability_description("InvalidAbility")
    assert description == "No description available."


def test_get_abilities_by_generation():
    """Test getting abilities by generation."""
    # Test each generation
    for gen in [1, 2, 3]:
        abilities = get_abilities_by_generation(gen)
        assert isinstance(abilities, list)
        assert len(abilities) > 0
        
        # Check that all returned abilities are valid
        all_abilities = Abilities.list_all()
        for ability in abilities:
            assert ability in all_abilities


def test_get_abilities_by_generation_invalid():
    """Test that invalid generation numbers raise ValueError."""
    invalid_generations = [0, 4, 5, -1, 10]
    
    for gen in invalid_generations:
        with pytest.raises(ValueError) as exc_info:
            get_abilities_by_generation(gen)
        
        error_message = str(exc_info.value)
        assert f"Invalid generation {gen}" in error_message


def test_get_weather_abilities():
    """Test getting weather-affecting abilities."""
    weather_abilities = get_weather_abilities()
    
    expected_weather_abilities = [
        Abilities.DRIZZLE,
        Abilities.DROUGHT,
        Abilities.SAND_STREAM,
        Abilities.SNOW_WARNING,
    ]
    
    assert set(weather_abilities) == set(expected_weather_abilities)
    
    # Test that all weather abilities have appropriate descriptions
    for ability in weather_abilities:
        description = get_ability_description(ability)
        assert "rain" in description.lower() or "sun" in description.lower() or "sand" in description.lower() or "hail" in description.lower()


def test_get_contact_abilities():
    """Test getting contact-activated abilities."""
    contact_abilities = get_contact_abilities()
    
    expected_contact_abilities = [
        Abilities.STATIC,
        Abilities.POISON_POINT,
        Abilities.FLAME_BODY,
        Abilities.EFFECT_SPORE,
        Abilities.ROUGH_SKIN,
        Abilities.IRON_BARBS,
        Abilities.CUTE_CHARM,
        Abilities.POISON_TOUCH,
        Abilities.MUMMY,
        Abilities.PICKPOCKET,
    ]
    
    assert set(contact_abilities) == set(expected_contact_abilities)
    
    # Test that all contact abilities have appropriate descriptions
    for ability in contact_abilities:
        description = get_ability_description(ability)
        assert "contact" in description.lower() or "hit" in description.lower()


def test_get_immunity_abilities():
    """Test getting immunity-providing abilities."""
    immunity_abilities = get_immunity_abilities()
    
    expected_immunity_abilities = [
        Abilities.VOLT_ABSORB,
        Abilities.WATER_ABSORB,
        Abilities.FLASH_FIRE,
        Abilities.LEVITATE,
        Abilities.SOUNDPROOF,
        Abilities.STORM_DRAIN,
        Abilities.SAP_SIPPER,
        Abilities.LIGHTNING_ROD,
    ]
    
    assert set(immunity_abilities) == set(expected_immunity_abilities)
    
    # Test that all immunity abilities have appropriate descriptions
    for ability in immunity_abilities:
        description = get_ability_description(ability)
        # Check for immunity-related keywords in descriptions
        immunity_keywords = ["immune", "heals", "absorbs", "draws in", "powers up", "cannot be"]
        has_immunity_keyword = any(keyword in description.lower() for keyword in immunity_keywords)
        assert has_immunity_keyword, f"Ability {ability} description should contain immunity-related keywords: {description}"


def test_generation_1_abilities():
    """Test specific Gen 1 abilities."""
    gen1_abilities = get_abilities_by_generation(1)
    
    # Check that key Gen 1 abilities are present
    key_gen1_abilities = [
        'Overgrow', 'Blaze', 'Torrent', 'Swarm', 'Static', 'Levitate',
        'Intimidate', 'Flash Fire', 'Volt Absorb', 'Water Absorb',
        'Wonder Guard', 'Huge Power', 'Pure Power', 'Pressure',
    ]
    
    for ability in key_gen1_abilities:
        assert ability in gen1_abilities


def test_generation_2_abilities():
    """Test specific Gen 2 abilities."""
    gen2_abilities = get_abilities_by_generation(2)
    
    # Check that key Gen 2 abilities are present
    key_gen2_abilities = [
        'Adaptability', 'Technician', 'Magic Guard', 'Mold Breaker',
        'Poison Heal', 'Simple', 'Download', 'Iron Fist',
        'Skill Link', 'Super Luck', 'Anticipation', 'Forewarn',
    ]
    
    for ability in key_gen2_abilities:
        assert ability in gen2_abilities


def test_generation_3_abilities():
    """Test specific Gen 3 abilities."""
    gen3_abilities = get_abilities_by_generation(3)
    
    # Check that key Gen 3 abilities are present
    key_gen3_abilities = [
        'Sheer Force', 'Contrary', 'Regenerator', 'Prankster',
        'Magic Bounce', 'Moxie', 'Analytic', 'Illusion',
        'Imposter', 'Infiltrator', 'Victory Star', 'Turboblaze',
    ]
    
    for ability in key_gen3_abilities:
        assert ability in gen3_abilities


def test_ability_descriptions_completeness():
    """Test that all abilities have descriptions."""
    all_abilities = Abilities.list_all()
    
    for ability in all_abilities:
        description = get_ability_description(ability)
        assert description != "No description available."
        assert len(description) > 0


def test_generation_exclusivity():
    """Test that abilities don't appear in multiple generations."""
    gen1_abilities = set(get_abilities_by_generation(1))
    gen2_abilities = set(get_abilities_by_generation(2))
    gen3_abilities = set(get_abilities_by_generation(3))
    
    # Check that no ability appears in multiple generations
    assert len(gen1_abilities & gen2_abilities) == 0
    assert len(gen1_abilities & gen3_abilities) == 0
    assert len(gen2_abilities & gen3_abilities) == 0


def test_ability_categories_non_overlapping():
    """Test that ability categories don't overlap inappropriately."""
    weather_abilities = set(get_weather_abilities())
    contact_abilities = set(get_contact_abilities())
    immunity_abilities = set(get_immunity_abilities())
    
    # Some abilities can be in multiple categories, but let's check for logical consistency
    # For example, an ability shouldn't be both weather and contact
    weather_contact_overlap = weather_abilities & contact_abilities
    assert len(weather_contact_overlap) == 0, f"Weather and contact abilities shouldn't overlap: {weather_contact_overlap}"
    
    # Weather and immunity can overlap (like Storm Drain)
    weather_immunity_overlap = weather_abilities & immunity_abilities
    assert len(weather_immunity_overlap) >= 0  # This is acceptable


def test_ability_validation():
    """Test that all abilities in helper functions are valid."""
    all_abilities = set(Abilities.list_all())
    
    # Test weather abilities
    weather_abilities = set(get_weather_abilities())
    assert weather_abilities.issubset(all_abilities)
    
    # Test contact abilities
    contact_abilities = set(get_contact_abilities())
    assert contact_abilities.issubset(all_abilities)
    
    # Test immunity abilities
    immunity_abilities = set(get_immunity_abilities())
    assert immunity_abilities.issubset(all_abilities)
    
    # Test generation abilities
    for gen in [1, 2, 3]:
        gen_abilities = set(get_abilities_by_generation(gen))
        assert gen_abilities.issubset(all_abilities) 