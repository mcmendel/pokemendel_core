"""Tests for Generation 4 Pokemon data."""

from pokemendel_core.data.gen4 import PokemonGen4, NAME_TO_POKEMON
from pokemendel_core.utils.definitions.types import Types
from pokemendel_core.utils.definitions.genders import Genders
from pokemendel_core.models.evolution.evolution_type import EvolutionType
from pokemendel_core.models.evolution.items import Item


def test_pokemon_count():
    """Test that there are exactly 502 Pokemon (Gen 1 + Gen 2 + Gen 3 + Gen 4)."""
    assert len(NAME_TO_POKEMON) == 502, "There should be exactly 502 Pokemon instances"


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
            if len(part) > 1 and part not in ("Mr.", "Jr."):
                assert part[1:].islower(), f"Rest of word '{part}' in '{name}' should be lowercase"


def test_special_pokemon_names():
    """Test special Pokemon names specific to Gen 4."""
    assert PokemonGen4.PORYGON_Z == "Porygon-Z"
    assert PokemonGen4.MIME_JR == "Mime Jr."
    assert PokemonGen4.WORMADAM_SANDY == "Wormadam-Sandy"
    assert PokemonGen4.WORMADAM_TRASH == "Wormadam-Trash"
    assert PokemonGen4.WORMADAM_PLANT == "Wormadam-Plant"
    assert PokemonGen4.HEAT_ROTOM == "Heat Rotom"
    assert PokemonGen4.WASH_ROTOM == "Wash Rotom"
    assert PokemonGen4.FROST_ROTOM == "Frost Rotom"
    assert PokemonGen4.FAN_ROTOM == "Fan Rotom"
    assert PokemonGen4.MOW_ROTOM == "Mow Rotom"
    assert PokemonGen4.GIRATINA_ORIGIN == "Giratina Origin Form"
    assert PokemonGen4.SHAYMIN_LAND == "Shaymin Land Form"
    assert PokemonGen4.SHAYMIN_SKY == "Shaymin Sky Form"


def test_starter_pokemon():
    """Test Gen 4 starter Pokemon and their evolution chains."""
    starters = {
        PokemonGen4.TURTWIG: [PokemonGen4.GROTLE, PokemonGen4.TORTERRA],
        PokemonGen4.CHIMCHAR: [PokemonGen4.MONFERNO, PokemonGen4.INFERNAPE],
        PokemonGen4.PIPLUP: [PokemonGen4.PRINPLUP, PokemonGen4.EMPOLEON],
    }

    for starter, evolutions in starters.items():
        pokemon = NAME_TO_POKEMON[starter]
        assert pokemon.gen == 4, f"{starter} should be Gen 4"
        assert len(pokemon.evolves_to) == 1, f"{starter} should have one evolution"
        assert pokemon.evolves_to[0].name == evolutions[0]

        mid = NAME_TO_POKEMON[evolutions[0]]
        assert mid.gen == 4, f"{evolutions[0]} should be Gen 4"
        assert len(mid.evolves_to) == 1
        assert mid.evolves_to[0].name == evolutions[1]

        final = NAME_TO_POKEMON[evolutions[1]]
        assert final.gen == 4
        assert not final.evolves_to, f"{evolutions[1]} should not evolve further"


def test_starter_types():
    """Test Gen 4 starter type assignments."""
    assert NAME_TO_POKEMON[PokemonGen4.TURTWIG].types == [Types.GRASS]
    assert NAME_TO_POKEMON[PokemonGen4.TORTERRA].types == [Types.GRASS, Types.GROUND]
    assert NAME_TO_POKEMON[PokemonGen4.CHIMCHAR].types == [Types.FIRE]
    assert NAME_TO_POKEMON[PokemonGen4.INFERNAPE].types == [Types.FIRE, Types.FIGHTING]
    assert NAME_TO_POKEMON[PokemonGen4.PIPLUP].types == [Types.WATER]
    assert NAME_TO_POKEMON[PokemonGen4.EMPOLEON].types == [Types.WATER, Types.STEEL]


