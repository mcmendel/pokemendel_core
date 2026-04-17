from ..models.pokemon import Pokemon
from ..models.evolution.evolution import Evolution
from ..models.evolution.evolution_type import EvolutionType
from ..models.evolution.items import Item
from ..utils.definitions.types import Types
from ..utils.definitions.colors import Colors
from ..utils.definitions.categories import Categories
from ..utils.definitions.stats import Stats
from ..utils.definitions.genders import Genders
from ..utils.definitions.abilities import Abilities
from .utils.names import PokemonNames as PokemonGen4
from .utils.evolutions import update_evolution
from .gen3 import NAME_TO_POKEMON as NAME_TO_POKEMON_GEN3
from dataclasses import replace
from copy import deepcopy

NAME_TO_POKEMON = {
    pokemon_name: replace(deepcopy(pokemon), gen=4)
    for pokemon_name, pokemon in NAME_TO_POKEMON_GEN3.items()
}

# Pichu
update_evolution(NAME_TO_POKEMON, PokemonGen4.PICHU, PokemonGen4.PIKACHU, Evolution(name="", level=25, evolution_type=EvolutionType.FRIENDSHIP))
update_evolution(NAME_TO_POKEMON, PokemonGen4.PIKACHU, PokemonGen4.RAICHU, Evolution(name="", evolution_type=EvolutionType.GYM, item=Item.THUNDER_STONE, special_information="Sixth gym"))

# Nidorans
update_evolution(NAME_TO_POKEMON, PokemonGen4.NIDORINA, PokemonGen4.NIDOQUEEN, Evolution(name="", level=23, evolution_type=EvolutionType.STONE, item=Item.MOON_STONE))
update_evolution(NAME_TO_POKEMON, PokemonGen4.NIDORINO, PokemonGen4.NIDOKING, Evolution(name=PokemonGen4.NIDOKING, level=43, evolution_type=EvolutionType.STONE, item=Item.MOON_STONE))

# cleffa
update_evolution(NAME_TO_POKEMON, PokemonGen4.CLEFFA, PokemonGen4.CLEFAIRY, Evolution(name="", level=21, evolution_type=EvolutionType.FRIENDSHIP))
update_evolution(NAME_TO_POKEMON, PokemonGen4.CLEFAIRY, PokemonGen4.CLEFABLE, Evolution(name="", level=43, item=Item.MOON_STONE, evolution_type=EvolutionType.STONE, special_information="Sixth gym"))

# vulpix
update_evolution(NAME_TO_POKEMON, PokemonGen4.VULPIX, PokemonGen4.NINETALES, Evolution(name="", level=44, evolution_type=EvolutionType.STONE, item=Item.FIRE_STONE))

# igglybuff
update_evolution(NAME_TO_POKEMON, PokemonGen4.IGGLYBUFF, PokemonGen4.JIGGLYPUFF, Evolution(name="", level=16, evolution_type=EvolutionType.FRIENDSHIP))
update_evolution(NAME_TO_POKEMON, PokemonGen4.JIGGLYPUFF, PokemonGen4.WIGGLYTUFF, Evolution(name="", level=45, evolution_type=EvolutionType.STONE, item=Item.MOON_STONE))

# zubat
update_evolution(NAME_TO_POKEMON, PokemonGen4.GOLBAT, PokemonGen4.CROBAT, Evolution(name="", evolution_type=EvolutionType.FRIENDSHIP))

# oddish
update_evolution(NAME_TO_POKEMON, PokemonGen4.GLOOM, PokemonGen4.VILEPLUME, Evolution(name="", evolution_type=EvolutionType.STONE, item=Item.LEAF_STONE, special_information="Sixth gym"))
update_evolution(NAME_TO_POKEMON, PokemonGen4.GLOOM, PokemonGen4.BELLOSSOM, Evolution(name="", level=23, evolution_type=EvolutionType.STONE, item=Item.SUN_STONE))

# growlithe
update_evolution(NAME_TO_POKEMON, PokemonGen4.GROWLITHE, PokemonGen4.ARCANINE, Evolution(name="", level=39, evolution_type=EvolutionType.STONE, item=Item.FIRE_STONE))

# poliwag
update_evolution(NAME_TO_POKEMON, PokemonGen4.POLIWHIRL, PokemonGen4.POLIWRATH, Evolution(name="", level=43, evolution_type=EvolutionType.STONE, item=Item.WATER_STONE))
update_evolution(NAME_TO_POKEMON, PokemonGen4.POLIWHIRL, PokemonGen4.POLITOED, Evolution(name="", level=48, evolution_type=EvolutionType.TRADE, should_hold=True, item=Item.KINGS_ROCK),)

# abra
update_evolution(NAME_TO_POKEMON, PokemonGen4.KADABRA, PokemonGen4.ALAKAZAM, Evolution(name="", evolution_type=EvolutionType.TRADE, special_information="Sixth gym"),)

# machop
update_evolution(NAME_TO_POKEMON, PokemonGen4.MACHOKE, PokemonGen4.MACHAMP, Evolution(name="", evolution_type=EvolutionType.TRADE, special_information="Sixth gym"),)

# bellsprout
update_evolution(NAME_TO_POKEMON, PokemonGen4.WEEPINBELL, PokemonGen4.VICTREEBEL, Evolution(name="", level=47, evolution_type=EvolutionType.STONE, item=Item.LEAF_STONE))

# geodude
update_evolution(NAME_TO_POKEMON, PokemonGen4.GRAVELER, PokemonGen4.GOLEM, Evolution(name="", evolution_type=EvolutionType.TRADE, special_information="Sixth gym"),)

# slowpoke
update_evolution(NAME_TO_POKEMON, PokemonGen4.SLOWPOKE, PokemonGen4.SLOWKING, Evolution(name="", evolution_type=EvolutionType.TRADE, level=36, item=Item.KINGS_ROCK, special_information="Sixth gym"),)

# magnemite
update_evolution(NAME_TO_POKEMON, PokemonGen4.MAGNETON, PokemonGen4.MAGNEZONE, Evolution(name="", evolution_type=EvolutionType.LOCATION, special_information="Sixth gym, magnetic field"),)

# shellder
update_evolution(NAME_TO_POKEMON, PokemonGen4.SHELLDER, PokemonGen4.CLOYSTER, Evolution(name="", level=49, evolution_type=EvolutionType.STONE, item=Item.WATER_STONE))

# gastly
update_evolution(NAME_TO_POKEMON, PokemonGen4.HAUNTER, PokemonGen4.GENGAR, Evolution(name="", evolution_type=EvolutionType.TRADE, special_information="Sixth gym"),)

# onix
update_evolution(NAME_TO_POKEMON, PokemonGen4.ONIX, PokemonGen4.STEELIX, Evolution(name="", evolution_type=EvolutionType.TRADE, level=46, item=Item.METAL_COAT, special_information="Sixth gym"),)

# exeggcute
update_evolution(NAME_TO_POKEMON, PokemonGen4.EXEGGCUTE, PokemonGen4.EXEGGUTOR, Evolution(name="", level=47, evolution_type=EvolutionType.STONE, item=Item.LEAF_STONE))

# lickitung
update_evolution(NAME_TO_POKEMON, PokemonGen4.LICKITUNG, PokemonGen4.LICKILICKY, Evolution(name="", level=33, evolution_type=EvolutionType.MOVE, special_information="Rollout"))

# rhyhorn
update_evolution(NAME_TO_POKEMON, PokemonGen4.RHYDON, PokemonGen4.RHYPERIOR, Evolution(name="", evolution_type=EvolutionType.TRADE, level=44, item=Item.PROTECTOR),)

# chansey
update_evolution(NAME_TO_POKEMON, PokemonGen4.CHANSEY, PokemonGen4.BLISSEY, Evolution(name="", evolution_type=EvolutionType.FRIENDSHIP, special_information="Sixth Gym"))

# tangela
update_evolution(NAME_TO_POKEMON, PokemonGen4.TANGELA, PokemonGen4.TANGROWTH, Evolution(name="", level=33, evolution_type=EvolutionType.MOVE, special_information="Ancient Power"))

# horsea
update_evolution(NAME_TO_POKEMON, PokemonGen4.SEADRA, PokemonGen4.KINGDRA, Evolution(name="", evolution_type=EvolutionType.TRADE, item=Item.DRAGON_SCALE, special_information="Sixth gym"),)

# staryu
update_evolution(NAME_TO_POKEMON, PokemonGen4.STARYU, PokemonGen4.STARMIE, Evolution(name="", level=46, item=Item.WATER_STONE, evolution_type=EvolutionType.STONE))

# scyther
update_evolution(NAME_TO_POKEMON, PokemonGen4.SCYTHER, PokemonGen4.SCIZOR, Evolution(name="", level=53, evolution_type=EvolutionType.TRADE, item=Item.METAL_COAT, should_hold=True))

# elekid
update_evolution(NAME_TO_POKEMON, PokemonGen4.ELECTABUZZ, PokemonGen4.ELECTIVIRE, Evolution(name="", level=53, evolution_type=EvolutionType.TRADE, item=Item.ELECTRIZIER, should_hold=True))

# magmar
update_evolution(NAME_TO_POKEMON, PokemonGen4.MAGMAR, PokemonGen4.MAGMORTAR, Evolution(name="", level=43, evolution_type=EvolutionType.TRADE, item=Item.MAGMARIZER, should_hold=True))

# eevee
update_evolution(NAME_TO_POKEMON, PokemonGen4.EEVEE, PokemonGen4.GLACEON, Evolution(name="", item=Item.ICE_STONE, evolution_type=EvolutionType.STONE))
update_evolution(NAME_TO_POKEMON, PokemonGen4.EEVEE, PokemonGen4.LEAFEON, Evolution(name="", item=Item.LEAF_STONE, evolution_type=EvolutionType.STONE))

# porygon
update_evolution(NAME_TO_POKEMON, PokemonGen4.PORYGON, PokemonGen4.PORYGON2, Evolution(name="", evolution_type=EvolutionType.TRADE, item=Item.UPGRADE, should_hold=True, special_information="Second gym"))
update_evolution(NAME_TO_POKEMON, PokemonGen4.PORYGON2, PokemonGen4.PORYGON_Z, Evolution(name="", evolution_type=EvolutionType.TRADE, item=Item.DUBIOUS_DISC, should_hold=True, special_information="Sixth gym"))

