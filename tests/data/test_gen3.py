"""Tests for Generation 3 Pokemon data."""

from pokemendel_core.data.gen3 import PokemonGen3, NAME_TO_POKEMON
from pokemendel_core.utils.definitions.types import Types
from pokemendel_core.utils.definitions.genders import Genders
from pokemendel_core.models.evolution.evolution_type import EvolutionType


def test_pokemon_count():
    """Test that there are exactly 386 Pokemon (Gen 1 + Gen 2 + Gen 3)."""
    assert len(NAME_TO_POKEMON) == 386, "There should be exactly 386 Pokemon instances"


def test_name_to_pokemon_keys():
    """Test that each Pokemon's name matches its key in NAME_TO_POKEMON."""
    for key, pokemon in NAME_TO_POKEMON.items():
        assert key == pokemon.name, f"Pokemon with key '{key}' has mismatched name '{pokemon.name}'"


def test_pokemon_name_formatting():
    """Test that Pokemon names are properly formatted."""
    special_cases = {"Ho-oh", "Porygon2"}

    for name in NAME_TO_POKEMON:
        assert name[0].isupper(), f"Pokemon name '{name}' should start with a capital letter"

        if name in special_cases:
            continue

        parts = name.replace('-', ' ').split()
        for part in parts:
            assert part[0].isupper(), f"Each word in '{name}' should start with a capital letter"
            if len(part) > 1 and part not in ("Mr.",):
                assert part[1:].islower(), f"Rest of word '{part}' in '{name}' should be lowercase"


def test_special_pokemon_names():
    """Test special Pokemon names present in Gen 3 data."""
    assert PokemonGen3.FARFETCHD == "Farfetch'd"
    assert PokemonGen3.MR_MIME == "Mr. Mime"
    assert PokemonGen3.NIDORAN_F == "Nidoran-F"
    assert PokemonGen3.NIDORAN_M == "Nidoran-M"
    assert PokemonGen3.HO_OH == "Ho-oh"
    assert PokemonGen3.PORYGON2 == "Porygon2"


def test_starter_pokemon():
    """Test Gen 3 starter Pokemon and their evolution chains."""
    starters = {
        PokemonGen3.TREECKO: [PokemonGen3.GROVYLE, PokemonGen3.SCEPTILE],
        PokemonGen3.TORCHIC: [PokemonGen3.COMBUSKEN, PokemonGen3.BLAZIKEN],
        PokemonGen3.MUDKIP: [PokemonGen3.MARSHTOMP, PokemonGen3.SWAMPERT],
    }

    for starter, evolutions in starters.items():
        pokemon = NAME_TO_POKEMON[starter]
        assert pokemon.gen == 3, f"{starter} should be Gen 3"
        assert len(pokemon.evolves_to) == 1, f"{starter} should have one evolution"
        assert pokemon.evolves_to[0].name == evolutions[0]

        mid = NAME_TO_POKEMON[evolutions[0]]
        assert mid.gen == 3, f"{evolutions[0]} should be Gen 3"
        assert len(mid.evolves_to) == 1
        assert mid.evolves_to[0].name == evolutions[1]

        final = NAME_TO_POKEMON[evolutions[1]]
        assert final.gen == 3
        assert not final.evolves_to, f"{evolutions[1]} should not evolve further"


def test_starter_types():
    """Test Gen 3 starter type assignments."""
    assert NAME_TO_POKEMON[PokemonGen3.TREECKO].types == [Types.GRASS]
    assert NAME_TO_POKEMON[PokemonGen3.SCEPTILE].types == [Types.GRASS]
    assert NAME_TO_POKEMON[PokemonGen3.TORCHIC].types == [Types.FIRE]
    assert NAME_TO_POKEMON[PokemonGen3.BLAZIKEN].types == [Types.FIRE, Types.FIGHTING]
    assert NAME_TO_POKEMON[PokemonGen3.MUDKIP].types == [Types.WATER]
    assert NAME_TO_POKEMON[PokemonGen3.SWAMPERT].types == [Types.WATER, Types.GROUND]