def test_legendary_pokemon():
    """Test Gen 4 legendary Pokemon."""
    genderless_legendaries = [
        PokemonGen4.UXIE,
        PokemonGen4.MESPRIT,
        PokemonGen4.AZELF,
        PokemonGen4.DIALGA,
        PokemonGen4.PALKIA,
        PokemonGen4.HEATRAN,
        PokemonGen4.REGIGIGAS,
        PokemonGen4.GIRATINA,
        PokemonGen4.GIRATINA_ORIGIN,
        PokemonGen4.PHIONE,
        PokemonGen4.MANAPHY,
        PokemonGen4.DARKRAI,
        PokemonGen4.SHAYMIN_LAND,
        PokemonGen4.SHAYMIN_SKY,
        PokemonGen4.ARCEUS,
    ]

    for legendary in genderless_legendaries:
        pokemon = NAME_TO_POKEMON[legendary]
        assert pokemon.gen == 4, f"{legendary} should be Gen 4"
        assert not pokemon.evolves_to, f"{legendary} should not evolve"
        assert pokemon.supported_genders == [Genders.GENDERLESS], f"{legendary} should be genderless"

    cresselia = NAME_TO_POKEMON[PokemonGen4.CRESSELIA]
    assert cresselia.gen == 4
    assert not cresselia.evolves_to
    assert cresselia.supported_genders == [Genders.FEMALE]


def test_legendary_types():
    """Test Gen 4 legendary Pokemon types."""
    legendary_types = {
        PokemonGen4.UXIE: [Types.PSYCHIC],
        PokemonGen4.MESPRIT: [Types.PSYCHIC],
        PokemonGen4.AZELF: [Types.PSYCHIC],
        PokemonGen4.DIALGA: [Types.STEEL, Types.DRAGON],
        PokemonGen4.PALKIA: [Types.WATER, Types.DRAGON],
        PokemonGen4.HEATRAN: [Types.FIRE, Types.STEEL],
        PokemonGen4.REGIGIGAS: [Types.NORMAL],
        PokemonGen4.GIRATINA: [Types.GHOST, Types.DRAGON],
        PokemonGen4.GIRATINA_ORIGIN: [Types.GHOST, Types.DRAGON],
        PokemonGen4.CRESSELIA: [Types.PSYCHIC],
        PokemonGen4.PHIONE: [Types.WATER],
        PokemonGen4.MANAPHY: [Types.WATER],
        PokemonGen4.DARKRAI: [Types.DARK],
        PokemonGen4.SHAYMIN_LAND: [Types.GRASS],
        PokemonGen4.SHAYMIN_SKY: [Types.GRASS, Types.FLYING],
        PokemonGen4.ARCEUS: [Types.NORMAL],
    }

    for name, expected_types in legendary_types.items():
        assert NAME_TO_POKEMON[name].types == expected_types, f"{name} types should be {expected_types}"


def test_baby_pokemon():
    """Test Gen 4 baby Pokemon and their evolutions."""
    babies = {
        PokemonGen4.BUDEW: PokemonGen4.ROSELIA,
        PokemonGen4.BONSLY: PokemonGen4.SUDOWOODO,
        PokemonGen4.MIME_JR: PokemonGen4.MR_MIME,
        PokemonGen4.HAPPINY: PokemonGen4.CHANSEY,
        PokemonGen4.MUNCHLAX: PokemonGen4.SNORLAX,
        PokemonGen4.MANTYKE: PokemonGen4.MANTINE,
        PokemonGen4.CHINGLING: PokemonGen4.CHIMECHO,
        PokemonGen4.RIOLU: PokemonGen4.LUCARIO,
    }

    for baby, evolution in babies.items():
        pokemon = NAME_TO_POKEMON[baby]
        assert pokemon.gen == 4, f"{baby} should be Gen 4"
        assert len(pokemon.evolves_to) == 1, f"{baby} should have one evolution"
        assert pokemon.evolves_to[0].name == evolution, f"{baby} should evolve to {evolution}"