# togepi
update_evolution(NAME_TO_POKEMON, PokemonGen4.TOGEPI, PokemonGen4.TOGETIC, Evolution(name="", evolution_type=EvolutionType.FRIENDSHIP, special_information="Second gym"))
update_evolution(NAME_TO_POKEMON, PokemonGen4.TOGETIC, PokemonGen4.TOGEKISS, Evolution(name="", evolution_type=EvolutionType.STONE, item=Item.SHINY_STONE, special_information="Sixth gym"))

# Azurill
update_evolution(NAME_TO_POKEMON, PokemonGen4.AZURILL, PokemonGen4.MARILL, Evolution(name="", evolution_type=EvolutionType.FRIENDSHIP, level=10))

# aipom
update_evolution(NAME_TO_POKEMON, PokemonGen4.AIPOM, PokemonGen4.AMBIPOM, Evolution(name="", level=32, evolution_type=EvolutionType.MOVE, special_information="Double Hit"))

# sunkern
update_evolution(NAME_TO_POKEMON, PokemonGen4.SUNKERN, PokemonGen4.SUNFLORA, Evolution(name="", item=Item.SUN_STONE, evolution_type=EvolutionType.STONE, level=29))

# yanma
update_evolution(NAME_TO_POKEMON, PokemonGen4.YANMA, PokemonGen4.YANMEGA, Evolution(name="", level=33, evolution_type=EvolutionType.MOVE, special_information="Ancient Power"))

# murkrow
update_evolution(NAME_TO_POKEMON, PokemonGen4.MURKROW, PokemonGen4.HONCHKROW, Evolution(name="", item=Item.DUSK_STONE, evolution_type=EvolutionType.STONE, level=35))

# misdreavus
update_evolution(NAME_TO_POKEMON, PokemonGen4.MISDREAVUS, PokemonGen4.MISMAGIUS, Evolution(name="", item=Item.DUSK_STONE, evolution_type=EvolutionType.STONE, level=50))

# gligar
update_evolution(NAME_TO_POKEMON, PokemonGen4.GLIGAR, PokemonGen4.GLISCOR, Evolution(name="", item=Item.RAZOR_FANG, evolution_type=EvolutionType.TIME, level=31, special_information="Night"))

# sneasel
update_evolution(NAME_TO_POKEMON, PokemonGen4.SNEASEL, PokemonGen4.WEAVILE, Evolution(name="", item=Item.RAZOR_CLAW, evolution_type=EvolutionType.TIME, level=35, special_information="Night"))

# swinub
update_evolution(NAME_TO_POKEMON, PokemonGen4.PILOSWINE, PokemonGen4.MAMOSWINE, Evolution(name="", level=33, evolution_type=EvolutionType.MOVE, special_information="Ancient Power. Not learened naturally. Sixth gym"))

# lotad
update_evolution(NAME_TO_POKEMON, PokemonGen4.LOMBRE, PokemonGen4.LUDICOLO, Evolution(name="", item=Item.WATER_STONE, evolution_type=EvolutionType.STONE, level=31))

# seedot
update_evolution(NAME_TO_POKEMON, PokemonGen4.NUZLEAF, PokemonGen4.SHIFTRY, Evolution(name="", item=Item.LEAF_STONE, evolution_type=EvolutionType.STONE, level=49))

# ralts
update_evolution(NAME_TO_POKEMON, PokemonGen4.KIRLIA, PokemonGen4.GALLADE, Evolution(name="", item=Item.DAWN_STONE, evolution_type=EvolutionType.STONE, level=31, special_information="Male"))

# nosepass
update_evolution(NAME_TO_POKEMON, PokemonGen4.NOSEPASS, PokemonGen4.PROBOPASS, Evolution(name="", evolution_type=EvolutionType.LOCATION, special_information="Fourth gym, magnetic field"),)

# skitty
update_evolution(NAME_TO_POKEMON, PokemonGen4.SKITTY, PokemonGen4.DELCATTY, Evolution(name="", item=Item.MOON_STONE, evolution_type=EvolutionType.STONE, level=29))

# Roselia
update_evolution(NAME_TO_POKEMON, PokemonGen4.ROSELIA, PokemonGen4.ROSERADE, Evolution(name="", item=Item.SHINY_STONE, evolution_type=EvolutionType.STONE, special_information="Sixth gym"))

# Feebas
update_evolution(NAME_TO_POKEMON, PokemonGen4.FEEBAS, PokemonGen4.MILOTIC, Evolution(name="", level=17, evolution_type=EvolutionType.TRADE, item=Item.PRISM_SCALE, should_hold=True))

# Duskull
update_evolution(NAME_TO_POKEMON, PokemonGen4.DUSCLOPS, PokemonGen4.DUSKNOIR, Evolution(name="", evolution_type=EvolutionType.TRADE, item=Item.REAPER_CLOTH, should_hold=True, special_information="Sixth gym"))

# snorunt
update_evolution(NAME_TO_POKEMON, PokemonGen4.SNORUNT, PokemonGen4.FROSLASS, Evolution(name="", item=Item.DAWN_STONE, evolution_type=EvolutionType.STONE, level=22, special_information="Female"))

# clamperl
update_evolution(NAME_TO_POKEMON, PokemonGen4.CLAMPERL, PokemonGen4.HUNTAIL, Evolution(name="", evolution_type=EvolutionType.TRADE, item=Item.DEEP_SEA_TOOTH, should_hold=True, level=15))
update_evolution(NAME_TO_POKEMON, PokemonGen4.CLAMPERL, PokemonGen4.GOREBYSS, Evolution(name="", evolution_type=EvolutionType.TRADE, item=Item.DEEP_SEA_SCALE, should_hold=True, level=15))