def test_legendary_pokemon():
    """Test Gen 3 legendary Pokemon."""
    genderless_legendaries = [
        PokemonGen3.REGIROCK,
        PokemonGen3.REGICE,
        PokemonGen3.REGISTEEL,
        PokemonGen3.KYOGRE,
        PokemonGen3.GROUDON,
        PokemonGen3.RAYQUAZA,
        PokemonGen3.JIRACHI,
        PokemonGen3.DEOXYS,
    ]

    for legendary in genderless_legendaries:
        pokemon = NAME_TO_POKEMON[legendary]
        assert pokemon.gen == 3, f"{legendary} should be Gen 3"
        assert not pokemon.evolves_to, f"{legendary} should not evolve"
        assert pokemon.supported_genders == [Genders.GENDERLESS], f"{legendary} should be genderless"

    latias = NAME_TO_POKEMON[PokemonGen3.LATIAS]
    assert latias.gen == 3
    assert not latias.evolves_to
    assert latias.supported_genders == [Genders.FEMALE]

    latios = NAME_TO_POKEMON[PokemonGen3.LATIOS]
    assert latios.gen == 3
    assert not latios.evolves_to
    assert latios.supported_genders == [Genders.MALE]


def test_legendary_types():
    """Test Gen 3 legendary Pokemon types."""
    legendary_types = {
        PokemonGen3.REGIROCK: [Types.ROCK],
        PokemonGen3.REGICE: [Types.ICE],
        PokemonGen3.REGISTEEL: [Types.STEEL],
        PokemonGen3.LATIAS: [Types.DRAGON, Types.PSYCHIC],
        PokemonGen3.LATIOS: [Types.DRAGON, Types.PSYCHIC],
        PokemonGen3.KYOGRE: [Types.WATER],
        PokemonGen3.GROUDON: [Types.GROUND],
        PokemonGen3.RAYQUAZA: [Types.DRAGON, Types.FLYING],
        PokemonGen3.JIRACHI: [Types.STEEL, Types.PSYCHIC],
        PokemonGen3.DEOXYS: [Types.PSYCHIC],
    }

    for name, expected_types in legendary_types.items():
        assert NAME_TO_POKEMON[name].types == expected_types, f"{name} types should be {expected_types}"


def test_baby_pokemon():
    """Test Gen 3 baby Pokemon and their evolutions."""
    babies = {
        PokemonGen3.AZURILL: PokemonGen3.MARILL,
        PokemonGen3.WYNAUT: PokemonGen3.WOBBUFFET,
    }

    for baby, evolution in babies.items():
        pokemon = NAME_TO_POKEMON[baby]
        assert pokemon.gen == 3, f"{baby} should be Gen 3"
        assert len(pokemon.evolves_to) == 1, f"{baby} should have one evolution"
        assert pokemon.evolves_to[0].name == evolution, f"{baby} should evolve to {evolution}"


def test_branching_evolutions():
    """Test Pokemon with branching evolution paths."""
    wurmple = NAME_TO_POKEMON[PokemonGen3.WURMPLE]
    assert len(wurmple.evolves_to) == 2
    evolution_names = {e.name for e in wurmple.evolves_to}
    assert PokemonGen3.SILCOON in evolution_names
    assert PokemonGen3.CASCOON in evolution_names

    silcoon = NAME_TO_POKEMON[PokemonGen3.SILCOON]
    assert len(silcoon.evolves_to) == 1
    assert silcoon.evolves_to[0].name == PokemonGen3.BEAUTIFLY

    cascoon = NAME_TO_POKEMON[PokemonGen3.CASCOON]
    assert len(cascoon.evolves_to) == 1
    assert cascoon.evolves_to[0].name == PokemonGen3.DUSTOX

    nincada = NAME_TO_POKEMON[PokemonGen3.NINCADA]
    evolution_names = {e.name for e in nincada.evolves_to}
    assert PokemonGen3.NINJASK in evolution_names
    assert PokemonGen3.SHEDINJA in evolution_names