def test_eevee_evolutions():
    """Test that Eevee has Leafeon and Glaceon as new Gen 4 evolutions."""
    eevee = NAME_TO_POKEMON[PokemonGen4.EEVEE]
    eeveelution_names = {e.name for e in eevee.evolves_to}
    assert PokemonGen4.VAPOREON in eeveelution_names
    assert PokemonGen4.JOLTEON in eeveelution_names
    assert PokemonGen4.FLAREON in eeveelution_names
    assert PokemonGen4.ESPEON in eeveelution_names
    assert PokemonGen4.UMBREON in eeveelution_names
    assert PokemonGen4.LEAFEON in eeveelution_names
    assert PokemonGen4.GLACEON in eeveelution_names
    assert len(eevee.evolves_to) == 7


def test_new_evolutions_of_old_pokemon():
    """Test new evolutions of older gen Pokemon introduced in Gen 4."""
    new_evolutions = {
        PokemonGen4.MAGNETON: PokemonGen4.MAGNEZONE,
        PokemonGen4.LICKITUNG: PokemonGen4.LICKILICKY,
        PokemonGen4.RHYDON: PokemonGen4.RHYPERIOR,
        PokemonGen4.TANGELA: PokemonGen4.TANGROWTH,
        PokemonGen4.ELECTABUZZ: PokemonGen4.ELECTIVIRE,
        PokemonGen4.MAGMAR: PokemonGen4.MAGMORTAR,
        PokemonGen4.YANMA: PokemonGen4.YANMEGA,
        PokemonGen4.GLIGAR: PokemonGen4.GLISCOR,
        PokemonGen4.PILOSWINE: PokemonGen4.MAMOSWINE,
        PokemonGen4.MURKROW: PokemonGen4.HONCHKROW,
        PokemonGen4.MISDREAVUS: PokemonGen4.MISMAGIUS,
        PokemonGen4.SNEASEL: PokemonGen4.WEAVILE,
        PokemonGen4.AIPOM: PokemonGen4.AMBIPOM,
        PokemonGen4.ROSELIA: PokemonGen4.ROSERADE,
        PokemonGen4.NOSEPASS: PokemonGen4.PROBOPASS,
        PokemonGen4.DUSCLOPS: PokemonGen4.DUSKNOIR,
    }

    for base, evolution in new_evolutions.items():
        pokemon = NAME_TO_POKEMON[base]
        evolution_names = {e.name for e in pokemon.evolves_to}
        assert evolution in evolution_names, f"{base} should be able to evolve into {evolution}"
        assert NAME_TO_POKEMON[evolution].gen == 4, f"{evolution} should be Gen 4"


def test_porygon_evolution_chain():
    """Test the full Porygon evolution chain through Gen 4."""
    porygon = NAME_TO_POKEMON[PokemonGen4.PORYGON]
    porygon2_evo = next(e for e in porygon.evolves_to if e.name == PokemonGen4.PORYGON2)
    assert porygon2_evo.evolution_type == EvolutionType.TRADE

    porygon2 = NAME_TO_POKEMON[PokemonGen4.PORYGON2]
    porygon_z_evo = next(e for e in porygon2.evolves_to if e.name == PokemonGen4.PORYGON_Z)
    assert porygon_z_evo.evolution_type == EvolutionType.TRADE
    assert porygon_z_evo.item == Item.DUBIOUS_DISC


def test_wormadam_forms():
    """Test Wormadam's three forms via Burmy evolution."""
    burmy = NAME_TO_POKEMON[PokemonGen4.BURMY]
    evolution_names = {e.name for e in burmy.evolves_to}
    assert PokemonGen4.WORMADAM_SANDY in evolution_names
    assert PokemonGen4.WORMADAM_TRASH in evolution_names
    assert PokemonGen4.WORMADAM_PLANT in evolution_names
    assert PokemonGen4.MOTHIM in evolution_names

    sandy = NAME_TO_POKEMON[PokemonGen4.WORMADAM_SANDY]
    assert sandy.types == [Types.BUG, Types.GROUND]
    assert sandy.supported_genders == [Genders.FEMALE]

    trash = NAME_TO_POKEMON[PokemonGen4.WORMADAM_TRASH]
    assert trash.types == [Types.BUG, Types.STEEL]
    assert trash.supported_genders == [Genders.FEMALE]

    plant = NAME_TO_POKEMON[PokemonGen4.WORMADAM_PLANT]
    assert plant.types == [Types.BUG, Types.GRASS]
    assert plant.supported_genders == [Genders.FEMALE]