_GEN4_POKEMONS = {
     PokemonGen4.TURTWIG: Pokemon(
         name=PokemonGen4.TURTWIG,
         gen=4,
         types=[Types.GRASS],
         evolves_to=[
             Evolution(name=PokemonGen4.GROTLE)
         ],
         colors=[Colors.GREEN, Colors.BROWN],
         supported_genders=[Genders.MALE, Genders.FEMALE],
         stats=Stats(
             attack=68,
             defence=64,
             special_attack=45,
             special_defence=55,
         ),
         categories=[
             Categories.PREHISTORIC, Categories.PLANT, Categories.REPTILE, Categories.FOOD, Categories.TURTLE,
         ],
         num_legs=4,
         supported_abilities=[Abilities.OVERGROW],
     ),
      PokemonGen4.GROTLE: Pokemon(
         name=PokemonGen4.GROTLE,
         gen=4,
         types=[Types.GRASS],
         evolves_to=[
             Evolution(name=PokemonGen4.TORTERRA)
         ],
         colors=[Colors.GREEN, Colors.BROWN],
         supported_genders=[Genders.MALE, Genders.FEMALE],
         stats=Stats(
             attack=89,
             defence=85,
             special_attack=55,
             special_defence=65,
         ),
         categories=[
             Categories.PREHISTORIC, Categories.PLANT, Categories.REPTILE, Categories.FOOD, Categories.TURTLE,
         ],
         num_legs=4,
         supported_abilities=[Abilities.OVERGROW],
     ),
      PokemonGen4.TORTERRA: Pokemon(
         name=PokemonGen4.TORTERRA,
         gen=4,
         types=[Types.GRASS, Types.GROUND],
         evolves_to=[],
         colors=[Colors.GREEN, Colors.BROWN],
         supported_genders=[Genders.MALE, Genders.FEMALE],
         stats=Stats(
             attack=109,
             defence=105,
             special_attack=75,
             special_defence=85,
         ),
         categories=[
             Categories.PREHISTORIC, Categories.PLANT, Categories.REPTILE, Categories.FOOD, Categories.TURTLE,
         ],
         num_legs=4,
         supported_abilities=[Abilities.OVERGROW],
     ),
      PokemonGen4.CHIMCHAR: Pokemon(
         name=PokemonGen4.CHIMCHAR,
         gen=4,
         types=[Types.FIRE],
         evolves_to=[
             Evolution(name=PokemonGen4.MONFERNO)
         ],
         colors=[Colors.ORANGE, Colors.WHITE],
         supported_genders=[Genders.MALE, Genders.FEMALE],
         stats=Stats(
             attack=58,
             defence=44,
             special_attack=58,
             special_defence=44,
         ),
         categories=[
             Categories.MAMMAL, Categories.APE,
         ],
         num_legs=2,
         supported_abilities=[Abilities.BLAZE],
     ),
      PokemonGen4.MONFERNO: Pokemon(
         name=PokemonGen4.MONFERNO,
         gen=4,
         types=[Types.FIRE, Types.FIGHTING],
         evolves_to=[
             Evolution(name=PokemonGen4.INFERNAPE)
         ], 
         colors=[Colors.ORANGE, Colors.WHITE],
         supported_genders=[Genders.MALE, Genders.FEMALE],
         stats=Stats(
             attack=78,
             defence=52,
             special_attack=78,
             special_defence=52,
         ),
         categories=[
             Categories.MAMMAL, Categories.APE,
         ],
         num_legs=2,
         supported_abilities=[Abilities.BLAZE],
     ),
      PokemonGen4.INFERNAPE: Pokemon(
         name=PokemonGen4.INFERNAPE,
         gen=4,
         types=[Types.FIRE, Types.FIGHTING],
         evolves_to=[],
         colors=[Colors.ORANGE, Colors.WHITE, Colors.YELLOW],
         supported_genders=[Genders.MALE, Genders.FEMALE],
         stats=Stats(
             attack=104,
             defence=71,
             special_attack=104,
             special_defence=71,
         ),
         categories=[
             Categories.MAMMAL, Categories.APE,
         ],
         num_legs=2,
         supported_abilities=[Abilities.BLAZE],
     ),
      PokemonGen4.PIPLUP: Pokemon(
         name=PokemonGen4.PIPLUP,
         gen=4,
         types=[Types.WATER],
         evolves_to=[
             Evolution(name=PokemonGen4.PRINPLUP)
         ],
         colors=[Colors.BLUE],
         supported_genders=[Genders.MALE, Genders.FEMALE],
         stats=Stats(
             attack=51,
             defence=53,
             special_attack=61,
             special_defence=56,
         ),
         categories=[
             Categories.WING, Categories.BIRD, Categories.WATERMON,
         ],
         num_legs=2,
         supported_abilities=[Abilities.TORRENT],
     ),
      PokemonGen4.PRINPLUP: Pokemon(
         name=PokemonGen4.PRINPLUP,
         gen=4,
         types=[Types.WATER],
         evolves_to=[
             Evolution(name=PokemonGen4.EMPOLEON)
         ],
         colors=[Colors.BLUE],
         supported_genders=[Genders.MALE, Genders.FEMALE],
         stats=Stats(
             attack=66,
             defence=68,
             special_attack=81,
             special_defence=76,
         ),
         categories=[
             Categories.WING, Categories.BIRD, Categories.WATERMON,
         ],
         num_legs=2,
         supported_abilities=[Abilities.TORRENT],
     ),
      PokemonGen4.EMPOLEON: Pokemon(
         name=PokemonGen4.EMPOLEON,
         gen=4,
         types=[Types.WATER, Types.STEEL],
         evolves_to=[],
         colors=[Colors.BLUE, Colors.WHITE],
         supported_genders=[Genders.MALE, Genders.FEMALE],
         stats=Stats(
             attack=86,
             defence=88,
             special_attack=111,
             special_defence=101,
         ),
         categories=[
             Categories.WING, Categories.BIRD, Categories.WATERMON,
         ],
         num_legs=2,
         supported_abilities=[Abilities.TORRENT],
     ),
      PokemonGen4.STARLY: Pokemon(
         name=PokemonGen4.STARLY,
         gen=4,
         types=[Types.NORMAL, Types.FLYING],
         evolves_to=[
             Evolution(name=PokemonGen4.STARAVIA)
         ],
         colors=[Colors.GRAY, Colors.WHITE],
         supported_genders=[Genders.MALE, Genders.FEMALE],
         stats=Stats(
             attack=55,
             defence=30,
             special_attack=30,
             special_defence=30,
         ),
         categories=[
             Categories.WING, Categories.BIRD,
         ],
         num_legs=2,
         supported_abilities=[Abilities.KEEN_EYE],
     ),
      PokemonGen4.STARAVIA: Pokemon(
         name=PokemonGen4.STARAVIA,
         gen=4,
         types=[Types.NORMAL, Types.FLYING],
         evolves_to=[
             Evolution(name=PokemonGen4.STARAPTOR)
         ],
         colors=[Colors.GRAY, Colors.WHITE],
         supported_genders=[Genders.MALE, Genders.FEMALE],
         stats=Stats(
             attack=75,
             defence=50,
             special_attack=40,
             special_defence=40,
         ),
         categories=[
             Categories.WING, Categories.BIRD,
         ],
         num_legs=2,
         supported_abilities=[Abilities.INTIMIDATE],
     ),
      PokemonGen4.STARAPTOR: Pokemon(
         name=PokemonGen4.STARAPTOR,
         gen=4,
         types=[Types.NORMAL, Types.FLYING],
         evolves_to=[],
         colors=[Colors.GRAY, Colors.WHITE],
         supported_genders=[Genders.MALE, Genders.FEMALE],
         stats=Stats(
             attack=120,
             defence=70,
             special_attack=50,
             special_defence=60,
         ),
         categories=[
             Categories.WING, Categories.BIRD,
         ],
         num_legs=2,
         supported_abilities=[Abilities.INTIMIDATE],
     ),
     PokemonGen4.BIDOOF: Pokemon(
        name=PokemonGen4.BIDOOF,
        gen=4,
        types=[Types.NORMAL],
        evolves_to=[
            Evolution(name=PokemonGen4.BIBAREL)
        ],
        colors=[Colors.BROWN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=45,
            defence=40,
            special_attack=35,
            special_defence=40,
        ),
        categories=[
            Categories.MAMMAL, Categories.RODENT, Categories.WATERMON,
        ],
        num_legs=4,
        supported_abilities=[Abilities.SIMPLE, Abilities.UNAWARE],
    ),
    PokemonGen4.BIBAREL: Pokemon(
        name=PokemonGen4.BIBAREL,
        gen=4,
        types=[Types.NORMAL, Types.WATER],
        evolves_to=[],
        colors=[Colors.BROWN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=85,
            defence=60,
            special_attack=55,
            special_defence=60,
        ),
        categories=[
            Categories.MAMMAL, Categories.RODENT, Categories.WATERMON,
        ],
        num_legs=2,
        supported_abilities=[Abilities.SIMPLE, Abilities.UNAWARE],
    ),
    PokemonGen4.KRICKETOT: Pokemon(
        name=PokemonGen4.KRICKETOT,
        gen=4,
        types=[Types.BUG],
        evolves_to=[
            Evolution(name=PokemonGen4.KRICKETUNE)
        ],
        colors=[Colors.RED, Colors.YELLOW],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=25,
            defence=41,
            special_attack=25,
            special_defence=41,
        ),
        categories=[
            Categories.WING, Categories.BUG,
        ],
        num_legs=2,
        supported_abilities=[Abilities.SHED_SKIN],
    ),
    PokemonGen4.KRICKETUNE: Pokemon(
        name=PokemonGen4.KRICKETUNE,
        gen=4,
        types=[Types.BUG],
        evolves_to=[],
        colors=[Colors.RED, Colors.YELLOW, Colors.BLACK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=85,
            defence=51,
            special_attack=55,
            special_defence=51,
        ),
        categories=[
            Categories.WING, Categories.BUG,
        ],
        num_legs=2,
        supported_abilities=[Abilities.SWARM],
    ),
    PokemonGen4.SHINX: Pokemon(
        name=PokemonGen4.SHINX,
        gen=4,
        types=[Types.ELECTRIC],
        evolves_to=[
            Evolution(name=PokemonGen4.LUXIO)
        ],
        colors=[Colors.YELLOW, Colors.BLACK, Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=65,
            defence=34,
            special_attack=40,
            special_defence=34,
        ),
        categories=[
            Categories.MAMMAL, Categories.CAT,
        ],
        num_legs=4,
        supported_abilities=[Abilities.RIVALRY, Abilities.INTIMIDATE],
    ),
    PokemonGen4.LUXIO: Pokemon(
        name=PokemonGen4.LUXIO,
        gen=4,
        types=[Types.ELECTRIC],
        evolves_to=[
            Evolution(name=PokemonGen4.LUXRAY)
        ],
        colors=[Colors.YELLOW, Colors.BLACK, Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=85,
            defence=49,
            special_attack=60,
            special_defence=49,
        ),
        categories=[
            Categories.MAMMAL, Categories.CAT,
        ],
        num_legs=4,
        supported_abilities=[Abilities.RIVALRY, Abilities.INTIMIDATE],
    ),
    PokemonGen4.LUXRAY: Pokemon(
        name=PokemonGen4.LUXRAY,
        gen=4,
        types=[Types.ELECTRIC],
        evolves_to=[],
        colors=[Colors.YELLOW, Colors.BLACK, Colors.BLUE, Colors.GRAY],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=120,
            defence=79,
            special_attack=95,
            special_defence=79,
        ),
        categories=[
            Categories.MAMMAL, Categories.CAT,
        ],
        num_legs=4,
        supported_abilities=[Abilities.RIVALRY, Abilities.INTIMIDATE],
    ),
    PokemonGen4.BUDEW: Pokemon(
        name=PokemonGen4.BUDEW,
        gen=4,
        types=[Types.GRASS, Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen4.ROSELIA, evolution_type=EvolutionType.FRIENDSHIP, level=13, special_information="Day")
        ],
        colors=[Colors.GREEN, Colors.YELLOW],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=30,
            defence=35,
            special_attack=50,
            special_defence=70,
        ),
        categories=[
            Categories.PLANT
        ],
        num_legs=2,
        supported_abilities=[Abilities.NATURAL_CURE, Abilities.POISON_POINT],
    ),
    PokemonGen4.ROSERADE: Pokemon(
        name=PokemonGen4.ROSERADE,
        gen=4,
        types=[Types.GRASS, Types.POISON],
        evolves_to=[],
        colors=[Colors.GREEN, Colors.RED, Colors.PURPLE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=70,
            defence=65,
            special_attack=125,
            special_defence=105,
        ),
        categories=[
            Categories.PLANT
        ],
        num_legs=2,
        supported_abilities=[Abilities.NATURAL_CURE, Abilities.POISON_POINT],
    ),
    PokemonGen4.CRANIDOS: Pokemon(
        name=PokemonGen4.CRANIDOS,
        gen=4,
        types=[Types.ROCK],
        evolves_to=[
            Evolution(name=PokemonGen4.RAMPARDOS)
        ],
        colors=[Colors.GRAY, Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=125,
            defence=40,
            special_attack=30,
            special_defence=30,
        ),
        categories=[
            Categories.PREHISTORIC, Categories.REPTILE,
        ],
        num_legs=2,
        supported_abilities=[Abilities.MOLD_BREAKER],
    ),
    PokemonGen4.RAMPARDOS: Pokemon(
        name=PokemonGen4.RAMPARDOS,
        gen=4,
        types=[Types.ROCK],
        evolves_to=[],
        colors=[Colors.GRAY, Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=165,
            defence=60,
            special_attack=65,
            special_defence=50,
        ),
        categories=[
            Categories.PREHISTORIC, Categories.REPTILE,
        ],
        num_legs=2,
        supported_abilities=[Abilities.MOLD_BREAKER],
    ),
    PokemonGen4.SHIELDON: Pokemon(
        name=PokemonGen4.SHIELDON,
        gen=4,
        types=[Types.ROCK, Types.STEEL],
        evolves_to=[
            Evolution(name=PokemonGen4.BASTIODON)
        ],
        colors=[Colors.YELLOW, Colors.GRAY],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=42,
            defence=118,
            special_attack=42,
            special_defence=88,
        ),
        categories=[
            Categories.PREHISTORIC, Categories.REPTILE,
        ],
        num_legs=4,
        supported_abilities=[Abilities.STURDY],
    ),
    PokemonGen4.BASTIODON: Pokemon(
        name=PokemonGen4.BASTIODON,
        gen=4,
        types=[Types.ROCK, Types.STEEL],
        evolves_to=[],
        colors=[Colors.YELLOW, Colors.GRAY],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=52,
            defence=168,
            special_attack=47,
            special_defence=138,
        ),
        categories=[
            Categories.PREHISTORIC, Categories.REPTILE,
        ],
        num_legs=4,
        supported_abilities=[Abilities.STURDY],
    ),
    PokemonGen4.BURMY: Pokemon(
        name=PokemonGen4.BURMY,
        gen=4,
        types=[Types.BUG],
        evolves_to=[
            Evolution(name=PokemonGen4.MOTHIM, special_information="Male"),
            Evolution(name=PokemonGen4.WORMADAM_SANDY, level=20, special_information="Female, in caves"),
            Evolution(name=PokemonGen4.WORMADAM_TRASH, level=20, special_information="Female, in buildings"),
            Evolution(name=PokemonGen4.WORMADAM_PLANT, level=20, special_information="Female, in grass"),
        ],
        colors=[Colors.GREEN, Colors.BLACK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=29,
            defence=45,
            special_attack=29,
            special_defence=45,
        ),
        categories=[
            Categories.BUG, Categories.PLANT
        ],
        num_legs=2,
        supported_abilities=[Abilities.SHED_SKIN],
    ),
    PokemonGen4.WORMADAM_SANDY: Pokemon(
        name=PokemonGen4.WORMADAM_SANDY,
        gen=4,
        types=[Types.BUG, Types.GROUND],
        evolves_to=[],
        colors=[Colors.YELLOW, Colors.BLACK, Colors.BROWN],
        supported_genders=[Genders.FEMALE],
        stats=Stats(
            attack=79,
            defence=105,
            special_attack=59,
            special_defence=85,
        ),
        categories=[
            Categories.BUG
        ],
        num_legs=0,
        supported_abilities=[Abilities.ANTICIPATION],
        form="Sandy",
        base_name="Wormadam",
    ),
    PokemonGen4.WORMADAM_TRASH: Pokemon(
        name=PokemonGen4.WORMADAM_TRASH,
        gen=4,
        types=[Types.BUG, Types.STEEL],
        evolves_to=[],
        colors=[Colors.GRAY, Colors.BLACK, Colors.PINK],
        supported_genders=[Genders.FEMALE],
        stats=Stats(
            attack=69,
            defence=95,
            special_attack=69,
            special_defence=95,
        ),
        categories=[
            Categories.BUG
        ],
        num_legs=0,
        supported_abilities=[Abilities.ANTICIPATION],
        form="Trash",
        base_name="Wormadam",
    ),
    PokemonGen4.WORMADAM_PLANT: Pokemon(
        name=PokemonGen4.WORMADAM_PLANT,
        gen=4,
        types=[Types.BUG, Types.GRASS],
        evolves_to=[],
        colors=[Colors.GREEN, Colors.BLACK],
        supported_genders=[Genders.FEMALE],
        stats=Stats(
            attack=95,
            defence=85,
            special_attack=79,
            special_defence=105,
        ),
        categories=[
            Categories.BUG, Categories.PLANT,
        ],
        num_legs=0,
        supported_abilities=[Abilities.ANTICIPATION],
        form="Plant",
        base_name="Wormadam",
    ),
    PokemonGen4.MOTHIM: Pokemon(
        name=PokemonGen4.MOTHIM,
        gen=4,
        types=[Types.BUG, Types.FLYING],
        evolves_to=[],
        colors=[Colors.BLACK, Colors.BLACK, Colors.ORANGE],
        supported_genders=[Genders.MALE],
        stats=Stats(
            attack=94,
            defence=50,
            special_attack=94,
            special_defence=50,
        ),
        categories=[
            Categories.WING, Categories.BUG,
        ],
        num_legs=4,
        supported_abilities=[Abilities.SWARM],
    ),
    PokemonGen4.COMBEE: Pokemon(
        name=PokemonGen4.COMBEE,
        gen=4,
        types=[Types.BUG, Types.FLYING],
        evolves_to=[
            Evolution(name=PokemonGen4.VESPIQUEN, special_information="Female")
        ],
        colors=[Colors.YELLOW, Colors.BLACK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=30,
            defence=42,
            special_attack=30,
            special_defence=42,
        ),
        categories=[
            Categories.WING, Categories.BUG, Categories.FOOD,
        ],
        num_legs=0,
        supported_abilities=[Abilities.HONEY_GATHER],
    ),
    PokemonGen4.VESPIQUEN: Pokemon(
        name=PokemonGen4.VESPIQUEN,
        gen=4,
        types=[Types.BUG, Types.FLYING],
        evolves_to=[],
        colors=[Colors.YELLOW, Colors.BLACK],
        supported_genders=[Genders.FEMALE],
        stats=Stats(
            attack=80,
            defence=102,
            special_attack=80,
            special_defence=102,
        ),
        categories=[
            Categories.WING, Categories.BUG, Categories.FOOD,
        ],
        num_legs=0,
        supported_abilities=[Abilities.PRESSURE],
    ),
    PokemonGen4.PACHIRISU: Pokemon(
        name=PokemonGen4.PACHIRISU,
        gen=4,
        types=[Types.ELECTRIC],
        evolves_to=[],
        colors=[Colors.WHITE, Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=45,
            defence=70,
            special_attack=45,
            special_defence=90,
        ),
        categories=[
            Categories.MAMMAL, Categories.RODENT,
        ],
        num_legs=2,
        supported_abilities=[Abilities.RUN_AWAY, Abilities.PICKUP],
    ),
    PokemonGen4.BUIZEL: Pokemon(
        name=PokemonGen4.BUIZEL,
        gen=4,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen4.FLOATZEL)
        ],
        colors=[Colors.ORANGE, Colors.YELLOW],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=65,
            defence=35,
            special_attack=60,
            special_defence=30,
        ),
        categories=[
            Categories.MAMMAL
        ],
        num_legs=2,
        supported_abilities=[Abilities.SWIFT_SWIM],
    ),
    PokemonGen4.FLOATZEL: Pokemon(
        name=PokemonGen4.FLOATZEL,
        gen=4,
        types=[Types.WATER],
        evolves_to=[],
        colors=[Colors.ORANGE, Colors.YELLOW],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=105,
            defence=55,
            special_attack=85,
            special_defence=50,
        ),
        categories=[
            Categories.MAMMAL,
        ],
        num_legs=2,
        supported_abilities=[Abilities.SWIFT_SWIM],
    ),
    PokemonGen4.CHERUBI: Pokemon(
        name=PokemonGen4.CHERUBI,
        gen=4,
        types=[Types.GRASS],
        evolves_to=[
            Evolution(name=PokemonGen4.CHERRIM)
        ],
        colors=[Colors.GREEN, Colors.PINK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=35,
            defence=45,
            special_attack=62,
            special_defence=53,
        ),
        categories=[
            Categories.PLANT, Categories.FOOD,
        ],
        num_legs=2,
        supported_abilities=[Abilities.CHLOROPHYLL],
    ),
    PokemonGen4.CHERRIM: Pokemon(
        name=PokemonGen4.CHERRIM,
        gen=4,
        types=[Types.GRASS],
        evolves_to=[],
        colors=[Colors.PURPLE, Colors.GREEN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=60,
            defence=70,
            special_attack=87,
            special_defence=78,
        ),
        categories=[
            Categories.PLANT, Categories.FOOD,
        ],
        num_legs=2,
        supported_abilities=[Abilities.FLOWER_GIFT],
    ),
    PokemonGen4.SHELLOS: Pokemon(
        name=PokemonGen4.SHELLOS,
        gen=4,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen4.GASTRODON)
        ],
        colors=[Colors.PINK, Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=48,
            defence=48,
            special_attack=57,
            special_defence=62,
        ),
        categories=[
            Categories.REPTILE, Categories.WATERMON, Categories.FOOD, Categories.TURTLE,
        ],
        num_legs=0,
        supported_abilities=[Abilities.STICKY_HOLD, Abilities.STORM_DRAIN],
    ),
    PokemonGen4.GASTRODON: Pokemon(
        name=PokemonGen4.GASTRODON,
        gen=4,
        types=[Types.WATER, Types.GROUND],
        evolves_to=[],
        colors=[Colors.PINK, Colors.BLUE, Colors.BROWN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=83,
            defence=68,
            special_attack=92,
            special_defence=82,
        ),
        categories=[
            Categories.REPTILE, Categories.WATERMON, Categories.FOOD, Categories.TURTLE,
        ],
        num_legs=9,
        supported_abilities=[Abilities.STICKY_HOLD, Abilities.STORM_DRAIN],
    ),
    PokemonGen4.AMBIPOM: Pokemon(
        name=PokemonGen4.AMBIPOM,
        gen=4,
        types=[Types.NORMAL],
        evolves_to=[],
        colors=[Colors.PURPLE, Colors.WHITE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=100,
            defence=66,
            special_attack=60,
            special_defence=66,
        ),
        categories=[
            Categories.MAMMAL, Categories.APE,
        ],
        num_legs=2,
        supported_abilities=[Abilities.TECHNICIAN, Abilities.PICKUP],
    ),
    PokemonGen4.DRIFLOON: Pokemon(
        name=PokemonGen4.DRIFLOON,
        gen=4,
        types=[Types.GHOST, Types.FLYING],
        evolves_to=[
            Evolution(name=PokemonGen4.DRIFBLIM)
        ],
        colors=[Colors.PURPLE, Colors.WHITE, Colors.YELLOW],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=50,
            defence=34,
            special_attack=60,
            special_defence=44,
        ),
        categories=[
            Categories.ITEM
        ],
        num_legs=0,
        supported_abilities=[Abilities.AFTERMATH, Abilities.UNBURDEN],
    ),
    PokemonGen4.DRIFBLIM: Pokemon(
        name=PokemonGen4.DRIFBLIM,
        gen=4,
        types=[Types.GHOST, Types.FLYING],
        evolves_to=[],
        colors=[Colors.PURPLE, Colors.WHITE, Colors.YELLOW],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=80,
            defence=44,
            special_attack=90,
            special_defence=54,
        ),
        categories=[
            Categories.ITEM
        ],
        num_legs=0,
        supported_abilities=[Abilities.AFTERMATH, Abilities.UNBURDEN],
    ),
    PokemonGen4.BUNEARY: Pokemon(
        name=PokemonGen4.BUNEARY,
        gen=4,
        types=[Types.NORMAL],
        evolves_to=[
            Evolution(name=PokemonGen4.LOPUNNY, evolution_type=EvolutionType.FRIENDSHIP, level=13)
        ],
        colors=[Colors.BROWN, Colors.WHITE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=66,
            defence=44,
            special_attack=44,
            special_defence=56,
        ),
        categories=[
            Categories.MAMMAL, Categories.FOOD, Categories.BUNNY,
        ],
        num_legs=2,
        supported_abilities=[Abilities.RUN_AWAY, Abilities.KLUTZ],
    ),
    PokemonGen4.LOPUNNY: Pokemon(
        name=PokemonGen4.LOPUNNY,
        gen=4,
        types=[Types.NORMAL],
        evolves_to=[],
        colors=[Colors.BROWN, Colors.WHITE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=76,
            defence=84,
            special_attack=54,
            special_defence=96,
        ),
        categories=[
            Categories.MAMMAL, Categories.FOOD, Categories.BUNNY,
        ],
        num_legs=2,
        supported_abilities=[Abilities.CUTE_CHARM, Abilities.KLUTZ],
    ),
    PokemonGen4.MISMAGIUS: Pokemon(
        name=PokemonGen4.MISMAGIUS,
        gen=4,
        types=[Types.GHOST],
        evolves_to=[],
        colors=[Colors.PURPLE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=60,
            defence=60,
            special_attack=105,
            special_defence=105,
        ),
        categories=[
            Categories.MAMMAL, Categories.FANTASY, Categories.HUMAN,
        ],
        num_legs=0,
        supported_abilities=[Abilities.LEVITATE],
    ),
    PokemonGen4.HONCHKROW: Pokemon(
        name=PokemonGen4.HONCHKROW,
        gen=4,
        types=[Types.DARK, Types.FLYING],
        evolves_to=[],
        colors=[Colors.BLACK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=125,
            defence=52,
            special_attack=105,
            special_defence=52,
        ),
        categories=[
            Categories.WING, Categories.BIRD, Categories.FANTASY,
        ],
        num_legs=2,
        supported_abilities=[Abilities.INSOMNIA, Abilities.SUPER_LUCK],
    ),
    PokemonGen4.GLAMEOW: Pokemon(
        name=PokemonGen4.GLAMEOW,
        gen=4,
        types=[Types.NORMAL],
        evolves_to=[
            Evolution(name=PokemonGen4.PURUGLY)
        ],
        colors=[Colors.GRAY],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=55,
            defence=42,
            special_attack=42,
            special_defence=37,
        ),
        categories=[
            Categories.MAMMAL, Categories.CAT
        ],
        num_legs=4,
        supported_abilities=[Abilities.LIMBER, Abilities.OWN_TEMPO],
    ),
    PokemonGen4.PURUGLY: Pokemon(
        name=PokemonGen4.PURUGLY,
        gen=4,
        types=[Types.NORMAL],
        evolves_to=[],
        colors=[Colors.GRAY, Colors.WHITE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=82,
            defence=64,
            special_attack=64,
            special_defence=59,
        ),
        categories=[
            Categories.MAMMAL, Categories.CAT
        ],
        num_legs=4,
        supported_abilities=[Abilities.THICK_FAT, Abilities.OWN_TEMPO],
    ),
    PokemonGen4.CHINGLING: Pokemon(
        name=PokemonGen4.CHINGLING,
        gen=4,
        types=[Types.PSYCHIC],
        evolves_to=[
            Evolution(name=PokemonGen4.CHIMECHO, level=17, evolution_type=EvolutionType.FRIENDSHIP, special_information="Night")
        ],
        colors=[Colors.YELLOW, Colors.RED],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=30,
            defence=50,
            special_attack=65,
            special_defence=50,
        ),
        categories=[
            Categories.ITEM
        ],
        num_legs=2,
        supported_abilities=[Abilities.LEVITATE],
    ),
    PokemonGen4.STUNKY: Pokemon(
        name=PokemonGen4.STUNKY,
        gen=4,
        types=[Types.POISON, Types.DARK],
        evolves_to=[
            Evolution(name=PokemonGen4.SKUNTANK)
        ],
        colors=[Colors.PURPLE, Colors.WHITE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=63,
            defence=47,
            special_attack=41,
            special_defence=41,
        ),
        categories=[
            Categories.MAMMAL
        ],
        num_legs=4,
        supported_abilities=[Abilities.STENCH, Abilities.AFTERMATH],
    ),
    PokemonGen4.SKUNTANK: Pokemon(
        name=PokemonGen4.SKUNTANK,
        gen=4,
        types=[Types.POISON, Types.DARK],
        evolves_to=[],
        colors=[Colors.PURPLE, Colors.WHITE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=93,
            defence=67,
            special_attack=71,
            special_defence=61,
        ),
        categories=[
            Categories.MAMMAL,
        ],
        num_legs=4,
        supported_abilities=[Abilities.STENCH, Abilities.AFTERMATH],
    ),
    PokemonGen4.BRONZOR: Pokemon(
        name=PokemonGen4.BRONZOR,
        gen=4,
        types=[Types.STEEL, Types.PSYCHIC],
        evolves_to=[
            Evolution(name=PokemonGen4.BRONZONG)
        ],
        colors=[Colors.BLUE],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=24,
            defence=86,
            special_attack=24,
            special_defence=86,
        ),
        categories=[
            Categories.ITEM
        ],
        num_legs=0,
        supported_abilities=[Abilities.LEVITATE, Abilities.HEATPROOF],
    ),
    PokemonGen4.BRONZONG: Pokemon(
        name=PokemonGen4.BRONZONG,
        gen=4,
        types=[Types.STEEL, Types.PSYCHIC],
        evolves_to=[],
        colors=[Colors.BLUE],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=89,
            defence=116,
            special_attack=79,
            special_defence=86,
        ),
        categories=[
            Categories.ITEM
        ],
        num_legs=0,
        supported_abilities=[Abilities.LEVITATE, Abilities.HEATPROOF],
    ),
    PokemonGen4.BONSLY: Pokemon(
        name=PokemonGen4.BONSLY,
        gen=4,
        types=[Types.ROCK],
        evolves_to=[
            Evolution(name=PokemonGen4.SUDOWOODO, level=17, evolution_type=EvolutionType.MOVE, special_information="Mimic")
        ],
        colors=[Colors.BROWN, Colors.GREEN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=80,
            defence=95,
            special_attack=10,
            special_defence=45,
        ),
        categories=[
            Categories.PLANT,
        ],
        num_legs=2,
        supported_abilities=[Abilities.STURDY, Abilities.ROCK_HEAD],
    ),
    PokemonGen4.MIME_JR: Pokemon(
        name=PokemonGen4.MIME_JR,
        gen=4,
        types=[Types.PSYCHIC],
        evolves_to=[
            Evolution(name=PokemonGen4.MR_MIME, level=18, evolution_type=EvolutionType.MOVE, special_information="Mimic")
        ],
        colors=[Colors.PINK, Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=25,
            defence=45,
            special_attack=70,
            special_defence=90,
        ),
        categories=[
            Categories.MAMMAL, Categories.HUMAN
        ],
        num_legs=2,
        supported_abilities=[Abilities.SOUNDPROOF, Abilities.FILTER],
    ),
    PokemonGen4.HAPPINY: Pokemon(
        name=PokemonGen4.HAPPINY,
        gen=4,
        types=[Types.NORMAL],
        evolves_to=[
            Evolution(level=12, name=PokemonGen4.CHANSEY, evolution_type=EvolutionType.STONE, item=Item.OVAL_STONE, should_hold=True)
        ],
        colors=[Colors.PINK, Colors.WHITE],
        supported_genders=[Genders.FEMALE],
        stats=Stats(
            attack=5,
            defence=5,
            special_attack=15,
            special_defence=65,
        ),
        categories=[
            Categories.MAMMAL, Categories.FOOD, Categories.HUMAN,
        ],
        num_legs=2,
        supported_abilities=[Abilities.NATURAL_CURE, Abilities.SERENE_GRACE],
    ),
    PokemonGen4.CHATOT: Pokemon(
        name=PokemonGen4.CHATOT,
        gen=4,
        types=[Types.NORMAL, Types.FLYING],
        evolves_to=[],
        colors=[Colors.BLUE, Colors.WHITE, Colors.YELLOW, Colors.RED, Colors.BLACK, Colors.GREEN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=65,
            defence=45,
            special_attack=92,
            special_defence=42,
        ),
        categories=[
            Categories.WING, Categories.BIRD,
        ],
        num_legs=2,
        supported_abilities=[Abilities.KEEN_EYE, Abilities.TANGLED_FEET],
    ),
    PokemonGen4.SPIRITOMB: Pokemon(
        name=PokemonGen4.SPIRITOMB,
        gen=4,
        types=[Types.GHOST, Types.DARK],
        evolves_to=[],
        colors=[Colors.PINK, Colors.GREEN, Colors.GRAY],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=92,
            defence=108,
            special_attack=92,
            special_defence=108,
        ),
        categories=[
            Categories.ITEM, Categories.FANTASY,
        ],
        num_legs=0,
        supported_abilities=[Abilities.PRESSURE],
    ),
    PokemonGen4.GIBLE: Pokemon(
        name=PokemonGen4.GIBLE,
        gen=4,
        types=[Types.DRAGON, Types.GROUND],
        evolves_to=[
            Evolution(name=PokemonGen4.GABITE)
        ],
        colors=[Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=70,
            defence=45,
            special_attack=40,
            special_defence=45,
        ),
        categories=[
            Categories.WATERMON, Categories.FOOD, Categories.FISH
        ],
        num_legs=2,
        supported_abilities=[Abilities.SAND_VEIL],
    ),
    PokemonGen4.GABITE: Pokemon(
        name=PokemonGen4.GABITE,
        gen=4,
        types=[Types.DRAGON, Types.GROUND],
        evolves_to=[
            Evolution(name=PokemonGen4.GARCHOMP)
        ],
        colors=[Colors.BLUE, Colors.RED],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=90,
            defence=65,
            special_attack=50,
            special_defence=55,
        ),
        categories=[
            Categories.WATERMON, Categories.FOOD, Categories.FISH
        ],
        num_legs=2,
        supported_abilities=[Abilities.SAND_VEIL],
    ),
    PokemonGen4.GARCHOMP: Pokemon(
        name=PokemonGen4.GARCHOMP,
        gen=4,
        types=[Types.DRAGON, Types.GROUND],
        evolves_to=[],
        colors=[Colors.BLUE, Colors.RED],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=130,
            defence=95,
            special_attack=80,
            special_defence=85,
        ),
        categories=[
            Categories.WATERMON, Categories.FOOD, Categories.FISH, Categories.WEAPON
        ],
        num_legs=2,
        supported_abilities=[Abilities.SAND_VEIL],
    ),
    PokemonGen4.MUNCHLAX: Pokemon(
        name=PokemonGen4.MUNCHLAX,
        gen=4,
        types=[Types.NORMAL],
        evolves_to=[
            Evolution(name=PokemonGen4.SNORLAX, evolution_type=EvolutionType.FRIENDSHIP, level=17)
        ],
        colors=[Colors.GREEN, Colors.WHITE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=85,
            defence=40,
            special_attack=40,
            special_defence=85,
        ),
        categories=[
            Categories.MAMMAL, Categories.BEAR
        ],
        num_legs=2,
        supported_abilities=[Abilities.PICKUP, Abilities.THICK_FAT],
    ),
    PokemonGen4.RIOLU: Pokemon(
        name=PokemonGen4.RIOLU,
        gen=4,
        types=[Types.FIGHTING],
        evolves_to=[
            Evolution(name=PokemonGen4.LUCARIO, level=19, evolution_type=EvolutionType.FRIENDSHIP, special_information="Day")
        ],
        colors=[Colors.BLUE, Colors.BLACK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=70,
            defence=40,
            special_attack=35,
            special_defence=40,
        ),
        categories=[
            Categories.MAMMAL, Categories.FANTASY, Categories.DOG,
        ],
        num_legs=2,
        supported_abilities=[Abilities.STEADFAST, Abilities.INNER_FOCUS],
    ),
    PokemonGen4.LUCARIO: Pokemon(
        name=PokemonGen4.LUCARIO,
        gen=4,
        types=[Types.FIGHTING, Types.STEEL],
        evolves_to=[],
        colors=[Colors.BLUE, Colors.BLACK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=110,
            defence=70,
            special_attack=115,
            special_defence=70,
        ),
        categories=[
            Categories.MAMMAL, Categories.FANTASY, Categories.DOG,
        ],
        num_legs=2,
        supported_abilities=[Abilities.STEADFAST, Abilities.INNER_FOCUS],
    ),
    PokemonGen4.HIPPOPOTAS: Pokemon(
        name=PokemonGen4.HIPPOPOTAS,
        gen=4,
        types=[Types.GROUND],
        evolves_to=[
            Evolution(name=PokemonGen4.HIPPOWDON)
        ],
        colors=[Colors.BROWN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=72,
            defence=78,
            special_attack=38,
            special_defence=42,
        ),
        categories=[
            Categories.MAMMAL, Categories.WATERMON
        ],
        num_legs=4,
        supported_abilities=[Abilities.SAND_STREAM],
    ),
    PokemonGen4.HIPPOWDON: Pokemon(
        name=PokemonGen4.HIPPOWDON,
        gen=4,
        types=[Types.GROUND],
        evolves_to=[],
        colors=[Colors.BROWN, Colors.BLACK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=112,
            defence=118,
            special_attack=68,
            special_defence=72,
        ),
        categories=[
            Categories.MAMMAL, Categories.WATERMON
        ],
        num_legs=4,
        supported_abilities=[Abilities.SAND_STREAM],
    ),
    PokemonGen4.SKORUPI: Pokemon(
        name=PokemonGen4.SKORUPI,
        gen=4,
        types=[Types.POISON, Types.BUG],
        evolves_to=[
            Evolution(name=PokemonGen4.DRAPION)
        ],
        colors=[Colors.PURPLE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=50,
            defence=90,
            special_attack=30,
            special_defence=55,
        ),
        categories=[
            Categories.BUG
        ],
        num_legs=4,
        supported_abilities=[Abilities.BATTLE_ARMOR, Abilities.SNIPER],
    ),
    PokemonGen4.DRAPION: Pokemon(
        name=PokemonGen4.DRAPION,
        gen=4,
        types=[Types.POISON, Types.DARK],
        evolves_to=[],
        colors=[Colors.PURPLE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=90,
            defence=110,
            special_attack=60,
            special_defence=75,
        ),
        categories=[
            Categories.BUG
        ],
        num_legs=4,
        supported_abilities=[Abilities.BATTLE_ARMOR, Abilities.SNIPER],
    ),
    PokemonGen4.CROAGUNK: Pokemon(
        name=PokemonGen4.CROAGUNK,
        gen=4,
        types=[Types.POISON, Types.FIGHTING],
        evolves_to=[
            Evolution(name=PokemonGen4.TOXICROAK)
        ],
        colors=[Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=61,
            defence=40,
            special_attack=61,
            special_defence=40,
        ),
        categories=[
            Categories.REPTILE, Categories.WATERMON, Categories.FROG
        ],
        num_legs=2,
        supported_abilities=[Abilities.ANTICIPATION, Abilities.DRY_SKIN],
    ),
    PokemonGen4.TOXICROAK: Pokemon(
        name=PokemonGen4.TOXICROAK,
        gen=4,
        types=[Types.POISON, Types.FIGHTING],
        evolves_to=[],
        colors=[Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=106,
            defence=65,
            special_attack=86,
            special_defence=65,
        ),
        categories=[
            Categories.REPTILE, Categories.WATERMON, Categories.FROG
        ],
        num_legs=2,
        supported_abilities=[Abilities.ANTICIPATION, Abilities.DRY_SKIN],
    ),
    PokemonGen4.CARNIVINE: Pokemon(
        name=PokemonGen4.CARNIVINE,
        gen=4,
        types=[Types.GRASS],
        evolves_to=[],
        colors=[Colors.GREEN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=100,
            defence=72,
            special_attack=90,
            special_defence=72,
        ),
        categories=[
            Categories.PLANT, Categories.PREHISTORIC
        ],
        num_legs=0,
        supported_abilities=[Abilities.LEVITATE],
    ),
    PokemonGen4.FINNEON: Pokemon(
        name=PokemonGen4.FINNEON,
        gen=4,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen4.LUMINEON)
        ],
        colors=[Colors.BLUE, Colors.PINK, Colors.BLACK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=49,
            defence=56,
            special_attack=49,
            special_defence=61,
        ),
        categories=[
            Categories.WATERMON, Categories.FISH, Categories.FOOD
        ],
        num_legs=0,
        supported_abilities=[Abilities.SWIFT_SWIM, Abilities.STORM_DRAIN],
    ),
    PokemonGen4.LUMINEON: Pokemon(
        name=PokemonGen4.LUMINEON,
        gen=4,
        types=[Types.WATER],
        evolves_to=[],
        colors=[Colors.BLUE, Colors.BLACK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=69,
            defence=76,
            special_attack=69,
            special_defence=86,
        ),
        categories=[
            Categories.WATERMON, Categories.FISH, Categories.FOOD
        ],
        num_legs=0,
        supported_abilities=[Abilities.SWIFT_SWIM, Abilities.STORM_DRAIN],
    ),
    PokemonGen4.MANTYKE: Pokemon(
        name=PokemonGen4.MANTYKE,
        gen=4,
        types=[Types.WATER, Types.FLYING],
        evolves_to=[
            Evolution(name=PokemonGen4.MANTINE, special_information="Second Gym. With Remoraid in party")
        ],
        colors=[Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=20,
            defence=50,
            special_attack=60,
            special_defence=120,
        ),
        categories=[
            Categories.WATERMON,
            Categories.FISH,
            Categories.WING,
            Categories.FOOD,
        ],
        num_legs=0,
        supported_abilities=[Abilities.SWIFT_SWIM, Abilities.WATER_ABSORB],
    ),
    PokemonGen4.SNOVER: Pokemon(
        name=PokemonGen4.SNOVER,
        gen=4,
        types=[Types.GRASS, Types.ICE],
        evolves_to=[
            Evolution(name=PokemonGen4.ABOMASNOW)
        ],
        colors=[Colors.GREEN, Colors.WHITE, Colors.BROWN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=62,
            defence=50,
            special_attack=62,
            special_defence=60,
        ),
        categories=[
            Categories.PLANT, Categories.FANTASY
        ],
        num_legs=2,
        supported_abilities=[Abilities.SNOW_WARNING],
    ),
    PokemonGen4.ABOMASNOW: Pokemon(
        name=PokemonGen4.ABOMASNOW,
        gen=4,
        types=[Types.GRASS, Types.ICE],
        evolves_to=[],
        colors=[Colors.GREEN, Colors.WHITE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=92,
            defence=75,
            special_attack=92,
            special_defence=85,
        ),
        categories=[
            Categories.PLANT, Categories.FANTASY
        ],
        num_legs=2,
        supported_abilities=[Abilities.SNOW_WARNING],
    ),
    PokemonGen4.WEAVILE: Pokemon(
        name=PokemonGen4.WEAVILE,
        gen=4,
        types=[Types.DARK, Types.ICE],
        evolves_to=[],
        colors=[Colors.PURPLE, Colors.RED],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=120,
            defence=65,
            special_attack=45,
            special_defence=85,
        ),
        categories=[
            Categories.MAMMAL
        ],
        num_legs=2,
        supported_abilities=[Abilities.PRESSURE],
    ),
    PokemonGen4.MAGNEZONE: Pokemon(
        name=PokemonGen4.MAGNEZONE,
        gen=4,
        types=[Types.ELECTRIC],
        evolves_to=[],
        colors=[Colors.GRAY, Colors.BLUE, Colors.RED],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=70,
            defence=115,
            special_attack=130,
            special_defence=90,
        ),
        categories=[
            Categories.ITEM
        ],
        num_legs=0,
        supported_abilities=[Abilities.MAGNET_PULL, Abilities.STURDY],
    ),
    PokemonGen4.LICKILICKY: Pokemon(
        name=PokemonGen4.LICKILICKY,
        gen=4,
        types=[Types.NORMAL],
        evolves_to=[],
        colors=[Colors.PINK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=85,
            defence=95,
            special_attack=80,
            special_defence=95,
        ),
        categories=[
            Categories.FROG
        ],
        num_legs=2,
        supported_abilities=[Abilities.OWN_TEMPO, Abilities.OBLIVIOUS],
    ),
    PokemonGen4.RHYPERIOR: Pokemon(
        name=PokemonGen4.RHYPERIOR,
        gen=4,
        types=[Types.GROUND, Types.ROCK],
        evolves_to=[],
        colors=[Colors.GRAY, Colors.ORANGE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=140,
            defence=130,
            special_attack=55,
            special_defence=55,
        ),
        categories=[
            Categories.MAMMAL, Categories.WATERMON
        ],
        num_legs=2,
        supported_abilities=[Abilities.LIGHTNING_ROD, Abilities.SOLID_ROCK],
    ),
    PokemonGen4.TANGROWTH: Pokemon(
        name=PokemonGen4.TANGROWTH,
        gen=4,
        types=[Types.GRASS],
        evolves_to=[],
        colors=[Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=100,
            defence=125,
            special_attack=110,
            special_defence=50,
        ),
        categories=[
            Categories.PLANT, Categories.FOOD
        ],
        num_legs=2,
        supported_abilities=[Abilities.CHLOROPHYLL, Abilities.LEAF_GUARD],
    ),
    PokemonGen4.ELECTIVIRE: Pokemon(
        name=PokemonGen4.ELECTIVIRE,
        gen=4,
        types=[Types.ELECTRIC],
        evolves_to=[],
        colors=[Colors.YELLOW, Colors.BLACK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=123,
            defence=67,
            special_attack=95,
            special_defence=85,
        ),
        categories=[
            Categories.MAMMAL, Categories.HUMAN
        ],
        num_legs=2,
        supported_abilities=[Abilities.MOTOR_DRIVE],
    ),
    PokemonGen4.MAGMORTAR: Pokemon(
        name=PokemonGen4.MAGMORTAR,
        gen=4,
        types=[Types.FIRE],
        evolves_to=[],
        colors=[Colors.RED, Colors.YELLOW],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=95,
            defence=67,
            special_attack=125,
            special_defence=95,
        ),
        categories=[
            Categories.WING, Categories.BIRD, Categories.FOOD, Categories.WATERMON, Categories.DUCK
        ],
        num_legs=2,
        supported_abilities=[Abilities.FLAME_BODY],
    ),
    PokemonGen4.TOGEKISS: Pokemon(
        name=PokemonGen4.TOGEKISS,
        gen=4,
        types=[Types.NORMAL, Types.FLYING],
        evolves_to=[],
        colors=[Colors.WHITE, Colors.BLUE, Colors.RED],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=50,
            defence=95,
            special_attack=120,
            special_defence=115,
        ),
        categories=[
            Categories.WING, Categories.ITEM
        ],
        num_legs=2,
        supported_abilities=[Abilities.HUSTLE, Abilities.SERENE_GRACE],
    ),
    PokemonGen4.YANMEGA: Pokemon(
        name=PokemonGen4.YANMEGA,
        gen=4,
        types=[Types.BUG, Types.FLYING],
        evolves_to=[],
        colors=[Colors.GREEN, Colors.RED],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=76,
            defence=86,
            special_attack=116,
            special_defence=56,
        ),
        categories=[
            Categories.WING, Categories.BUG, Categories.DRAGON, Categories.WATERMON,
        ],
        num_legs=6,
        supported_abilities=[Abilities.SPEED_BOOST, Abilities.TINTED_LENS],
    ),
    PokemonGen4.LEAFEON: Pokemon(
        name=PokemonGen4.LEAFEON,
        gen=4,
        types=[Types.GRASS],
        evolves_to=[],
        colors=[Colors.GREEN, Colors.YELLOW],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=110,
            defence=130,
            special_attack=60,
            special_defence=65,
        ),
        categories=[
            Categories.PLANT, Categories.MAMMAL, Categories.DOG
        ],
        num_legs=4,
        supported_abilities=[Abilities.LEAF_GUARD],
    ),
    PokemonGen4.GLACEON: Pokemon(
        name=PokemonGen4.GLACEON,
        gen=4,
        types=[Types.ICE],
        evolves_to=[],
        colors=[Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=60,
            defence=110,
            special_attack=130,
            special_defence=95,
        ),
        categories=[
            Categories.MAMMAL, Categories.DOG
        ],
        num_legs=4,
        supported_abilities=[Abilities.SNOW_CLOAK],
    ),
    PokemonGen4.GLISCOR: Pokemon(
        name=PokemonGen4.GLISCOR,
        gen=4,
        types=[Types.GROUND, Types.FLYING],
        evolves_to=[],
        colors=[Colors.PURPLE, Colors.BLACK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=95,
            defence=125,
            special_attack=45,
            special_defence=75,
        ),
        categories=[
            Categories.BUG, Categories.FANTASY
        ],
        num_legs=2,
        supported_abilities=[Abilities.HYPER_CUTTER, Abilities.SAND_VEIL],
    ),
    PokemonGen4.MAMOSWINE: Pokemon(
        name=PokemonGen4.MAMOSWINE,
        gen=4,
        types=[Types.ICE, Types.GROUND],
        evolves_to=[],
        colors=[Colors.BROWN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=130,
            defence=80,
            special_attack=70,
            special_defence=60,
        ),
        categories=[
            Categories.PREHISTORIC, Categories.MAMMAL, Categories.FOOD, Categories.PIG
        ],
        num_legs=4,
        supported_abilities=[Abilities.OBLIVIOUS, Abilities.SNOW_CLOAK],
    ),
    PokemonGen4.PORYGON_Z: Pokemon(
        name=PokemonGen4.PORYGON_Z,
        gen=4,
        types=[Types.NORMAL],
        evolves_to=[],
        colors=[Colors.PINK, Colors.BLUE],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=80,
            defence=70,
            special_attack=135,
            special_defence=75,
        ),
        categories=[
            Categories.ITEM
        ],
        num_legs=0,
        supported_abilities=[Abilities.ADAPTABILITY, Abilities.DOWNLOAD],
    ),
    PokemonGen4.GALLADE: Pokemon(
        name=PokemonGen4.GALLADE,
        gen=4,
        types=[Types.PSYCHIC, Types.FIGHTING],
        evolves_to=[],
        colors=[Colors.WHITE, Colors.GREEN],
        supported_genders=[Genders.MALE],
        stats=Stats(
            attack=125,
            defence=65,
            special_attack=65,
            special_defence=115,
        ),
        categories=[
            Categories.MAMMAL, Categories.FANTASY, Categories.HUMAN
        ],
        num_legs=2,
        supported_abilities=[Abilities.STEADFAST, Abilities.SHARPNESS],
    ),
    PokemonGen4.PROBOPASS: Pokemon(
        name=PokemonGen4.PROBOPASS,
        gen=4,
        types=[Types.ROCK, Types.STEEL],
        evolves_to=[],
        colors=[Colors.BLUE, Colors.RED],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=55,
            defence=145,
            special_attack=75,
            special_defence=150,
        ),
        categories=[
            Categories.PREHISTORIC, Categories.ITEM, Categories.FANTASY
        ],
        num_legs=0,
        supported_abilities=[Abilities.STURDY, Abilities.MAGNET_PULL],
    ),
    PokemonGen4.DUSKNOIR: Pokemon(
        name=PokemonGen4.DUSKNOIR,
        gen=4,
        types=[Types.GHOST],
        evolves_to=[],
        colors=[Colors.GRAY, Colors.BLACK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=100,
            defence=135,
            special_attack=65,
            special_defence=135,
        ),
        categories=[
            Categories.FANTASY, Categories.MAMMAL, Categories.HUMAN
        ],
        num_legs=0,
        supported_abilities=[Abilities.PRESSURE],
    ),
    PokemonGen4.FROSLASS: Pokemon(
        name=PokemonGen4.FROSLASS,
        gen=4,
        types=[Types.ICE, Types.GHOST],
        evolves_to=[],
        colors=[Colors.WHITE, Colors.BLUE],
        supported_genders=[Genders.FEMALE],
        stats=Stats(
            attack=80,
            defence=70,
            special_attack=80,
            special_defence=70,
        ),
        categories=[
            Categories.MAMMAL, Categories.ITEM, Categories.FANTASY, Categories.HUMAN
        ],
        num_legs=0,
        supported_abilities=[Abilities.SNOW_CLOAK],
    ),
    PokemonGen4.ROTOM: Pokemon(
        name=PokemonGen4.ROTOM,
        gen=4,
        types=[Types.ELECTRIC, Types.GHOST],
        evolves_to=[],
        colors=[Colors.ORANGE],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=50,
            defence=77,
            special_attack=95,
            special_defence=75,
        ),
        categories=[
            Categories.ITEM
        ],
        num_legs=0,
        supported_abilities=[Abilities.LEVITATE],
    ),
    PokemonGen4.HEAT_ROTOM: Pokemon(
        name=PokemonGen4.HEAT_ROTOM,
        gen=4,
        types=[Types.ELECTRIC, Types.FIRE],
        evolves_to=[],
        colors=[Colors.RED, Colors.ORANGE],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=65,
            defence=107,
            special_attack=105,
            special_defence=107,
        ),
        categories=[
            Categories.ITEM
        ],
        num_legs=0,
        supported_abilities=[Abilities.LEVITATE],
        form="Heat",
        base_name=PokemonGen4.ROTOM,
    ),
    PokemonGen4.WASH_ROTOM: Pokemon(
        name=PokemonGen4.WASH_ROTOM,
        gen=4,
        types=[Types.ELECTRIC, Types.WATER],
        evolves_to=[],
        colors=[Colors.BLUE, Colors.ORANGE],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=65,
            defence=107,
            special_attack=105,
            special_defence=107,
        ),
        categories=[
            Categories.ITEM
        ],
        num_legs=0,
        supported_abilities=[Abilities.LEVITATE],
        form="Wash",
        base_name=PokemonGen4.ROTOM,
    ),
    PokemonGen4.FROST_ROTOM: Pokemon(
        name=PokemonGen4.FROST_ROTOM,
        gen=4,
        types=[Types.ELECTRIC, Types.ICE],
        evolves_to=[],
        colors=[Colors.PURPLE, Colors.ORANGE],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=65,
            defence=107,
            special_attack=105,
            special_defence=107,
        ),
        categories=[
            Categories.ITEM
        ],
        num_legs=0,
        supported_abilities=[Abilities.LEVITATE],
        form="Frost",
        base_name=PokemonGen4.ROTOM,
    ),
    PokemonGen4.FAN_ROTOM: Pokemon(
        name=PokemonGen4.FAN_ROTOM,
        gen=4,
        types=[Types.ELECTRIC, Types.FLYING],
        evolves_to=[],
        colors=[Colors.YELLOW, Colors.ORANGE],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=65,
            defence=107,
            special_attack=105,
            special_defence=107,
        ),
        categories=[
            Categories.ITEM
        ],
        num_legs=0,
        supported_abilities=[Abilities.LEVITATE],
        form="Fan",
        base_name=PokemonGen4.ROTOM,
    ),
    PokemonGen4.MOW_ROTOM: Pokemon(
        name=PokemonGen4.MOW_ROTOM,
        gen=4,
        types=[Types.ELECTRIC, Types.GRASS],
        evolves_to=[],
        colors=[Colors.GREEN, Colors.ORANGE],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=65,
            defence=107,
            special_attack=105,
            special_defence=107,
        ),
        categories=[
            Categories.ITEM
        ],
        num_legs=0,
        supported_abilities=[Abilities.LEVITATE],
        form="Mow",
        base_name=PokemonGen4.ROTOM,
    ),
    PokemonGen4.UXIE: Pokemon(
        name=PokemonGen4.UXIE,
        gen=4,
        types=[Types.PSYCHIC],
        evolves_to=[],
        colors=[Colors.BLUE, Colors.YELLOW],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=75,
            defence=130,
            special_attack=75,
            special_defence=130,
        ),
        categories=[
            Categories.FANTASY
        ],
        num_legs=2,
        supported_abilities=[Abilities.LEVITATE],
    ),
    PokemonGen4.MESPRIT: Pokemon(
        name=PokemonGen4.MESPRIT,
        gen=4,
        types=[Types.PSYCHIC],
        evolves_to=[],
        colors=[Colors.PINK, Colors.BLUE],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=105,
            defence=105,
            special_attack=105,
            special_defence=105,
        ),
        categories=[
            Categories.FANTASY
        ],
        num_legs=2,
        supported_abilities=[Abilities.LEVITATE],
    ),
    PokemonGen4.AZELF: Pokemon(
        name=PokemonGen4.AZELF,
        gen=4,
        types=[Types.PSYCHIC],
        evolves_to=[],
        colors=[Colors.BLUE],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=125,
            defence=70,
            special_attack=125,
            special_defence=70,
        ),
        categories=[
            Categories.FANTASY
        ],
        num_legs=2,
        supported_abilities=[Abilities.LEVITATE],
    ),
    PokemonGen4.DIALGA: Pokemon(
        name=PokemonGen4.DIALGA,
        gen=4,
        types=[Types.STEEL, Types.DRAGON],
        evolves_to=[],
        colors=[Colors.GRAY, Colors.BLUE],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=120,
            defence=120,
            special_attack=150,
            special_defence=100,
        ),
        categories=[
            Categories.PREHISTORIC, Categories.DRAGON, Categories.FANTASY
        ],
        num_legs=4,
        supported_abilities=[Abilities.PRESSURE],
    ),
    PokemonGen4.PALKIA: Pokemon(
        name=PokemonGen4.PALKIA,
        gen=4,
        types=[Types.WATER, Types.DRAGON],
        evolves_to=[],
        colors=[Colors.GRAY, Colors.PINK],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=120,
            defence=100,
            special_attack=150,
            special_defence=120,
        ),
        categories=[
            Categories.PREHISTORIC, Categories.DRAGON, Categories.FANTASY
        ],
        num_legs=4,
        supported_abilities=[Abilities.PRESSURE],
    ),
    PokemonGen4.HEATRAN: Pokemon(
        name=PokemonGen4.HEATRAN,
        gen=4,
        types=[Types.FIRE, Types.STEEL],
        evolves_to=[],
        colors=[Colors.RED, Colors.GRAY],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=90,
            defence=106,
            special_attack=130,
            special_defence=106,
        ),
        categories=[
            Categories.BUG, Categories.REPTILE, Categories.FROG, Categories.ITEM, Categories.TURTLE
        ],
        num_legs=4,
        supported_abilities=[Abilities.FLASH_FIRE],
    ),
    PokemonGen4.REGIGIGAS: Pokemon(
        name=PokemonGen4.REGIGIGAS,
        gen=4,
        types=[Types.NORMAL],
        evolves_to=[],
        colors=[Colors.WHITE, Colors.YELLOW],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=160,
            defence=110,
            special_attack=80,
            special_defence=110,
        ),
        categories=[
            Categories.ITEM
        ],
        num_legs=2,
        supported_abilities=[Abilities.SLOW_START],
    ),
    PokemonGen4.GIRATINA: Pokemon(
        name=PokemonGen4.GIRATINA,
        gen=4,
        types=[Types.GHOST, Types.DRAGON],
        evolves_to=[],
        colors=[Colors.GRAY, Colors.BLACK, Colors.RED, Colors.YELLOW],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=100,
            defence=120,
            special_attack=100,
            special_defence=120,
        ),
        categories=[
            Categories.DRAGON, Categories.FANTASY, Categories.ITEM
        ],
        num_legs=4,
        supported_abilities=[Abilities.PRESSURE],
    ),
    PokemonGen4.GIRATINA_ORIGIN: Pokemon(
        name=PokemonGen4.GIRATINA_ORIGIN,
        gen=4,
        types=[Types.GHOST, Types.DRAGON],
        evolves_to=[],
        colors=[Colors.GRAY, Colors.BLACK, Colors.RED, Colors.YELLOW],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=120,
            defence=100,
            special_attack=120,
            special_defence=100,
        ),
        categories=[
            Categories.DRAGON, Categories.FANTASY, Categories.ITEM
        ],
        num_legs=0,
        supported_abilities=[Abilities.LEVITATE],
        form="Origin",
        base_name=PokemonGen4.GIRATINA,
    ),
    PokemonGen4.CRESSELIA: Pokemon(
        name=PokemonGen4.CRESSELIA,
        gen=4,
        types=[Types.PSYCHIC],
        evolves_to=[],
        colors=[Colors.BLUE, Colors.YELLOW, Colors.PINK],
        supported_genders=[Genders.FEMALE],
        stats=Stats(
            attack=70,
            defence=110,
            special_attack=75,
            special_defence=120,
        ),
        categories=[
            Categories.WING, Categories.BIRD, Categories.WATERMON, Categories.FOOD, Categories.DUCK
        ],
        num_legs=0,
        supported_abilities=[Abilities.LEVITATE],
    ),
    PokemonGen4.PHIONE: Pokemon(
        name=PokemonGen4.PHIONE,
        gen=4,
        types=[Types.WATER],
        evolves_to=[],
        colors=[Colors.BLUE],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=80,
            defence=80,
            special_attack=80,
            special_defence=80,
        ),
        categories=[
            Categories.WATERMON, Categories.BUG, 
        ],
        num_legs=0,
        supported_abilities=[Abilities.HYDRATION],
    ),
    PokemonGen4.MANAPHY: Pokemon(
        name=PokemonGen4.MANAPHY,
        gen=4,
        types=[Types.WATER],
        evolves_to=[],
        colors=[Colors.BLUE],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=100,
            defence=100,
            special_attack=100,
            special_defence=100,
        ),
        categories=[
            Categories.WATERMON, Categories.BUG, 
        ],
        num_legs=2,
        supported_abilities=[Abilities.HYDRATION],
    ),
    PokemonGen4.DARKRAI: Pokemon(
        name=PokemonGen4.DARKRAI,
        gen=4,
        types=[Types.DARK],
        evolves_to=[],
        colors=[Colors.BLACK, Colors.RED],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=90,
            defence=90,
            special_attack=135,
            special_defence=90,
        ),
        categories=[
            Categories.MAMMAL, Categories.FANTASY, Categories.HUMAN
        ],
        num_legs=0,
        supported_abilities=[Abilities.BAD_DREAMS],
    ),
    PokemonGen4.SHAYMIN_LAND: Pokemon(
        name=PokemonGen4.SHAYMIN_LAND,
        gen=4,
        types=[Types.GRASS],
        evolves_to=[],
        colors=[Colors.GREEN, Colors.WHITE],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=100,
            defence=100,
            special_attack=100,
            special_defence=100,
        ),
        categories=[
            Categories.MAMMAL, Categories.PLANT, Categories.MOUSE, Categories.RODENT
        ],
        num_legs=4,
        supported_abilities=[Abilities.NATURAL_CURE],
        form="Land",
        base_name="Shaymin",
    ),
    PokemonGen4.SHAYMIN_SKY: Pokemon(
        name=PokemonGen4.SHAYMIN_SKY,
        gen=4,
        types=[Types.GRASS, Types.FLYING],
        evolves_to=[],
        colors=[Colors.GREEN, Colors.WHITE],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=103,
            defence=75,
            special_attack=120,
            special_defence=75,
        ),
        categories=[
            Categories.MAMMAL, Categories.PLANT, Categories.DOG
        ],
        num_legs=4,
        supported_abilities=[Abilities.SERENE_GRACE],
        form="Sky",
        base_name="Shaymin",
    ),
    PokemonGen4.ARCEUS: Pokemon(
        name=PokemonGen4.ARCEUS,
        gen=4,
        types=[Types.NORMAL],
        evolves_to=[],
        colors=[Colors.WHITE, Colors.YELLOW],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=120,
            defence=120,
            special_attack=120,
            special_defence=120,
        ),
        categories=[
            Categories.ITEM, 
            Categories.FANTASY, 
            Categories.HUMAN, 
            Categories.PREHISTORIC, 
            Categories.MAMMAL,
            Categories.CATTLE,
            Categories.HORSE,
        ],
        num_legs=4,
        supported_abilities=[Abilities.MULTITYPE],
    ),
}

# PokemonGen4.: Pokemon(
#         name=PokemonGen4.,
#         gen=4,
#         types=[Types.],
#         evolves_to=[
#             Evolution(name=PokemonGen4.)
#         ],
#         colors=[Colors.],
#         supported_genders=[Genders.MALE, Genders.FEMALE],
#         stats=Stats(
#             attack=0,
#             defence=0,
#             special_attack=0,
#             special_defence=0,
#         ),
#         categories=[
#             Categories.
#         ],
#         num_legs=2,
#         supported_abilities=[Abilities.],
#     ),

NAME_TO_POKEMON.update(_GEN4_POKEMONS)