def test_pseudo_legendary():
    """Test Gen 3 pseudo-legendary Pokemon evolution chains."""
    bagon = NAME_TO_POKEMON[PokemonGen3.BAGON]
    assert bagon.gen == 3
    assert len(bagon.evolves_to) == 1
    assert bagon.evolves_to[0].name == PokemonGen3.SHELGON

    shelgon = NAME_TO_POKEMON[PokemonGen3.SHELGON]
    assert len(shelgon.evolves_to) == 1
    assert shelgon.evolves_to[0].name == PokemonGen3.SALAMENCE

    salamence = NAME_TO_POKEMON[PokemonGen3.SALAMENCE]
    assert salamence.types == [Types.DRAGON, Types.FLYING]
    assert not salamence.evolves_to

    beldum = NAME_TO_POKEMON[PokemonGen3.BELDUM]
    assert beldum.gen == 3
    assert len(beldum.evolves_to) == 1
    assert beldum.evolves_to[0].name == PokemonGen3.METANG

    metang = NAME_TO_POKEMON[PokemonGen3.METANG]
    assert len(metang.evolves_to) == 1
    assert metang.evolves_to[0].name == PokemonGen3.METAGROSS

    metagross = NAME_TO_POKEMON[PokemonGen3.METAGROSS]
    assert metagross.types == [Types.STEEL, Types.PSYCHIC]
    assert not metagross.evolves_to


def test_pokemon_abilities():
    """Test that all Pokemon have abilities assigned (introduced in Gen 3)."""
    for name, pokemon in NAME_TO_POKEMON.items():
        assert pokemon.supported_abilities is not None, f"{name} should have abilities"
        assert len(pokemon.supported_abilities) > 0, f"{name} should have at least one ability"


def test_pokemon_instances():
    """Test that specific Pokemon instances have correct data."""
    treecko = NAME_TO_POKEMON[PokemonGen3.TREECKO]
    assert treecko.gen == 3
    assert treecko.types == [Types.GRASS]
    assert len(treecko.evolves_to) == 1
    assert treecko.evolves_to[0].name == PokemonGen3.GROVYLE

    kyogre = NAME_TO_POKEMON[PokemonGen3.KYOGRE]
    assert kyogre.gen == 3
    assert kyogre.types == [Types.WATER]
    assert not kyogre.evolves_to
    assert kyogre.supported_genders == [Genders.GENDERLESS]

    rayquaza = NAME_TO_POKEMON[PokemonGen3.RAYQUAZA]
    assert rayquaza.gen == 3
    assert rayquaza.types == [Types.DRAGON, Types.FLYING]
    assert not rayquaza.evolves_to


def test_previous_gen_pokemon_included():
    """Test that previous gen Pokemon are included with gen=3."""
    previous_gen_pokemon = [
        PokemonGen3.BULBASAUR,
        PokemonGen3.PIKACHU,
        PokemonGen3.CHARIZARD,
        PokemonGen3.CHIKORITA,
        PokemonGen3.LUGIA,
    ]

    for name in previous_gen_pokemon:
        assert name in NAME_TO_POKEMON, f"{name} should be in Gen 3 data"
        assert NAME_TO_POKEMON[name].gen == 3, f"{name} should have gen=3 in Gen 3 data"


def test_evolution_updates():
    """Test that evolution data is updated for Gen 3."""
    pichu = NAME_TO_POKEMON[PokemonGen3.PICHU]
    assert any(e.name == PokemonGen3.PIKACHU for e in pichu.evolves_to)

    eevee = NAME_TO_POKEMON[PokemonGen3.EEVEE]
    eeveelution_names = {e.name for e in eevee.evolves_to}
    assert PokemonGen3.VAPOREON in eeveelution_names
    assert PokemonGen3.JOLTEON in eeveelution_names
    assert PokemonGen3.FLAREON in eeveelution_names
    assert PokemonGen3.ESPEON in eeveelution_names
    assert PokemonGen3.UMBREON in eeveelution_names