def test_rotom_forms():
    """Test all Rotom forms."""
    rotom_forms = {
        PokemonGen4.ROTOM: [Types.ELECTRIC, Types.GHOST],
        PokemonGen4.HEAT_ROTOM: [Types.ELECTRIC, Types.FIRE],
        PokemonGen4.WASH_ROTOM: [Types.ELECTRIC, Types.WATER],
        PokemonGen4.FROST_ROTOM: [Types.ELECTRIC, Types.ICE],
        PokemonGen4.FAN_ROTOM: [Types.ELECTRIC, Types.FLYING],
        PokemonGen4.MOW_ROTOM: [Types.ELECTRIC, Types.GRASS],
    }

    for name, expected_types in rotom_forms.items():
        pokemon = NAME_TO_POKEMON[name]
        assert pokemon.gen == 4
        assert pokemon.types == expected_types, f"{name} types should be {expected_types}"
        assert pokemon.supported_genders == [Genders.GENDERLESS]
        assert not pokemon.evolves_to


def test_pseudo_legendary():
    """Test Gen 4 pseudo-legendary Pokemon (Garchomp family)."""
    gible = NAME_TO_POKEMON[PokemonGen4.GIBLE]
    assert gible.gen == 4
    assert len(gible.evolves_to) == 1
    assert gible.evolves_to[0].name == PokemonGen4.GABITE

    gabite = NAME_TO_POKEMON[PokemonGen4.GABITE]
    assert len(gabite.evolves_to) == 1
    assert gabite.evolves_to[0].name == PokemonGen4.GARCHOMP

    garchomp = NAME_TO_POKEMON[PokemonGen4.GARCHOMP]
    assert not garchomp.evolves_to


def test_pokemon_instances():
    """Test that specific Pokemon instances have correct data."""
    dialga = NAME_TO_POKEMON[PokemonGen4.DIALGA]
    assert dialga.gen == 4
    assert dialga.types == [Types.STEEL, Types.DRAGON]
    assert not dialga.evolves_to
    assert dialga.supported_genders == [Genders.GENDERLESS]

    lucario = NAME_TO_POKEMON[PokemonGen4.LUCARIO]
    assert lucario.gen == 4
    assert Types.FIGHTING in lucario.types
    assert not lucario.evolves_to

    darkrai = NAME_TO_POKEMON[PokemonGen4.DARKRAI]
    assert darkrai.types == [Types.DARK]
    assert darkrai.supported_genders == [Genders.GENDERLESS]


def test_previous_gen_pokemon_included():
    """Test that previous gen Pokemon are included with gen=4."""
    previous_gen_pokemon = [
        PokemonGen4.BULBASAUR,
        PokemonGen4.PIKACHU,
        PokemonGen4.CHIKORITA,
        PokemonGen4.TREECKO,
        PokemonGen4.RAYQUAZA,
    ]

    for name in previous_gen_pokemon:
        assert name in NAME_TO_POKEMON, f"{name} should be in Gen 4 data"
        assert NAME_TO_POKEMON[name].gen == 4, f"{name} should have gen=4 in Gen 4 data"


def test_gallade_branching():
    """Test that Kirlia can evolve into both Gardevoir and Gallade."""
    kirlia = NAME_TO_POKEMON[PokemonGen4.KIRLIA]
    evolution_names = {e.name for e in kirlia.evolves_to}
    assert PokemonGen4.GARDEVOIR in evolution_names
    assert PokemonGen4.GALLADE in evolution_names


def test_snorunt_branching():
    """Test that Snorunt can evolve into both Glalie and Froslass."""
    snorunt = NAME_TO_POKEMON[PokemonGen4.SNORUNT]
    evolution_names = {e.name for e in snorunt.evolves_to}
    assert PokemonGen4.GLALIE in evolution_names
    assert PokemonGen4.FROSLASS in evolution_names
