"""Generation 3 Pokemon data module."""

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


class PokemonGen3:
    """Generation 1, 2 and 3 Pokémon names.
    
    This class contains string constants for all Pokémon from Generation 1 and 2.
    The names are stored in their proper English localization format, including:
    - Proper capitalization (e.g., "Charizard", not "charizard")
    - Special characters (e.g., "Farfetch'd", "Mr. Mime", "Ho-oh")
    - Gender-specific forms (e.g., "Nidoran-F", "Nidoran-M")
    - Special naming conventions (e.g., "Porygon2")
    """
    
    BULBASAUR = "Bulbasaur"
    IVYSAUR = "Ivysaur"
    VENUSAUR = "Venusaur"
    CHARMANDER = "Charmander"
    CHARMELEON = "Charmeleon"
    CHARIZARD = "Charizard"
    SQUIRTLE = "Squirtle"
    WARTORTLE = "Wartortle"
    BLASTOISE = "Blastoise"
    CATERPIE = "Caterpie"
    METAPOD = "Metapod"
    BUTTERFREE = "Butterfree"
    WEEDLE = "Weedle"
    KAKUNA = "Kakuna"
    BEEDRILL = "Beedrill"
    PIDGEY = "Pidgey"
    PIDGEOTTO = "Pidgeotto"
    PIDGEOT = "Pidgeot"
    RATTATA = "Rattata"
    RATICATE = "Raticate"
    SPEAROW = "Spearow"
    FEAROW = "Fearow"
    EKANS = "Ekans"
    ARBOK = "Arbok"
    PIKACHU = "Pikachu"
    RAICHU = "Raichu"
    SANDSHREW = "Sandshrew"
    SANDSLASH = "Sandslash"
    NIDORAN_F = "Nidoran-F"
    NIDORINA = "Nidorina"
    NIDOQUEEN = "Nidoqueen"
    NIDORAN_M = "Nidoran-M"
    NIDORINO = "Nidorino"
    NIDOKING = "Nidoking"
    CLEFAIRY = "Clefairy"
    CLEFABLE = "Clefable"
    VULPIX = "Vulpix"
    NINETALES = "Ninetales"
    JIGGLYPUFF = "Jigglypuff"
    WIGGLYTUFF = "Wigglytuff"
    ZUBAT = "Zubat"
    GOLBAT = "Golbat"
    ODDISH = "Oddish"
    GLOOM = "Gloom"
    VILEPLUME = "Vileplume"
    PARAS = "Paras"
    PARASECT = "Parasect"
    VENONAT = "Venonat"
    VENOMOTH = "Venomoth"
    DIGLETT = "Diglett"
    DUGTRIO = "Dugtrio"
    MEOWTH = "Meowth"
    PERSIAN = "Persian"
    PSYDUCK = "Psyduck"
    GOLDUCK = "Golduck"
    MANKEY = "Mankey"
    PRIMEAPE = "Primeape"
    GROWLITHE = "Growlithe"
    ARCANINE = "Arcanine"
    POLIWAG = "Poliwag"
    POLIWHIRL = "Poliwhirl"
    POLIWRATH = "Poliwrath"
    ABRA = "Abra"
    KADABRA = "Kadabra"
    ALAKAZAM = "Alakazam"
    MACHOP = "Machop"
    MACHOKE = "Machoke"
    MACHAMP = "Machamp"
    BELLSPROUT = "Bellsprout"
    WEEPINBELL = "Weepinbell"
    VICTREEBEL = "Victreebel"
    TENTACOOL = "Tentacool"
    TENTACRUEL = "Tentacruel"
    GEODUDE = "Geodude"
    GRAVELER = "Graveler"
    GOLEM = "Golem"
    PONYTA = "Ponyta"
    RAPIDASH = "Rapidash"
    SLOWPOKE = "Slowpoke"
    SLOWBRO = "Slowbro"
    MAGNEMITE = "Magnemite"
    MAGNETON = "Magneton"
    FARFETCHD = "Farfetch'd"
    DODUO = "Doduo"
    DODRIO = "Dodrio"
    SEEL = "Seel"
    DEWGONG = "Dewgong"
    GRIMER = "Grimer"
    MUK = "Muk"
    SHELLDER = "Shellder"
    CLOYSTER = "Cloyster"
    GASTLY = "Gastly"
    HAUNTER = "Haunter"
    GENGAR = "Gengar"
    ONIX = "Onix"
    DROWZEE = "Drowzee"
    HYPNO = "Hypno"
    KRABBY = "Krabby"
    KINGLER = "Kingler"
    VOLTORB = "Voltorb"
    ELECTRODE = "Electrode"
    EXEGGCUTE = "Exeggcute"
    EXEGGUTOR = "Exeggutor"
    CUBONE = "Cubone"
    MAROWAK = "Marowak"
    HITMONLEE = "Hitmonlee"
    HITMONCHAN = "Hitmonchan"
    LICKITUNG = "Lickitung"
    KOFFING = "Koffing"
    WEEZING = "Weezing"
    RHYHORN = "Rhyhorn"
    RHYDON = "Rhydon"
    CHANSEY = "Chansey"
    TANGELA = "Tangela"
    KANGASKHAN = "Kangaskhan"
    HORSEA = "Horsea"
    SEADRA = "Seadra"
    GOLDEEN = "Goldeen"
    SEAKING = "Seaking"
    STARYU = "Staryu"
    STARMIE = "Starmie"
    MR_MIME = "Mr. Mime"
    SCYTHER = "Scyther"
    JYNX = "Jynx"
    ELECTABUZZ = "Electabuzz"
    MAGMAR = "Magmar"
    PINSIR = "Pinsir"
    TAUROS = "Tauros"
    MAGIKARP = "Magikarp"
    GYARADOS = "Gyarados"
    LAPRAS = "Lapras"
    DITTO = "Ditto"
    EEVEE = "Eevee"
    VAPOREON = "Vaporeon"
    JOLTEON = "Jolteon"
    FLAREON = "Flareon"
    PORYGON = "Porygon"
    OMANYTE = "Omanyte"
    OMASTAR = "Omastar"
    KABUTO = "Kabuto"
    KABUTOPS = "Kabutops"
    AERODACTYL = "Aerodactyl"
    SNORLAX = "Snorlax"
    ARTICUNO = "Articuno"
    ZAPDOS = "Zapdos"
    MOLTRES = "Moltres"
    DRATINI = "Dratini"
    DRAGONAIR = "Dragonair"
    DRAGONITE = "Dragonite"
    MEWTWO = "Mewtwo"
    MEW = "Mew"
    CHIKORITA = "Chikorita"
    BAYLEEF = "Bayleef"
    MEGANIUM = "Meganium"
    CYNDAQUIL = "Cyndaquil"
    QUILAVA = "Quilava"
    TYPHLOSION = "Typhlosion"
    TOTODILE = "Totodile"
    CROCONAW = "Croconaw"
    FERALIGATR = "Feraligatr"
    SENTRET = "Sentret"
    FURRET = "Furret"
    HOOTHOOT = "Hoothoot"
    NOCTOWL = "Noctowl"
    LEDYBA = "Ledyba"
    LEDIAN = "Ledian"
    SPINARAK = "Spinarak"
    ARIADOS = "Ariados"
    CROBAT = "Crobat"
    CHINCHOU = "Chinchou"
    LANTURN = "Lanturn"
    PICHU = "Pichu"
    CLEFFA = "Cleffa"
    IGGLYBUFF = "Igglybuff"
    TOGEPI = "Togepi"
    TOGETIC = "Togetic"
    NATU = "Natu"
    XATU = "Xatu"
    MAREEP = "Mareep"
    FLAAFFY = "Flaaffy"
    AMPHAROS = "Ampharos"
    BELLOSSOM = "Bellossom"
    MARILL = "Marill"
    AZUMARILL = "Azumarill"
    SUDOWOODO = "Sudowoodo"
    POLITOED = "Politoed"
    HOPPIP = "Hoppip"
    SKIPLOOM = "Skiploom"
    JUMPLUFF = "Jumpluff"
    AIPOM = "Aipom"
    SUNKERN = "Sunkern"
    SUNFLORA = "Sunflora"
    YANMA = "Yanma"
    WOOPER = "Wooper"
    QUAGSIRE = "Quagsire"
    ESPEON = "Espeon"
    UMBREON = "Umbreon"
    MURKROW = "Murkrow"
    SLOWKING = "Slowking"
    MISDREAVUS = "Misdreavus"
    UNOWN = "Unown"
    WOBBUFFET = "Wobbuffet"
    GIRAFARIG = "Girafarig"
    PINECO = "Pineco"
    FORRETRESS = "Forretress"
    DUNSPARCE = "Dunsparce"
    GLIGAR = "Gligar"
    STEELIX = "Steelix"
    SNUBBULL = "Snubbull"
    GRANBULL = "Granbull"
    QWILFISH = "Qwilfish"
    SCIZOR = "Scizor"
    SHUCKLE = "Shuckle"
    HERACROSS = "Heracross"
    SNEASEL = "Sneasel"
    TEDDIURSA = "Teddiursa"
    URSARING = "Ursaring"
    SLUGMA = "Slugma"
    MAGCARGO = "Magcargo"
    SWINUB = "Swinub"
    PILOSWINE = "Piloswine"
    CORSOLA = "Corsola"
    REMORAID = "Remoraid"
    OCTILLERY = "Octillery"
    DELIBIRD = "Delibird"
    MANTINE = "Mantine"
    SKARMORY = "Skarmory"
    HOUNDOUR = "Houndour"
    HOUNDOOM = "Houndoom"
    KINGDRA = "Kingdra"
    PHANPY = "Phanpy"
    DONPHAN = "Donphan"
    PORYGON2 = "Porygon2"
    STANTLER = "Stantler"
    SMEARGLE = "Smeargle"
    TYROGUE = "Tyrogue"
    HITMONTOP = "Hitmontop"
    SMOOCHUM = "Smoochum"
    ELEKID = "Elekid"
    MAGBY = "Magby"
    MILTANK = "Miltank"
    BLISSEY = "Blissey"
    RAIKOU = "Raikou"
    ENTEI = "Entei"
    SUICUNE = "Suicune"
    LARVITAR = "Larvitar"
    PUPITAR = "Pupitar"
    TYRANITAR = "Tyranitar"
    LUGIA = "Lugia"
    HO_OH = "Ho-oh"
    CELEBI = "Celebi"
    

NAME_TO_POKEMON = {
    PokemonGen3.BULBASAUR: Pokemon(
        name=PokemonGen3.BULBASAUR,
        gen=2,  # All Pokemon in gen2.py should be gen=2 as this represents their Gen 2 data
        types=[Types.GRASS, Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen3.IVYSAUR)
        ],
        colors=[Colors.GREEN, Colors.BLUE],
        categories=[
            Categories.PREHISTORIC,
            Categories.PLANT,
            Categories.FROG
        ],
        num_legs=4,
        stats=Stats(
            attack=49,
            defence=49,
            special_attack=65,
            special_defence=65,
        ),
        supported_abilities=[Abilities.OVERGROW],
    ),
    PokemonGen3.IVYSAUR: Pokemon(
        name=PokemonGen3.IVYSAUR,
        gen=2,  # All Pokemon in gen2.py should be gen=2 as this represents their Gen 2 data
        types=[Types.GRASS, Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen3.VENUSAUR)
        ],
        colors=[Colors.BLUE, Colors.GREEN, Colors.PINK],
        categories=[
            Categories.PREHISTORIC,
            Categories.PLANT,
            Categories.FROG
        ],
        num_legs=4,
        stats=Stats(
            attack=62,
            defence=63,
            special_attack=80,
            special_defence=80,
        ),
        supported_abilities=[Abilities.OVERGROW],
    ),
    PokemonGen3.VENUSAUR: Pokemon(
        name=PokemonGen3.VENUSAUR,
        gen=1,  # Gen 1 Pokemon
        types=[Types.GRASS, Types.POISON],
        colors=[Colors.BLUE, Colors.GREEN, Colors.PINK],
        categories=[
            Categories.PREHISTORIC,
            Categories.PLANT,
            Categories.FROG
        ],
        num_legs=4,
        stats=Stats(
            attack=82,
            defence=83,
            special_attack=100,
            special_defence=100,
        ),
        supported_abilities=[Abilities.OVERGROW],
    ),
    PokemonGen3.CHARMANDER: Pokemon(
        name=PokemonGen3.CHARMANDER,
        gen=2,
        types=[Types.FIRE],
        evolves_to=[
            Evolution(name=PokemonGen3.CHARMELEON)
        ],
        colors=[Colors.ORANGE],
        categories=[
            Categories.PREHISTORIC,
            Categories.REPTILE,
            Categories.DRAGON,
        ],
        num_legs=2,
        stats=Stats(
            attack=39,
            defence=52,
            special_attack=43,
            special_defence=60,
        ),
        supported_abilities=[Abilities.BLAZE],
    ),
    PokemonGen3.CHARMELEON: Pokemon(
        name=PokemonGen3.CHARMELEON,
        gen=2,
        types=[Types.FIRE],
        evolves_to=[
            Evolution(name=PokemonGen3.CHARIZARD)
        ],
        colors=[Colors.RED],
        categories=[
            Categories.PREHISTORIC,
            Categories.REPTILE,
            Categories.DRAGON,
        ],
        num_legs=2,
        stats=Stats(
            attack=58,
            defence=64,
            special_attack=58,
            special_defence=80,
        ),
        supported_abilities=[Abilities.BLAZE],
    ),
    PokemonGen3.CHARIZARD: Pokemon(
        name=PokemonGen3.CHARIZARD,
        gen=2,
        types=[Types.FIRE, Types.FLYING],
        colors=[Colors.ORANGE],
        categories=[
            Categories.PREHISTORIC,
            Categories.REPTILE,
            Categories.DRAGON,
            Categories.WING,
        ],
        num_legs=2,
        stats=Stats(
            attack=84,
            defence=78,
            special_attack=78,
            special_defence=109,
        ),
        supported_abilities=[Abilities.BLAZE],
    ),
    PokemonGen3.SQUIRTLE: Pokemon(
        name=PokemonGen3.SQUIRTLE,
        gen=2,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen3.WARTORTLE)
        ],
        colors=[Colors.BLUE, Colors.BROWN],
        categories=[
            Categories.PREHISTORIC,
            Categories.REPTILE,
            Categories.WATERMON,
            Categories.FOOD,
            Categories.TURTLE,
        ],
        num_legs=2,
        stats=Stats(
            attack=59,
            defence=63,
            special_attack=58,
            special_defence=67,
        ),
        supported_abilities=[Abilities.TORRENT],
    ),
    PokemonGen3.WARTORTLE: Pokemon(
        name=PokemonGen3.WARTORTLE,
        gen=2,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen3.BLASTOISE)
        ],
        colors=[Colors.BLUE, Colors.BROWN],
        categories=[
            Categories.PREHISTORIC,
            Categories.REPTILE,
            Categories.WATERMON,
            Categories.FOOD,
            Categories.TURTLE,
        ],
        num_legs=2,
        stats=Stats(
            attack=83,
            defence=80,
            special_attack=80,
            special_defence=100,
        ),
        supported_abilities=[Abilities.TORRENT],
    ),
    PokemonGen3.BLASTOISE: Pokemon(
        name=PokemonGen3.BLASTOISE,
        gen=2,
        types=[Types.WATER],
        colors=[Colors.BLUE, Colors.BROWN],
        categories=[
            Categories.PREHISTORIC,
            Categories.REPTILE,
            Categories.WATERMON,
            Categories.FOOD,
            Categories.TURTLE,
            Categories.WEAPON,
        ],
        num_legs=2,
        stats=Stats(
            attack=100,
            defence=110,
            special_attack=95,
            special_defence=80,
        ),
        supported_abilities=[Abilities.TORRENT],
    ),
    PokemonGen3.CATERPIE: Pokemon(
        name=PokemonGen3.CATERPIE,
        gen=2,
        types=[Types.BUG],
        evolves_to=[
            Evolution(name=PokemonGen3.METAPOD)
        ],
        colors=[Colors.GREEN],
        categories=[
            Categories.BUG,
        ],
        num_legs=6,
        stats=Stats(
            attack=30,
            defence=35,
            special_attack=45,
            special_defence=20,
        ),
        supported_abilities=[Abilities.SHIELD_DUST],
    ),
    PokemonGen3.METAPOD: Pokemon(
        name=PokemonGen3.METAPOD,
        gen=2,
        types=[Types.BUG],
        evolves_to=[
            Evolution(name=PokemonGen3.BUTTERFREE)
        ],
        colors=[Colors.GREEN],
        categories=[
            Categories.BUG,
        ],
        num_legs=0,
        stats=Stats(
            attack=70,
            defence=60,
            special_attack=65,
            special_defence=55,
        ),
        supported_abilities=[Abilities.SHED_SKIN],
    ),
    PokemonGen3.BUTTERFREE: Pokemon(
        name=PokemonGen3.BUTTERFREE,
        gen=2,
        types=[Types.BUG, Types.FLYING],
        colors=[Colors.WHITE, Colors.PURPLE],
        categories=[
            Categories.BUG,
            Categories.WING,
        ],
        num_legs=2,
        stats=Stats(
            attack=80,
            defence=55,
            special_attack=65,
            special_defence=75,
        ),
        supported_abilities=[Abilities.COMPOUND_EYES],
    ),
    PokemonGen3.WEEDLE: Pokemon(
        name=PokemonGen3.WEEDLE,
        gen=2,
        types=[Types.BUG, Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen3.KAKUNA)
        ],
        colors=[Colors.BROWN],
        categories=[
            Categories.BUG,
            Categories.WEAPON,
        ],
        num_legs=14,
        stats=Stats(
            attack=75,
            defence=35,
            special_attack=55,
            special_defence=25,
        ),
        supported_abilities=[Abilities.SHIELD_DUST],
    ),
    PokemonGen3.KAKUNA: Pokemon(
        name=PokemonGen3.KAKUNA,
        gen=2,
        types=[Types.BUG, Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen3.BEEDRILL)
        ],
        colors=[Colors.YELLOW],
        categories=[
            Categories.BUG,
        ],
        num_legs=0,
        stats=Stats(
            attack=80,
            defence=55,
            special_attack=65,
            special_defence=75,
        ),
        supported_abilities=[Abilities.SHED_SKIN],
    ),
    PokemonGen3.BEEDRILL: Pokemon(
        name=PokemonGen3.BEEDRILL,
        gen=2,
        types=[Types.BUG, Types.POISON],
        colors=[Colors.YELLOW, Colors.BLACK],
        categories=[
            Categories.BUG,
            Categories.WEAPON,
            Categories.WING,
        ],
        num_legs=2,
        stats=Stats(
            attack=100,
            defence=65,
            special_attack=60,
            special_defence=70,
        ),
        supported_abilities=[Abilities.SWARM],
    ),
    PokemonGen3.PIDGEY: Pokemon(
        name=PokemonGen3.PIDGEY,
        gen=2,
        types=[Types.NORMAL, Types.FLYING],
        evolves_to=[
            Evolution(name=PokemonGen3.PIDGEOTTO)
        ],
        colors=[Colors.BROWN, Colors.WHITE],
        categories=[
            Categories.WING,
            Categories.FOOD,
            Categories.BIRD,
        ],
        num_legs=2,
        stats=Stats(
            attack=45,
            defence=40,
            special_attack=35,
            special_defence=35,
        ),
        supported_abilities=[Abilities.KEEN_EYE, Abilities.TANGLED_FEET],
    ),
    PokemonGen3.PIDGEOTTO: Pokemon(
        name=PokemonGen3.PIDGEOTTO,
        gen=2,
        types=[Types.NORMAL, Types.FLYING],
        evolves_to=[
            Evolution(name=PokemonGen3.PIDGEOT)
        ],
        colors=[Colors.BROWN, Colors.WHITE],
        categories=[
            Categories.WING,
            Categories.FOOD,
            Categories.BIRD,
        ],
        num_legs=2,
        stats=Stats(
            attack=60,
            defence=55,
            special_attack=50,
            special_defence=50,
        ),
        supported_abilities=[Abilities.KEEN_EYE, Abilities.TANGLED_FEET],
    ),
    PokemonGen3.PIDGEOT: Pokemon(
        name=PokemonGen3.PIDGEOT,
        gen=2,
        types=[Types.NORMAL, Types.FLYING],
        colors=[Colors.BROWN, Colors.WHITE],
        categories=[
            Categories.WING,
            Categories.FOOD,
            Categories.BIRD,
        ],
        num_legs=2,
        stats=Stats(
            attack=83,
            defence=80,
            special_attack=75,
            special_defence=70,
        ),
        supported_abilities=[Abilities.KEEN_EYE, Abilities.TANGLED_FEET],
    ),
    PokemonGen3.RATTATA: Pokemon(
        name=PokemonGen3.RATTATA,
        gen=2,
        types=[Types.NORMAL],
        evolves_to=[
            Evolution(name=PokemonGen3.RATICATE)
        ],
        colors=[Colors.PURPLE, Colors.WHITE],
        categories=[
            Categories.RODENT,
            Categories.MOUSE,
        ],
        num_legs=4,
        stats=Stats(
            attack=55,
            defence=35,
            special_attack=30,
            special_defence=40,
        ),
        supported_abilities=[Abilities.RUN_AWAY, Abilities.GUTS],
    ),
    PokemonGen3.RATICATE: Pokemon(
        name=PokemonGen3.RATICATE,
        gen=2,
        types=[Types.NORMAL],
        colors=[Colors.BROWN, Colors.WHITE],
        categories=[
            Categories.RODENT,
            Categories.MOUSE,
        ],
        num_legs=4,
        stats=Stats(
            attack=75,
            defence=55,
            special_attack=40,
            special_defence=50,
        ),
        supported_abilities=[Abilities.RUN_AWAY, Abilities.GUTS],
    ),
    PokemonGen3.SPEAROW: Pokemon(
        name=PokemonGen3.SPEAROW,
        gen=2,
        types=[Types.NORMAL, Types.FLYING],
        evolves_to=[
            Evolution(name=PokemonGen3.FEAROW)
        ],
        colors=[Colors.BROWN, Colors.RED, Colors.WHITE],
        categories=[
            Categories.WING,
            Categories.FOOD,
            Categories.BIRD,
        ],
        num_legs=2,
        stats=Stats(
            attack=65,
            defence=60,
            special_attack=60,
            special_defence=70,
        ),
        supported_abilities=[Abilities.KEEN_EYE],
    ),
    PokemonGen3.FEAROW: Pokemon(
        name=PokemonGen3.FEAROW,
        gen=2,
        types=[Types.NORMAL, Types.FLYING],
        colors=[Colors.BROWN, Colors.RED, Colors.WHITE],
        categories=[
            Categories.WING,
            Categories.FOOD,
            Categories.BIRD,
        ],
        num_legs=2,
        stats=Stats(
            attack=85,
            defence=65,
            special_attack=60,
            special_defence=70,
        ),
        supported_abilities=[Abilities.KEEN_EYE],
    ),
    PokemonGen3.EKANS: Pokemon(
        name=PokemonGen3.EKANS,
        gen=2,
        types=[Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen3.ARBOK)
        ],
        colors=[Colors.PURPLE, Colors.WHITE],
        categories=[
            Categories.REPTILE,
            Categories.FOOD,
            Categories.SNAKE,
        ],
        num_legs=0,
        stats=Stats(
            attack=60,
            defence=60,
            special_attack=40,
            special_defence=40,
        ),
        supported_abilities=[Abilities.INTIMIDATE, Abilities.SHED_SKIN],
    ),
    PokemonGen3.ARBOK: Pokemon(
        name=PokemonGen3.ARBOK,
        gen=2,
        types=[Types.POISON],
        colors=[Colors.PURPLE],
        categories=[
            Categories.REPTILE,
            Categories.FOOD,
            Categories.SNAKE,
        ],
        num_legs=0,
        stats=Stats(
            attack=85,
            defence=60,
            special_attack=60,
            special_defence=70,
        ),
        supported_abilities=[Abilities.INTIMIDATE, Abilities.SHED_SKIN],
    ),
    PokemonGen3.PIKACHU: Pokemon(
        name=PokemonGen3.PIKACHU,
        gen=2,
        types=[Types.ELECTRIC],
        evolves_to=[
            Evolution(name=PokemonGen3.RAICHU, level=41, evolution_type=EvolutionType.STONE, item=Item.THUNDER_STONE)
        ],
        colors=[Colors.YELLOW],
        categories=[
            Categories.RODENT,
            Categories.MOUSE,
        ],
        num_legs=4,
        stats=Stats(
            attack=50,
            defence=40,
            special_attack=40,
            special_defence=40,
        ),
        supported_abilities=[Abilities.STATIC],
    ),
    PokemonGen3.RAICHU: Pokemon(
        name=PokemonGen3.RAICHU,
        gen=2,
        types=[Types.ELECTRIC],
        colors=[Colors.YELLOW, Colors.ORANGE],
        categories=[
            Categories.RODENT,
            Categories.MOUSE,
        ],
        num_legs=2,
        stats=Stats(
            attack=90,
            defence=55,
            special_attack=65,
            special_defence=85,
        ),
        supported_abilities=[Abilities.STATIC],
    ),
    PokemonGen3.SANDSHREW: Pokemon(
        name=PokemonGen3.SANDSHREW,
        gen=2,
        types=[Types.GROUND],
        evolves_to=[
            Evolution(name=PokemonGen3.SANDSLASH)
        ],
        colors=[Colors.YELLOW, Colors.WHITE],
        categories=[
            Categories.MAMMAL,
            Categories.MOUSE,
            Categories.RODENT,
        ],
        num_legs=2,
        stats=Stats(
            attack=50,
            defence=95,
            special_attack=40,
            special_defence=50,
        ),
        supported_abilities=[Abilities.SAND_VEIL],
    ),
    PokemonGen3.SANDSLASH: Pokemon(
        name=PokemonGen3.SANDSLASH,
        gen=2,
        types=[Types.GROUND],
        colors=[Colors.YELLOW, Colors.BROWN],
        categories=[
            Categories.MAMMAL,
            Categories.MOUSE,
            Categories.RODENT,
        ],
        num_legs=2,
        stats=Stats(
            attack=75,
            defence=100,
            special_attack=60,
            special_defence=70,
        ),
        supported_abilities=[Abilities.SAND_VEIL],
    ),
    PokemonGen3.NIDORAN_F: Pokemon(
        name=PokemonGen3.NIDORAN_F,
        gen=2,
        types=[Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen3.NIDORINA)
        ],
        colors=[Colors.BLUE],
        categories=[
            Categories.PREHISTORIC,
            Categories.MAMMAL,
            Categories.FOOD,
            Categories.BUNNY,
        ],
        num_legs=4,
        stats=Stats(
            attack=50,
            defence=25,
            special_attack=25,
            special_defence=35,
        ),
        supported_abilities=[Abilities.POISON_POINT, Abilities.RIVALRY],
    ),
    PokemonGen3.NIDORINA: Pokemon(
        name=PokemonGen3.NIDORINA,
        gen=2,
        types=[Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen3.NIDOQUEEN, level=19, evolution_type=EvolutionType.STONE, item=Item.MOON_STONE)
        ],
        colors=[Colors.BLUE],
        categories=[
            Categories.PREHISTORIC,
            Categories.MAMMAL,
            Categories.FOOD,
            Categories.BUNNY,
        ],
        num_legs=4,
        stats=Stats(
            attack=70,
            defence=55,
            special_attack=55,
            special_defence=45,
        ),
        supported_abilities=[Abilities.POISON_POINT, Abilities.RIVALRY],
    ),
    PokemonGen3.NIDOQUEEN: Pokemon(
        name=PokemonGen3.NIDOQUEEN,
        gen=2,
        types=[Types.POISON, Types.GROUND],
        colors=[Colors.BLUE, Colors.WHITE],
        categories=[
            Categories.PREHISTORIC,
            Categories.MAMMAL,
            Categories.FOOD,
            Categories.BUNNY,
        ],
        num_legs=2,
        stats=Stats(
            attack=90,
            defence=85,
            special_attack=75,
            special_defence=85,
        ),
        supported_abilities=[Abilities.POISON_POINT, Abilities.RIVALRY],
    ),
    PokemonGen3.NIDORAN_M: Pokemon(
        name=PokemonGen3.NIDORAN_M,
        gen=2,
        types=[Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen3.NIDORINO)
        ],
        colors=[Colors.PURPLE],
        categories=[
            Categories.PREHISTORIC,
            Categories.MAMMAL,
            Categories.FOOD,
            Categories.BUNNY,
        ],
        num_legs=4,
        stats=Stats(
            attack=50,
            defence=25,
            special_attack=25,
            special_defence=35,
        ),
        supported_abilities=[Abilities.POISON_POINT, Abilities.RIVALRY],
    ),
    PokemonGen3.NIDORINO: Pokemon(
        name=PokemonGen3.NIDORINO,
        gen=2,
        types=[Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen3.NIDOKING, level=19, evolution_type=EvolutionType.STONE, item=Item.MOON_STONE)
        ],
        colors=[Colors.PURPLE],
        categories=[
            Categories.PREHISTORIC,
            Categories.MAMMAL,
            Categories.FOOD,
            Categories.BUNNY,
        ],
        num_legs=4,
        stats=Stats(
            attack=70,
            defence=55,
            special_attack=55,
            special_defence=45,
        ),
        supported_abilities=[Abilities.POISON_POINT, Abilities.RIVALRY],
    ),
    PokemonGen3.NIDOKING: Pokemon(
        name=PokemonGen3.NIDOKING,
        gen=2,
        types=[Types.POISON, Types.GROUND],
        colors=[Colors.PURPLE],
        categories=[
            Categories.PREHISTORIC,
            Categories.MAMMAL,
            Categories.FOOD,
            Categories.BUNNY,
            Categories.WEAPON,
        ],
        num_legs=2,
        stats=Stats(
            attack=90,
            defence=85,
            special_attack=75,
            special_defence=85,
        ),
        supported_abilities=[Abilities.POISON_POINT, Abilities.RIVALRY],
    ),
    PokemonGen3.CLEFAIRY: Pokemon(
        name=PokemonGen3.CLEFAIRY,
        gen=2,
        types=[Types.NORMAL],
        evolves_to=[
            Evolution(name=PokemonGen3.CLEFABLE, level=34, item=Item.MOON_STONE, evolution_type=EvolutionType.STONE)
        ],
        colors=[Colors.PINK],
        categories=[
            Categories.FANTASY,
            Categories.MAMMAL,
            Categories.HUMAN,
        ],
        num_legs=2,
        stats=Stats(
            attack=70,
            defence=45,
            special_attack=48,
            special_defence=60,
        ),
        supported_abilities=[Abilities.CUTE_CHARM, Abilities.MAGIC_GUARD],
    ),
    PokemonGen3.CLEFABLE: Pokemon(
        name=PokemonGen3.CLEFABLE,
        gen=2,
        types=[Types.NORMAL],
        colors=[Colors.PINK],
        categories=[
            Categories.FANTASY,
            Categories.MAMMAL,
            Categories.HUMAN,
            Categories.WING,
        ],
        num_legs=2,
        stats=Stats(
            attack=95,
            defence=75,
            special_attack=80,
            special_defence=100,
        ),
        supported_abilities=[Abilities.CUTE_CHARM, Abilities.MAGIC_GUARD],
    ),
    PokemonGen3.VULPIX: Pokemon(
        name=PokemonGen3.VULPIX,
        gen=2,
        types=[Types.FIRE],
        evolves_to=[
            Evolution(name=PokemonGen3.NINETALES, level=31, evolution_type=EvolutionType.STONE, item=Item.FIRE_STONE)
        ],
        colors=[Colors.BROWN],
        categories=[
            Categories.MAMMAL,
            Categories.DOG,
        ],
        num_legs=4,
        stats=Stats(
            attack=38,
            defence=41,
            special_attack=40,
            special_defence=50,
        ),
        supported_abilities=[Abilities.FLASH_FIRE],
    ),
    PokemonGen3.NINETALES: Pokemon(
        name=PokemonGen3.NINETALES,
        gen=2,
        types=[Types.FIRE],
        colors=[Colors.YELLOW],
        categories=[
            Categories.MAMMAL,
            Categories.DOG,
        ],
        num_legs=4,
        stats=Stats(
            attack=73,
            defence=76,
            special_attack=75,
            special_defence=81,
        ),
        supported_abilities=[Abilities.FLASH_FIRE],
    ),
    PokemonGen3.JIGGLYPUFF: Pokemon(
        name=PokemonGen3.JIGGLYPUFF,
        gen=2,
        types=[Types.NORMAL],
        evolves_to=[
            Evolution(name=PokemonGen3.WIGGLYTUFF, level=34, evolution_type=EvolutionType.STONE, item=Item.MOON_STONE)
        ],
        colors=[Colors.PINK],
        categories=[
            Categories.ITEM,
            Categories.FOOD,
        ],
        num_legs=2,
        stats=Stats(
            attack=115,
            defence=45,
            special_attack=20,
            special_defence=20,
        ),
        supported_abilities=[Abilities.CUTE_CHARM, Abilities.COMPETITIVE],
    ),
    PokemonGen3.WIGGLYTUFF: Pokemon(
        name=PokemonGen3.WIGGLYTUFF,
        gen=2,
        types=[Types.NORMAL],
        colors=[Colors.PINK],
        categories=[
            Categories.ITEM,
            Categories.FOOD,
        ],
        num_legs=2,
        stats=Stats(
            attack=100,
            defence=50,
            special_attack=50,
            special_defence=75,
        ),
        supported_abilities=[Abilities.CUTE_CHARM, Abilities.COMPETITIVE],
    ),
    PokemonGen3.ZUBAT: Pokemon(
        name=PokemonGen3.ZUBAT,
        gen=2,
        types=[Types.POISON, Types.FLYING],
        evolves_to=[
            Evolution(name=PokemonGen3.GOLBAT)
        ],
        colors=[Colors.BLUE],
        categories=[
            Categories.WING,
            Categories.MAMMAL,
        ],
        num_legs=0,
        stats=Stats(
            attack=40,
            defence=30,
            special_attack=50,
            special_defence=55,
        ),
        supported_abilities=[Abilities.INNER_FOCUS],
    ),
    PokemonGen3.GOLBAT: Pokemon(
        name=PokemonGen3.GOLBAT,
        gen=2,
        types=[Types.POISON, Types.FLYING],
        evolves_to=[Evolution(name=PokemonGen3.CROBAT, evolution_type=EvolutionType.FRIENDSHIP,)],
        colors=[Colors.BLUE],
        categories=[
            Categories.WING,
            Categories.MAMMAL,
        ],
        num_legs=2,
        stats=Stats(
            attack=75,
            defence=80,
            special_attack=70,
            special_defence=90,
        ),
        supported_abilities=[Abilities.INNER_FOCUS],
    ),
    PokemonGen3.ODDISH: Pokemon(
        name=PokemonGen3.ODDISH,
        gen=2,
        types=[Types.GRASS, Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen3.GLOOM)
        ],
        colors=[Colors.BLUE, Colors.GREEN],
        categories=[
            Categories.PLANT,
            Categories.FOOD,
        ],
        num_legs=2,
        stats=Stats(
            attack=45,
            defence=50,
            special_attack=55,
            special_defence=75,
        ),
        supported_abilities=[Abilities.CHLOROPHYLL],
    ),
    PokemonGen3.GLOOM: Pokemon(
        name=PokemonGen3.GLOOM,
        gen=2,
        types=[Types.GRASS, Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen3.VILEPLUME, level=44, evolution_type=EvolutionType.STONE, item=Item.LEAF_STONE),
            Evolution(name=PokemonGen3.BELLOSSOM, level=44, evolution_type=EvolutionType.STONE, item=Item.SUN_STONE)
        ],
        colors=[Colors.BLUE, Colors.RED],
        categories=[
            Categories.PLANT,
        ],
        num_legs=2,
        supported_abilities=[Abilities.CHLOROPHYLL],
    ),
    PokemonGen3.VILEPLUME: Pokemon(
        name=PokemonGen3.VILEPLUME,
        gen=2,
        types=[Types.GRASS, Types.POISON],
        colors=[Colors.BLUE, Colors.RED],
        categories=[
            Categories.PLANT,
        ],
        num_legs=2,
        stats=Stats(
            attack=75,
            defence=80,
            special_attack=85,
            special_defence=90,
        ),
        supported_abilities=[Abilities.CHLOROPHYLL],
    ),
    PokemonGen3.PARAS: Pokemon(
        name=PokemonGen3.PARAS,
        gen=2,
        types=[Types.BUG, Types.GRASS],
        evolves_to=[
            Evolution(name=PokemonGen3.PARASECT)
        ],
        colors=[Colors.ORANGE, Colors.RED, Colors.YELLOW],
        categories=[
            Categories.PLANT,
            Categories.CRAB,
            Categories.WATERMON,
            Categories.FOOD,
        ],
        num_legs=4,
        stats=Stats(
            attack=40,
            defence=30,
            special_attack=50,
            special_defence=55,
        ),
        supported_abilities=[Abilities.DRY_SKIN, Abilities.EFFECT_SPORE],
    ),
    PokemonGen3.PARASECT: Pokemon(
        name=PokemonGen3.PARASECT,
        gen=2,
        types=[Types.BUG, Types.GRASS],
        colors=[Colors.ORANGE, Colors.RED],
        categories=[
            Categories.PLANT,
            Categories.CRAB,
            Categories.WATERMON,
            Categories.FOOD,
        ],
        num_legs=4,
        stats=Stats(
            attack=60,
            defence=55,
            special_attack=50,
            special_defence=40,
        ),
        supported_abilities=[Abilities.EFFECT_SPORE, Abilities.DRY_SKIN],
    ),
    PokemonGen3.VENONAT: Pokemon(
        name=PokemonGen3.VENONAT,
        gen=2,
        types=[Types.BUG, Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen3.VENOMOTH)
        ],
        colors=[Colors.PURPLE, Colors.RED],
        categories=[
            Categories.BUG,
        ],
        num_legs=2,
        stats=Stats(
            attack=65,
            defence=55,
            special_attack=50,
            special_defence=40,
        ),
        supported_abilities=[Abilities.COMPOUND_EYES, Abilities.TINTED_LENS],
    ),
    PokemonGen3.VENOMOTH: Pokemon(
        name=PokemonGen3.VENOMOTH,
        gen=2,
        types=[Types.BUG, Types.POISON],
        colors=[Colors.PURPLE],
        categories=[
            Categories.BUG,
            Categories.WING,
        ],
        num_legs=0,
        stats=Stats(
            attack=65,
            defence=55,
            special_attack=50,
            special_defence=40,
        ),
        supported_abilities=[Abilities.SHIELD_DUST, Abilities.TINTED_LENS],
    ),
    PokemonGen3.DIGLETT: Pokemon(
        name=PokemonGen3.DIGLETT,
        gen=2,
        types=[Types.GROUND],
        evolves_to=[
            Evolution(name=PokemonGen3.DUGTRIO)
        ],
        colors=[Colors.BROWN],
        categories=[
            Categories.BUG,
            Categories.REPTILE,
        ],
        num_legs=0,
        stats=Stats(
            attack=35,
            defence=100,
            special_attack=50,
            special_defence=50,
        ),
        supported_abilities=[Abilities.SAND_VEIL, Abilities.ARENA_TRAP],
    ),
    PokemonGen3.DUGTRIO: Pokemon(
        name=PokemonGen3.DUGTRIO,
        gen=2,
        types=[Types.GROUND],
        colors=[Colors.BROWN],
        categories=[
            Categories.BUG,
            Categories.REPTILE,
        ],
        num_legs=0,
        stats=Stats(
            attack=85,
            defence=90,
            special_attack=80,
            special_defence=70,
        ),
        supported_abilities=[Abilities.SAND_VEIL, Abilities.ARENA_TRAP],
    ),
    PokemonGen3.MEOWTH: Pokemon(
        name=PokemonGen3.MEOWTH,
        gen=2,
        types=[Types.NORMAL],
        evolves_to=[
            Evolution(name=PokemonGen3.PERSIAN)
        ],
        colors=[Colors.WHITE],
        categories=[
            Categories.MAMMAL,
            Categories.CAT,
        ],
        num_legs=4,
        stats=Stats(
            attack=45,
            defence=50,
            special_attack=43,
            special_defence=38,
        ),
        supported_abilities=[Abilities.TECHNICIAN, Abilities.PICKUP],
    ),
    PokemonGen3.PERSIAN: Pokemon(
        name=PokemonGen3.PERSIAN,
        gen=2,
        types=[Types.NORMAL],
        colors=[Colors.WHITE],
        categories=[
            Categories.MAMMAL,
            Categories.CAT,
        ],
        num_legs=4,
        stats=Stats(
            attack=65,
            defence=60,
            special_attack=60,
            special_defence=70,
        ),
        supported_abilities=[Abilities.LIMBER, Abilities.TECHNICIAN],
    ),
    PokemonGen3.PSYDUCK: Pokemon(
        name=PokemonGen3.PSYDUCK,
        gen=2,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen3.GOLDUCK)
        ],
        colors=[Colors.YELLOW],
        categories=[
            Categories.WING,
            Categories.BIRD,
            Categories.WATERMON,
            Categories.FOOD,
            Categories.DUCK,
        ],
        num_legs=2,
        stats=Stats(
            attack=85,
            defence=73,
            special_attack=70,
            special_defence=70,
        ),
        supported_abilities=[Abilities.DAMP, Abilities.CLOUD_NINE],
    ),
    PokemonGen3.GOLDUCK: Pokemon(
        name=PokemonGen3.GOLDUCK,
        gen=2,
        types=[Types.WATER],
        colors=[Colors.BLUE],
        categories=[
            Categories.WING,
            Categories.BIRD,
            Categories.WATERMON,
            Categories.FOOD,
            Categories.DUCK,
        ],
        num_legs=2,
        stats=Stats(
            attack=85,
            defence=73,
            special_attack=70,
            special_defence=70,
        ),
        supported_abilities=[Abilities.DAMP, Abilities.CLOUD_NINE],
    ),
    PokemonGen3.MANKEY: Pokemon(
        name=PokemonGen3.MANKEY,
        gen=2,
        types=[Types.FIGHTING],
        evolves_to=[
            Evolution(name=PokemonGen3.PRIMEAPE)
        ],
        colors=[Colors.BROWN],
        categories=[
            Categories.MAMMAL,
            Categories.APE,
        ],
        num_legs=2,
        stats=Stats(
            attack=40,
            defence=35,
            special_attack=30,
            special_defence=20,
        ),
        supported_abilities=[Abilities.VITAL_SPIRIT, Abilities.ANGER_POINT],
    ),
    PokemonGen3.PRIMEAPE: Pokemon(
        name=PokemonGen3.PRIMEAPE,
        gen=2,
        types=[Types.FIGHTING],
        colors=[Colors.BROWN],
        categories=[
            Categories.MAMMAL,
            Categories.APE,
        ],
        num_legs=2,
        stats=Stats(
            attack=65,
            defence=50,
            special_attack=52,
            special_defence=50,
        ),
        supported_abilities=[Abilities.VITAL_SPIRIT, Abilities.ANGER_POINT],
    ),
    PokemonGen3.GROWLITHE: Pokemon(
        name=PokemonGen3.GROWLITHE,
        gen=2,
        types=[Types.FIRE],
        evolves_to=[
            Evolution(name=PokemonGen3.ARCANINE, level=50, evolution_type=EvolutionType.STONE, item=Item.FIRE_STONE)
        ],
        colors=[Colors.ORANGE, Colors.BLACK, Colors.WHITE],
        categories=[
            Categories.MAMMAL,
            Categories.DOG,
        ],
        num_legs=4,
        stats=Stats(
            attack=65,
            defence=50,
            special_attack=52,
            special_defence=50,
        ),
        supported_abilities=[Abilities.INTIMIDATE, Abilities.FLASH_FIRE],
    ),
    PokemonGen3.ARCANINE: Pokemon(
        name=PokemonGen3.ARCANINE,
        gen=2,
        types=[Types.FIRE],
        colors=[Colors.ORANGE, Colors.BLACK, Colors.WHITE],
        categories=[
            Categories.MAMMAL,
            Categories.DOG,
        ],
        num_legs=4,
        stats=Stats(
            attack=90,
            defence=70,
            special_attack=80,
            special_defence=70,
        ),
        supported_abilities=[Abilities.INTIMIDATE, Abilities.FLASH_FIRE],
    ),
    PokemonGen3.POLIWAG: Pokemon(
        name=PokemonGen3.POLIWAG,
        gen=2,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen3.POLIWHIRL)
        ],
        colors=[Colors.BLUE, Colors.WHITE],
        categories=[
            Categories.PREHISTORIC,
            Categories.WATERMON,
            Categories.REPTILE,
            Categories.FROG,
        ],
        num_legs=2, 
        stats=Stats(
            attack=40,
            defence=40,
            special_attack=35,
            special_defence=50,
        ),
        supported_abilities=[Abilities.WATER_ABSORB, Abilities.DAMP],
    ),
    PokemonGen3.POLIWHIRL: Pokemon(
        name=PokemonGen3.POLIWHIRL,
        gen=2,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen3.POLIWRATH, level=35, evolution_type=EvolutionType.STONE, item=Item.WATER_STONE),
            Evolution(name=PokemonGen3.POLITOED, evolution_type=EvolutionType.TRADE, should_hold=True, item=Item.KINGS_ROCK)
        ],
        colors=[Colors.BLUE, Colors.WHITE],
        categories=[
            Categories.PREHISTORIC,
            Categories.WATERMON,
            Categories.REPTILE,
            Categories.FROG,
        ],
        num_legs=2,
        stats=Stats(
            attack=65,
            defence=65,
            special_attack=60,
            special_defence=50,
        ),
        supported_abilities=[Abilities.WATER_ABSORB, Abilities.DAMP],
    ),
    PokemonGen3.POLIWRATH: Pokemon(
        name=PokemonGen3.POLIWRATH,
        gen=2,
        types=[Types.WATER, Types.FIGHTING],
        colors=[Colors.BLUE, Colors.WHITE],
        categories=[
            Categories.PREHISTORIC,
            Categories.WATERMON,
            Categories.REPTILE,
            Categories.FROG,
        ],
        num_legs=2,
        stats=Stats(
            attack=65,
            defence=65,
            special_attack=60,
            special_defence=50,
        ),
        supported_abilities=[Abilities.WATER_ABSORB, Abilities.DAMP],
    ),
    PokemonGen3.ABRA: Pokemon(
        name=PokemonGen3.ABRA,
        gen=2,
        types=[Types.PSYCHIC],
        evolves_to=[
            Evolution(name=PokemonGen3.KADABRA)
        ],
        colors=[Colors.YELLOW, Colors.BROWN],
        categories=[
            Categories.MAMMAL,
            Categories.APE,
        ],
        num_legs=2,
        stats=Stats(
            attack=25,
            defence=20,
            special_attack=15,
            special_defence=90,
        ),
        supported_abilities=[Abilities.SYNCHRONIZE, Abilities.INNER_FOCUS],
    ),
    PokemonGen3.KADABRA: Pokemon(
        name=PokemonGen3.KADABRA,
        gen=2,
        types=[Types.PSYCHIC],
        evolves_to=[
            Evolution(name=PokemonGen3.ALAKAZAM, evolution_type=EvolutionType.TRADE)
        ],
        colors=[Colors.YELLOW, Colors.BROWN],
        categories=[
            Categories.MAMMAL,
            Categories.APE,
        ],
        num_legs=2,
        stats=Stats(
            attack=50,
            defence=45,
            special_attack=75,
            special_defence=85,
        ),
        supported_abilities=[Abilities.SYNCHRONIZE, Abilities.INNER_FOCUS],
    ),
    PokemonGen3.ALAKAZAM: Pokemon(
        name=PokemonGen3.ALAKAZAM,
        gen=2,
        types=[Types.PSYCHIC],
        colors=[Colors.YELLOW, Colors.BROWN],
        categories=[
            Categories.MAMMAL,
            Categories.APE,
        ],
        num_legs=2,
        stats=Stats(
            attack=55,
            defence=50,
            special_attack=45,
            special_defence=135,
        ),
        supported_abilities=[Abilities.SYNCHRONIZE, Abilities.INNER_FOCUS],
    ),
    PokemonGen3.MACHOP: Pokemon(
        name=PokemonGen3.MACHOP,
        gen=2,
        types=[Types.FIGHTING],
        evolves_to=[
            Evolution(name=PokemonGen3.MACHOKE)
        ],
        colors=[Colors.GRAY],
        categories=[
            Categories.MAMMAL,
            Categories.HUMAN,
        ],
        num_legs=2,
        stats=Stats(
            attack=70,
            defence=80,
            special_attack=50,
            special_defence=35,
        ),
        supported_abilities=[Abilities.GUTS, Abilities.NO_GUARD],
    ),
    PokemonGen3.MACHOKE: Pokemon(
        name=PokemonGen3.MACHOKE,
        gen=2,
        types=[Types.FIGHTING],
        evolves_to=[
            Evolution(name=PokemonGen3.MACHAMP, evolution_type=EvolutionType.TRADE)
        ],
        colors=[Colors.GRAY, Colors.BLUE],
        categories=[
            Categories.MAMMAL,
            Categories.HUMAN,
        ],
        num_legs=2,
        stats=Stats(
            attack=80,
            defence=100,
            special_attack=30,
            special_defence=50,
        ),
        supported_abilities=[Abilities.GUTS, Abilities.NO_GUARD],
    ),
    PokemonGen3.MACHAMP: Pokemon(
        name=PokemonGen3.MACHAMP,
        gen=2,
        types=[Types.FIGHTING],
        colors=[Colors.BLUE, Colors.GRAY],
        categories=[
            Categories.MAMMAL,
            Categories.HUMAN,
        ],
        num_legs=2,
        stats=Stats(
            attack=90,
            defence=130,
            special_attack=45,
            special_defence=55,
        ),
        supported_abilities=[Abilities.GUTS, Abilities.NO_GUARD],
    ),
    PokemonGen3.BELLSPROUT: Pokemon(
        name=PokemonGen3.BELLSPROUT,
        gen=2,
        types=[Types.GRASS, Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen3.WEEPINBELL)
        ],
        colors=[Colors.YELLOW, Colors.GREEN],
        categories=[
            Categories.PLANT,
        ],
        num_legs=2,
        stats=Stats(
            attack=50,
            defence=75,
            special_attack=35,
            special_defence=70,
        ),
        supported_abilities=[Abilities.CHLOROPHYLL],
    ),
    PokemonGen3.WEEPINBELL: Pokemon(
        name=PokemonGen3.WEEPINBELL,
        gen=2,
        types=[Types.GRASS, Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen3.VICTREEBEL, level=54, evolution_type=EvolutionType.STONE, item=Item.LEAF_STONE)
        ],
        colors=[Colors.YELLOW, Colors.GREEN],
        categories=[
            Categories.PLANT,
        ],
        num_legs=0,
        stats=Stats(
            attack=60,
            defence=90,
            special_attack=50,
            special_defence=85,
        ),
        supported_abilities=[Abilities.CHLOROPHYLL],
    ),
    PokemonGen3.VICTREEBEL: Pokemon(
        name=PokemonGen3.VICTREEBEL,
        gen=2,
        types=[Types.GRASS, Types.POISON],
        colors=[Colors.YELLOW, Colors.GREEN],
        categories=[
            Categories.PLANT,
        ],
        num_legs=0,
        stats=Stats(
            attack=80,
            defence=105,
            special_attack=65,
            special_defence=100,
        ),
        supported_abilities=[Abilities.CHLOROPHYLL],
    ),
    PokemonGen3.TENTACOOL: Pokemon(
        name=PokemonGen3.TENTACOOL,
        gen=2,
        types=[Types.WATER, Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen3.TENTACRUEL)
        ],
        colors=[Colors.BLUE, Colors.RED],
        categories=[
            Categories.WATERMON,
            Categories.FOOD,
        ],
        num_legs=0,
        stats=Stats(
            attack=40,
            defence=35,
            special_attack=30,
            special_defence=50,
        ),
        supported_abilities=[Abilities.CLEAR_BODY, Abilities.LIQUID_OOZE],
    ),
    PokemonGen3.TENTACRUEL: Pokemon(
        name=PokemonGen3.TENTACRUEL,
        gen=2,
        types=[Types.WATER, Types.POISON],
        colors=[Colors.BLUE, Colors.RED],
        categories=[
            Categories.WATERMON,
            Categories.FOOD,
        ],
        num_legs=0,
        stats=Stats(
            attack=80,
            defence=70,
            special_attack=65,
            special_defence=80,
        ),
        supported_abilities=[Abilities.CLEAR_BODY, Abilities.LIQUID_OOZE],
    ),
    PokemonGen3.GEODUDE: Pokemon(
        name=PokemonGen3.GEODUDE,
        gen=2,
        types=[Types.ROCK, Types.GROUND],
        evolves_to=[
            Evolution(name=PokemonGen3.GRAVELER)
        ],
        colors=[Colors.GRAY],
        categories=[
            Categories.ITEM,
        ],
        num_legs=0,
        stats=Stats(
            attack=55,
            defence=85,
            special_attack=45,
            special_defence=50,
        ),
        supported_abilities=[Abilities.ROCK_HEAD, Abilities.STURDY],
    ),
    PokemonGen3.GRAVELER: Pokemon(
        name=PokemonGen3.GRAVELER,
        gen=2,
        types=[Types.ROCK, Types.GROUND],
        evolves_to=[
            Evolution(name=PokemonGen3.GOLEM, evolution_type=EvolutionType.TRADE)
        ],
        colors=[Colors.GRAY],
        categories=[
            Categories.ITEM,
        ],
        num_legs=2,
        stats=Stats(
            attack=80,
            defence=105,
            special_attack=65,
            special_defence=100,
        ),
        supported_abilities=[Abilities.ROCK_HEAD, Abilities.STURDY],
    ),
    PokemonGen3.GOLEM: Pokemon(
        name=PokemonGen3.GOLEM,
        gen=2,
        types=[Types.ROCK, Types.GROUND],
        colors=[Colors.GRAY, Colors.GREEN],
        categories=[
            Categories.REPTILE,
            Categories.FOOD,
            Categories.TURTLE,
        ],
        num_legs=2,
        stats=Stats(
            attack=80,
            defence=105,
            special_attack=65,
            special_defence=100,
        ),
        supported_abilities=[Abilities.ROCK_HEAD, Abilities.STURDY],
    ),
    PokemonGen3.PONYTA: Pokemon(
        name=PokemonGen3.PONYTA,
        gen=2,
        types=[Types.FIRE],
        evolves_to=[
            Evolution(name=PokemonGen3.RAPIDASH)
        ],
        colors=[Colors.WHITE, Colors.RED],
        categories=[
            Categories.MAMMAL,
            Categories.HORSE,
        ],
        num_legs=4,
        stats=Stats(
            attack=85,
            defence=55,
            special_attack=65,
            special_defence=60,
        ),
        supported_abilities=[Abilities.RUN_AWAY, Abilities.FLASH_FIRE],
    ),
    PokemonGen3.RAPIDASH: Pokemon(
        name=PokemonGen3.RAPIDASH,
        gen=2,
        types=[Types.FIRE],
        colors=[Colors.WHITE, Colors.RED],
        categories=[
            Categories.MAMMAL,
            Categories.HORSE,
        ],
        num_legs=4,
        stats=Stats(
            attack=85,
            defence=55,
            special_attack=65,
            special_defence=60,
        ),
        supported_abilities=[Abilities.RUN_AWAY, Abilities.FLASH_FIRE],
    ),
    PokemonGen3.SLOWPOKE: Pokemon(
        name=PokemonGen3.SLOWPOKE,
        gen=2,
        types=[Types.WATER, Types.PSYCHIC],
        evolves_to=[
            Evolution(name=PokemonGen3.SLOWBRO),
            Evolution(name=PokemonGen3.SLOWKING, evolution_type=EvolutionType.TRADE, should_hold=True, item=Item.KINGS_ROCK)
        ],
        colors=[Colors.PINK],
        categories=[
            Categories.MAMMAL,
            Categories.WATERMON,
            Categories.SLOTH,
        ],
        num_legs=4,
        stats=Stats(
            attack=30,
            defence=40,
            special_attack=50,
            special_defence=50,
        ),
        supported_abilities=[Abilities.OBLIVIOUS, Abilities.OWN_TEMPO],
    ),
    PokemonGen3.SLOWBRO: Pokemon(
        name=PokemonGen3.SLOWBRO,
        gen=2,
        types=[Types.WATER, Types.PSYCHIC],
        colors=[Colors.PINK, Colors.GRAY],
        categories=[
            Categories.MAMMAL,
            Categories.WATERMON,
            Categories.SLOTH,
        ],
        num_legs=2,
        stats=Stats(
            attack=95,
            defence=75,
            special_attack=80,
            special_defence=100,
        ),
        supported_abilities=[Abilities.OBLIVIOUS, Abilities.OWN_TEMPO],
    ),
    PokemonGen3.MAGNEMITE: Pokemon(
        name=PokemonGen3.MAGNEMITE,
        gen=2,
        types=[Types.ELECTRIC, Types.STEEL],
        evolves_to=[
            Evolution(name=PokemonGen3.MAGNETON)
        ],
        colors=[Colors.GRAY, Colors.BLUE, Colors.RED],
        categories=[
            Categories.ITEM,
        ],
        num_legs=0,
        stats=Stats(
            attack=25,
            defence=35,
            special_attack=70,
            special_defence=95,
        ),
        supported_abilities=[Abilities.MAGNET_PULL, Abilities.STURDY],
    ),
    PokemonGen3.MAGNETON: Pokemon(
        name=PokemonGen3.MAGNETON,
        gen=2,
        types=[Types.ELECTRIC, Types.STEEL],
        colors=[Colors.GRAY, Colors.BLUE, Colors.RED],
        categories=[
            Categories.ITEM,
        ],
        num_legs=0,
        stats=Stats(
            attack=50,
            defence=60,
            special_attack=95,
            special_defence=120,
        ),
        supported_abilities=[Abilities.MAGNET_PULL, Abilities.STURDY],
    ),
    PokemonGen3.FARFETCHD: Pokemon(
        name=PokemonGen3.FARFETCHD,
        gen=2,
        types=[Types.NORMAL, Types.FLYING],
        colors=[Colors.BROWN],
        categories=[
            Categories.WING,
            Categories.BIRD,
            Categories.WATERMON,
            Categories.FOOD,
            Categories.DUCK,
            Categories.WEAPON,
        ],
        num_legs=2,
        stats=Stats(
            attack=35,
            defence=85,
            special_attack=45,
            special_defence=35,
        ),
        supported_abilities=[Abilities.KEEN_EYE, Abilities.INNER_FOCUS],
    ),
    PokemonGen3.DODUO: Pokemon(
        name=PokemonGen3.DODUO,
        gen=2,
        types=[Types.NORMAL, Types.FLYING],
        evolves_to=[
            Evolution(name=PokemonGen3.DODRIO)
        ],
        colors=[Colors.BROWN],
        categories=[
            Categories.PREHISTORIC,
            Categories.WING,
            Categories.BIRD,
        ],
        num_legs=2,
        stats=Stats(
            attack=35,
            defence=85,
            special_attack=45,
            special_defence=35,
        ),
        supported_abilities=[Abilities.RUN_AWAY, Abilities.EARLY_BIRD],
    ),
    PokemonGen3.DODRIO: Pokemon(
        name=PokemonGen3.DODRIO,
        gen=2,
        types=[Types.NORMAL, Types.FLYING],
        colors=[Colors.BROWN],
        categories=[
            Categories.PREHISTORIC,
            Categories.WING,
            Categories.BIRD,
        ],
        num_legs=2,
        stats=Stats(
            attack=60,
            defence=110,
            special_attack=60,
            special_defence=60,
        ),
        supported_abilities=[Abilities.RUN_AWAY, Abilities.EARLY_BIRD],
    ),
    PokemonGen3.SEEL: Pokemon(
        name=PokemonGen3.SEEL,
        gen=2,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen3.DEWGONG)
        ],
        colors=[Colors.WHITE],
        categories=[
            Categories.MAMMAL,
            Categories.WATERMON,
            Categories.DOG,
        ],
        num_legs=0,
        stats=Stats(
            attack=65,
            defence=50,
            special_attack=35,
            special_defence=60,
        ),
        supported_abilities=[Abilities.THICK_FAT, Abilities.HYDRATION],
    ),
    PokemonGen3.DEWGONG: Pokemon(
        name=PokemonGen3.DEWGONG,
        gen=2,
        types=[Types.WATER, Types.ICE],
        colors=[Colors.WHITE],
        categories=[
            Categories.MAMMAL,
            Categories.WATERMON,
            Categories.DOG,
        ],
        num_legs=0,
        stats=Stats(
            attack=90,
            defence=65,
            special_attack=65,
            special_defence=55,
        ),
        supported_abilities=[Abilities.THICK_FAT, Abilities.HYDRATION],
    ),
    PokemonGen3.GRIMER: Pokemon(
        name=PokemonGen3.GRIMER,
        gen=2,
        types=[Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen3.MUK)
        ],
        colors=[Colors.PURPLE],
        categories=[
            Categories.ITEM,
        ],
        num_legs=0,
        stats=Stats(
            attack=80,
            defence=105,
            special_attack=65,
            special_defence=100,
        ),
        supported_abilities=[Abilities.STENCH, Abilities.STICKY_HOLD],
    ),
    PokemonGen3.MUK: Pokemon(
        name=PokemonGen3.MUK,
        gen=2,
        types=[Types.POISON],
        colors=[Colors.PURPLE],
        categories=[
            Categories.ITEM,
        ],
        num_legs=0,
        stats=Stats(
            attack=105,
            defence=105,
            special_attack=75,
            special_defence=65,
        ),
        supported_abilities=[Abilities.STENCH, Abilities.STICKY_HOLD],
    ),
    PokemonGen3.SHELLDER: Pokemon(
        name=PokemonGen3.SHELLDER,
        gen=2,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen3.CLOYSTER, level=49, evolution_type=EvolutionType.STONE, item=Item.WATER_STONE)
        ],
        colors=[Colors.PURPLE, Colors.BLACK],
        categories=[
            Categories.WATERMON,
            Categories.FOOD,
        ],
        num_legs=0,
        stats=Stats(
            attack=30,
            defence=105,
            special_attack=95,
            special_defence=55,
        ),
        supported_abilities=[Abilities.SHELL_ARMOR, Abilities.SKILL_LINK],
    ),
    PokemonGen3.CLOYSTER: Pokemon(
        name=PokemonGen3.CLOYSTER,
        gen=2,
        types=[Types.WATER, Types.ICE],
        colors=[Colors.GRAY, Colors.BLUE],
        categories=[
            Categories.WATERMON,
            Categories.FOOD,
        ],
        num_legs=0, 
        stats=Stats(
            attack=50,
            defence=95,
            special_attack=180,
            special_defence=85,
        ),
        supported_abilities=[Abilities.SHELL_ARMOR, Abilities.SKILL_LINK],
    ),
    PokemonGen3.GASTLY: Pokemon(
        name=PokemonGen3.GASTLY,
        gen=2,
        types=[Types.GHOST, Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen3.HAUNTER)
        ],
        colors=[Colors.BLACK, Colors.PURPLE],
        categories=[
            Categories.ITEM
        ],
        num_legs=0,
        stats=Stats(
            attack=30,
            defence=35,
            special_attack=30,
            special_defence=100,
        ),
        supported_abilities=[Abilities.LEVITATE],
    ),
    PokemonGen3.HAUNTER: Pokemon(
        name=PokemonGen3.HAUNTER,
        gen=2,
        types=[Types.GHOST, Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen3.GENGAR, evolution_type=EvolutionType.TRADE)
        ],
        num_legs=0,
        colors=[Colors.PURPLE],
        categories=[
            Categories.ITEM
        ],
        stats=Stats(
            attack=45,
            defence=50,
            special_attack=45,
            special_defence=100,
        ),
        supported_abilities=[Abilities.LEVITATE],
    ),
    PokemonGen3.GENGAR: Pokemon(
        name=PokemonGen3.GENGAR,
        gen=2,
        types=[Types.GHOST, Types.POISON],
        colors=[Colors.PURPLE],
        categories=[
            Categories.ITEM
        ],
        num_legs=2,
        stats=Stats(
            attack=60,
            defence=110,
            special_attack=80,
            special_defence=100,
        ),
        supported_abilities=[Abilities.CURSED_BODY],
    ),
    PokemonGen3.ONIX: Pokemon(
        name=PokemonGen3.ONIX,
        gen=2,
        types=[Types.ROCK, Types.GROUND],
        evolves_to=[Evolution(name=PokemonGen3.STEELIX, evolution_type=EvolutionType.TRADE, item=Item.METAL_COAT, should_hold=True)],
        colors=[Colors.GRAY],
        categories=[
            Categories.REPTILE,
            Categories.SNAKE,
        ],
        num_legs=0,
        stats=Stats(
            attack=35,
            defence=45,
            special_attack=160,
            special_defence=30,
        ),
        supported_abilities=[Abilities.ROCK_HEAD, Abilities.STURDY],
    ),
    PokemonGen3.DROWZEE: Pokemon(
        name=PokemonGen3.DROWZEE,
        gen=2,
        types=[Types.PSYCHIC],
        evolves_to=[
            Evolution(name=PokemonGen3.HYPNO)
        ],
        colors=[Colors.YELLOW, Colors.BROWN],
        categories=[
            Categories.MAMMAL,
            Categories.PIG,
        ],
        num_legs=2,
        stats=Stats(
            attack=40,
            defence=30,
            special_attack=50,
            special_defence=55,
        ),
        supported_abilities=[Abilities.INSOMNIA, Abilities.FOREWARN],
    ),
    PokemonGen3.HYPNO: Pokemon(
        name=PokemonGen3.HYPNO,
        gen=2,
        types=[Types.PSYCHIC],
        colors=[Colors.YELLOW],
        categories=[
            Categories.MAMMAL,
            Categories.HUMAN,
            Categories.PIG,
        ],
        num_legs=2,
        stats=Stats(
            attack=85,
            defence=40,
            special_attack=80,
            special_defence=100,
        ),
        supported_abilities=[Abilities.INSOMNIA, Abilities.FOREWARN],
    ),
    PokemonGen3.KRABBY: Pokemon(
        name=PokemonGen3.KRABBY,
        gen=2,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen3.KINGLER)
        ],
        colors=[Colors.ORANGE, Colors.WHITE],
        categories=[
            Categories.CRAB,
            Categories.WATERMON,
            Categories.FOOD,
        ],
        num_legs=4,
        stats=Stats(
            attack=55,
            defence=115,
            special_attack=45,
            special_defence=70,
        ),
        supported_abilities=[Abilities.HYPER_CUTTER, Abilities.SHELL_ARMOR],
    ),
    PokemonGen3.KINGLER: Pokemon(
        name=PokemonGen3.KINGLER,
        gen=2,
        types=[Types.WATER],
        colors=[Colors.WHITE, Colors.ORANGE],
        categories=[
            Categories.CRAB,
            Categories.WATERMON,
            Categories.FOOD,
        ],
        num_legs=4,
        stats=Stats(
            attack=55,
            defence=115,
            special_attack=45,
            special_defence=70,
        ),
        supported_abilities=[Abilities.HYPER_CUTTER, Abilities.SHELL_ARMOR],
    ),
    PokemonGen3.VOLTORB: Pokemon(
        name=PokemonGen3.VOLTORB,
        gen=2,
        types=[Types.ELECTRIC],
        evolves_to=[
            Evolution(name=PokemonGen3.ELECTRODE)
        ],
        colors=[Colors.RED, Colors.WHITE],
        categories=[
            Categories.ITEM,
        ],
        num_legs=0,
        stats=Stats(
            attack=60,
            defence=50,
            special_attack=70,
            special_defence=80,
        ),
        supported_abilities=[Abilities.SOUNDPROOF, Abilities.STATIC],
    ),
    PokemonGen3.ELECTRODE: Pokemon(
        name=PokemonGen3.ELECTRODE,
        gen=2,
        types=[Types.ELECTRIC],
        colors=[Colors.RED, Colors.WHITE],
        categories=[
            Categories.ITEM,
        ],
        num_legs=0,
        stats=Stats(
            attack=60,
            defence=50,
            special_attack=70,
            special_defence=80,
        ),
        supported_abilities=[Abilities.SOUNDPROOF, Abilities.STATIC],
    ),
    PokemonGen3.EXEGGCUTE: Pokemon(
        name=PokemonGen3.EXEGGCUTE,
        gen=2,
        types=[Types.GRASS, Types.PSYCHIC],
        evolves_to=[
            Evolution(name=PokemonGen3.EXEGGUTOR, level=43, evolution_type=EvolutionType.STONE, item=Item.LEAF_STONE)
        ],
        colors=[Colors.PINK],
        categories=[
            Categories.FOOD,
        ],
        num_legs=0,
        stats=Stats(
            attack=60,
            defence=50,
            special_attack=70,
            special_defence=80,
        ),
        supported_abilities=[Abilities.CHLOROPHYLL],
    ),
    PokemonGen3.EXEGGUTOR: Pokemon(
        name=PokemonGen3.EXEGGUTOR,
        gen=2,
        types=[Types.GRASS, Types.PSYCHIC],
        colors=[Colors.BROWN, Colors.YELLOW, Colors.GREEN],
        categories=[
            Categories.FOOD,
            Categories.PLANT,
        ],
        num_legs=2,
        stats=Stats(
            attack=95,
            defence=55,
            special_attack=85,
            special_defence=45,
        ),
        supported_abilities=[Abilities.CHLOROPHYLL],
    ),
    PokemonGen3.CUBONE: Pokemon(
        name=PokemonGen3.CUBONE,
        gen=2,
        types=[Types.GROUND],
        evolves_to=[
            Evolution(name=PokemonGen3.MAROWAK)
        ],
        colors=[Colors.BROWN, Colors.WHITE],
        categories=[
            Categories.PREHISTORIC,
            Categories.REPTILE,
            Categories.WEAPON,
        ],
        num_legs=2,
        stats=Stats(
            attack=50,
            defence=50,
            special_attack=95,
            special_defence=35,
        ),
        supported_abilities=[Abilities.ROCK_HEAD, Abilities.LIGHTNING_ROD],
    ),
    PokemonGen3.MAROWAK: Pokemon(
        name=PokemonGen3.MAROWAK,
        gen=2,
        types=[Types.GROUND],
        colors=[Colors.BROWN, Colors.WHITE],
        categories=[
            Categories.PREHISTORIC,
            Categories.REPTILE,
            Categories.WEAPON,
        ],
        num_legs=2,
        stats=Stats(
            attack=80,
            defence=80,
            special_attack=50,
            special_defence=40,
        ),
        supported_abilities=[Abilities.ROCK_HEAD, Abilities.LIGHTNING_ROD],
    ),
    PokemonGen3.HITMONLEE: Pokemon(
        name=PokemonGen3.HITMONLEE,
        gen=2,
        types=[Types.FIGHTING],
        colors=[Colors.BROWN],
        categories=[
            Categories.MAMMAL,
            Categories.HUMAN,
        ],
        num_legs=2,
        stats=Stats(
            attack=100,
            defence=53,
            special_attack=110,
            special_defence=87,
        ),
        supported_abilities=[Abilities.LIMBER, Abilities.RECKLESS],
    ),
    PokemonGen3.HITMONCHAN: Pokemon(
        name=PokemonGen3.HITMONCHAN,
        gen=2,
        types=[Types.FIGHTING],
        colors=[Colors.BROWN, Colors.RED],
        categories=[
            Categories.MAMMAL,
            Categories.HUMAN,
        ],
        num_legs=2,
        stats=Stats(
            attack=100,
            defence=53,
            special_attack=110,
            special_defence=87,
        ),
        supported_abilities=[Abilities.KEEN_EYE, Abilities.IRON_FIST],
    ),
    PokemonGen3.LICKITUNG: Pokemon(
        name=PokemonGen3.LICKITUNG,
        gen=2,
        types=[Types.NORMAL],
        colors=[Colors.PINK, Colors.YELLOW],
        categories=[
            Categories.FROG,
        ],
        num_legs=2,
        stats=Stats(
            attack=90,
            defence=55,
            special_attack=25,
            special_defence=35,
        ),
        supported_abilities=[Abilities.OWN_TEMPO, Abilities.OBLIVIOUS],
    ),
    PokemonGen3.KOFFING: Pokemon(
        name=PokemonGen3.KOFFING,
        gen=2,
        types=[Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen3.WEEZING)
        ],
        colors=[Colors.PURPLE],
        categories=[
            Categories.ITEM,
        ],
        num_legs=0,
        stats=Stats(
            attack=60,
            defence=60,
            special_attack=60,
            special_defence=60,
        ),
        supported_abilities=[Abilities.LEVITATE, Abilities.NEUTRALIZING_GAS],
    ),
    PokemonGen3.WEEZING: Pokemon(
        name=PokemonGen3.WEEZING,
        gen=2,
        types=[Types.POISON],
        colors=[Colors.PURPLE],
        categories=[
            Categories.ITEM,
        ],
        num_legs=0,
        stats=Stats(
            attack=60,
            defence=60,
            special_attack=60,
            special_defence=60,
        ),
        supported_abilities=[Abilities.LEVITATE, Abilities.NEUTRALIZING_GAS],
    ),
    PokemonGen3.RHYHORN: Pokemon(
        name=PokemonGen3.RHYHORN,
        gen=2,
        types=[Types.GROUND, Types.ROCK],
        evolves_to=[
            Evolution(name=PokemonGen3.RHYDON)
        ],
        colors=[Colors.GRAY],
        categories=[
            Categories.MAMMAL,
            Categories.WATERMON,
        ],
        num_legs=4,
        stats=Stats(
            attack=80,
            defence=80,
            special_attack=40,
            special_defence=40,
        ),
        supported_abilities=[Abilities.LIGHTNING_ROD, Abilities.ROCK_HEAD],
    ),
    PokemonGen3.RHYDON: Pokemon(
        name=PokemonGen3.RHYDON,
        gen=2,
        types=[Types.GROUND, Types.ROCK],
        colors=[Colors.GRAY, Colors.WHITE],
        categories=[
            Categories.MAMMAL,
            Categories.WATERMON,
        ],
        num_legs=2,
        stats=Stats(
            attack=105,
            defence=75,
            special_attack=85,
            special_defence=40,
        ),
        supported_abilities=[Abilities.LIGHTNING_ROD, Abilities.ROCK_HEAD],
    ),
    PokemonGen3.CHANSEY: Pokemon(
        name=PokemonGen3.CHANSEY,
        gen=2,
        types=[Types.NORMAL],
        evolves_to=[
            Evolution(name=PokemonGen3.BLISSEY, evolution_type=EvolutionType.FRIENDSHIP, level=47)
        ],
        colors=[Colors.PINK, Colors.WHITE],
        categories=[
            Categories.MAMMAL,
            Categories.FOOD,
            Categories.HUMAN,
        ],
        num_legs=2,
        stats=Stats(
            attack=100,
            defence=53,
            special_attack=110,
            special_defence=87,
        ),
        supported_abilities=[Abilities.NATURAL_CURE, Abilities.SERENE_GRACE],
    ),
    PokemonGen3.TANGELA: Pokemon(
        name=PokemonGen3.TANGELA,
        gen=2,
        types=[Types.GRASS],
        colors=[Colors.GREEN],
        categories=[
            Categories.PLANT,
            Categories.FOOD,
        ],
        num_legs=2,
        stats=Stats(
            attack=65,
            defence=55,
            special_attack=115,
            special_defence=60,
        ),
        supported_abilities=[Abilities.CHLOROPHYLL, Abilities.LEAF_GUARD],
    ),
    PokemonGen3.KANGASKHAN: Pokemon(
        name=PokemonGen3.KANGASKHAN,
        gen=2,
        types=[Types.NORMAL],
        colors=[Colors.BROWN, Colors.WHITE],
        categories=[
            Categories.MAMMAL,
        ],
        num_legs=2,
        stats=Stats(
            attack=105,
            defence=95,
            special_attack=85,
            special_defence=95,
        ),
        supported_abilities=[Abilities.EARLY_BIRD, Abilities.SCRAPPY],
    ),
    PokemonGen3.HORSEA: Pokemon(
        name=PokemonGen3.HORSEA,
        gen=2,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen3.SEADRA)
        ],
        colors=[Colors.BLUE, Colors.WHITE],
        categories=[
            Categories.WATERMON,
            Categories.FISH,
            Categories.DRAGON,
        ],
        num_legs=0,
        stats=Stats(
            attack=30,
            defence=40,
            special_attack=70,
            special_defence=20,
        ),
        supported_abilities=[Abilities.SWIFT_SWIM, Abilities.SNIPER],
    ),
    PokemonGen3.SEADRA: Pokemon(
        name=PokemonGen3.SEADRA,
        gen=2,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen3.KINGDRA, evolution_type=EvolutionType.TRADE, item=Item.DRAGON_SCALE, should_hold=True)
        ],
        colors=[Colors.BLUE, Colors.WHITE],
        categories=[
            Categories.WATERMON,
            Categories.FISH,
            Categories.DRAGON,
        ],
        num_legs=0,
        stats=Stats(
            attack=55,
            defence=65,
            special_attack=95,
            special_defence=85,
        ),
        supported_abilities=[Abilities.POISON_POINT, Abilities.SNIPER],
    ),
    PokemonGen3.GOLDEEN: Pokemon(
        name=PokemonGen3.GOLDEEN,
        gen=2,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen3.SEAKING)
        ],
        colors=[Colors.WHITE, Colors.RED],
        categories=[
            Categories.WATERMON,
            Categories.FISH,
            Categories.FOOD,
        ],
        num_legs=0,
        stats=Stats(
            attack=55,
            defence=65,
            special_attack=95,
            special_defence=85,
        ),
        supported_abilities=[Abilities.SWIFT_SWIM, Abilities.WATER_VEIL],
    ),
    PokemonGen3.SEAKING: Pokemon(
        name=PokemonGen3.SEAKING,
        gen=2,
        types=[Types.WATER],
        colors=[Colors.ORANGE, Colors.WHITE, Colors.BLACK],
        categories=[
            Categories.WATERMON,
            Categories.FISH,
            Categories.FOOD,
        ],
        num_legs=0,
        stats=Stats(
            attack=85,
            defence=95,
            special_attack=55,
            special_defence=45,
        ),
        supported_abilities=[Abilities.SWIFT_SWIM, Abilities.WATER_VEIL],
    ),
    PokemonGen3.STARYU: Pokemon(
        name=PokemonGen3.STARYU,
        gen=2,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen3.STARMIE, level=31, item=Item.WATER_STONE, evolution_type=EvolutionType.STONE)
        ],
        colors=[Colors.BROWN, Colors.YELLOW, Colors.RED],
        categories=[
            Categories.WATERMON,
            Categories.ITEM,
        ],
        num_legs=0,
        stats=Stats(
            attack=50,
            defence=50,
            special_attack=95,
            special_defence=85,
        ),
        supported_abilities=[Abilities.ILLUMINATE, Abilities.NATURAL_CURE],
    ),
    PokemonGen3.STARMIE: Pokemon(
        name=PokemonGen3.STARMIE,
        gen=2,
        types=[Types.WATER, Types.PSYCHIC],
        colors=[Colors.PURPLE, Colors.YELLOW, Colors.RED],
        categories=[
            Categories.WATERMON,
            Categories.ITEM,
        ],
        num_legs=0,
        stats=Stats(
            attack=50,
            defence=50,
            special_attack=95,
            special_defence=85,
        ),
        supported_abilities=[Abilities.ILLUMINATE, Abilities.NATURAL_CURE],
    ),
    PokemonGen3.MR_MIME: Pokemon(
        name=PokemonGen3.MR_MIME,
        gen=2,
        types=[Types.PSYCHIC],
        colors=[Colors.PINK, Colors.WHITE, Colors.BLUE],
        categories=[
            Categories.MAMMAL,
            Categories.HUMAN,
        ],
        num_legs=2,
        stats=Stats(
            attack=80,
            defence=80,
            special_attack=50,
            special_defence=40,
        ),
        supported_abilities=[Abilities.SOUNDPROOF, Abilities.FILTER],
    ),
    PokemonGen3.SCYTHER: Pokemon(
        name=PokemonGen3.SCYTHER,
        gen=2,
        types=[Types.BUG, Types.FLYING],
        evolves_to=[
            Evolution(name=PokemonGen3.SCIZOR, evolution_type=EvolutionType.TRADE, item=Item.MOON_STONE, should_hold=True),
        ],
        colors=[Colors.GREEN, Colors.WHITE],
        categories=[
            Categories.WING,
            Categories.BUG,
            Categories.WEAPON,
        ],
        num_legs=2,
        stats=Stats(
            attack=70,
            defence=100,
            special_attack=55,
            special_defence=80,
        ),
        supported_abilities=[Abilities.SWARM, Abilities.TECHNICIAN],
    ),
    PokemonGen3.JYNX: Pokemon(
        name=PokemonGen3.JYNX,
        gen=2,
        types=[Types.ICE, Types.PSYCHIC],
        colors=[Colors.PURPLE, Colors.YELLOW, Colors.RED],
        categories=[
            Categories.MAMMAL,
            Categories.FANTASY,
            Categories.HUMAN,
        ],
        num_legs=2,
        stats=Stats(
            attack=95,
            defence=95,
            special_attack=90,
            special_defence=90,
        ),
        supported_abilities=[Abilities.OBLIVIOUS, Abilities.FOREWARN],
    ),
    PokemonGen3.ELECTABUZZ: Pokemon(
        name=PokemonGen3.ELECTABUZZ,
        gen=2,
        types=[Types.ELECTRIC],
        colors=[Colors.YELLOW, Colors.BLACK],
        categories=[
            Categories.MAMMAL,
            Categories.HUMAN,
        ],
        num_legs=2,
        stats=Stats(
            attack=95,
            defence=95,
            special_attack=90,
            special_defence=90,
        ),
        supported_abilities=[Abilities.STATIC],
    ),
    PokemonGen3.MAGMAR: Pokemon(
        name=PokemonGen3.MAGMAR,
        gen=2,
        types=[Types.FIRE],
        colors=[Colors.RED, Colors.YELLOW],
        categories=[
            Categories.BIRD,
            Categories.WATERMON,
            Categories.FOOD,
            Categories.DUCK,
        ],
        num_legs=2,
        stats=Stats(
            attack=95,
            defence=95,
            special_attack=90,
            special_defence=90,
        ),
        supported_abilities=[Abilities.FLAME_BODY],
    ),
    PokemonGen3.PINSIR: Pokemon(
        name=PokemonGen3.PINSIR,
        gen=2,
        types=[Types.BUG],
        colors=[Colors.BROWN, Colors.WHITE],
        categories=[
            Categories.BUG,
        ],
        num_legs=2,
        stats=Stats(
            attack=100,
            defence=125,
            special_attack=100,
            special_defence=50,
        ),
        supported_abilities=[Abilities.HYPER_CUTTER, Abilities.MOLD_BREAKER],
    ),
    PokemonGen3.TAUROS: Pokemon(
        name=PokemonGen3.TAUROS,
        gen=2,
        types=[Types.NORMAL],
        colors=[Colors.BROWN],
        categories=[
            Categories.MAMMAL,
            Categories.FOOD,
            Categories.CATTLE,
            Categories.COW,
        ],
        num_legs=4,
        stats=Stats(
            attack=130,
            defence=85,
            special_attack=80,
            special_defence=60,
        ),
        supported_abilities=[Abilities.INTIMIDATE, Abilities.ANGER_POINT],
    ),
    PokemonGen3.MAGIKARP: Pokemon(
        name=PokemonGen3.MAGIKARP,
        gen=2,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen3.GYARADOS)
        ],
        colors=[Colors.RED],
        categories=[
            Categories.WATERMON,
            Categories.FOOD,
            Categories.FISH,
        ],
        num_legs=0,
        stats=Stats(
            attack=80,
            defence=100,
            special_attack=20,
            special_defence=50,
        ),
        supported_abilities=[Abilities.SWIFT_SWIM],
    ),
    PokemonGen3.GYARADOS: Pokemon(
        name=PokemonGen3.GYARADOS,
        gen=2,
        types=[Types.WATER, Types.FLYING],
        colors=[Colors.BLUE, Colors.YELLOW],
        categories=[
            Categories.WATERMON,
            Categories.DRAGON,
        ],
        num_legs=0,
        stats=Stats(
            attack=85,
            defence=90,
            special_attack=100,
            special_defence=120,
        ),
        supported_abilities=[Abilities.INTIMIDATE],
    ),
    PokemonGen3.LAPRAS: Pokemon(
        name=PokemonGen3.LAPRAS,
        gen=2,
        types=[Types.WATER, Types.ICE],
        colors=[Colors.BLUE, Colors.GRAY, Colors.WHITE],
        categories=[
            Categories.WATERMON,
            Categories.REPTILE,
            Categories.FANTASY,
            Categories.TURTLE,
        ],
        num_legs=0,
        stats=Stats(
            attack=130,
            defence=85,
            special_attack=80,
            special_defence=60,
        ),
        supported_abilities=[Abilities.WATER_ABSORB, Abilities.SHELL_ARMOR],
    ),
    PokemonGen3.DITTO: Pokemon(
        name=PokemonGen3.DITTO,
        gen=2,
        types=[Types.NORMAL],
        colors=[Colors.PINK],
        categories=[
            Categories.ITEM,
            Categories.FOOD,
        ],
        num_legs=0,
        stats=Stats(
            attack=45,
            defence=50,
            special_attack=45,
            special_defence=50,
        ),
        supported_abilities=[Abilities.LIMBER],
    ),
    PokemonGen3.EEVEE: Pokemon(
        name=PokemonGen3.EEVEE,
        gen=2,
        types=[Types.NORMAL],
        evolves_to=[
            Evolution(name=PokemonGen3.VAPOREON, evolution_type=EvolutionType.STONE, item=Item.WATER_STONE),
            Evolution(name=PokemonGen3.JOLTEON, evolution_type=EvolutionType.STONE, item=Item.THUNDER_STONE),
            Evolution(name=PokemonGen3.FLAREON, evolution_type=EvolutionType.STONE, item=Item.FIRE_STONE),
            Evolution(name=PokemonGen3.UMBREON, evolution_type=EvolutionType.FRIENDSHIP, special_information="Nighttime"),
            Evolution(name=PokemonGen3.ESPEON, evolution_type=EvolutionType.FRIENDSHIP, special_information="Daytime"),
        ],
        colors=[Colors.BROWN, Colors.WHITE],
        categories=[
            Categories.MAMMAL,
            Categories.DOG,
        ],
        num_legs=4,
        stats=Stats(
            attack=55,
            defence=50,
            special_attack=40,
            special_defence=55,
        ),
        supported_abilities=[Abilities.RUN_AWAY, Abilities.ADAPTABILITY],
    ),
    PokemonGen3.VAPOREON: Pokemon(
        name=PokemonGen3.VAPOREON,
        gen=2,
        types=[Types.WATER],
        colors=[Colors.BLUE, Colors.WHITE],
        categories=[
            Categories.MAMMAL,
            Categories.DOG,
            Categories.WATERMON,
        ],
        num_legs=4,
        stats=Stats(
            attack=65,
            defence=60,
            special_attack=110,
            special_defence=95,
        ),
        supported_abilities=[Abilities.WATER_ABSORB],
    ),
    PokemonGen3.JOLTEON: Pokemon(
        name=PokemonGen3.JOLTEON,
        gen=2,
        types=[Types.ELECTRIC],
        colors=[Colors.YELLOW, Colors.WHITE],
        categories=[
            Categories.MAMMAL,
            Categories.DOG,
        ],
        num_legs=4,
        stats=Stats(
            attack=65,
            defence=60,
            special_attack=110,
            special_defence=95,
        ),
        supported_abilities=[Abilities.VOLT_ABSORB],
    ),
    PokemonGen3.FLAREON: Pokemon(
        name=PokemonGen3.FLAREON,
        gen=2,
        types=[Types.FIRE],
        colors=[Colors.RED, Colors.WHITE],
        categories=[
            Categories.MAMMAL,
            Categories.DOG,
        ],
        num_legs=4,
        stats=Stats(
            attack=65,
            defence=60,
            special_attack=110,
            special_defence=95,
        ),
        supported_abilities=[Abilities.FLASH_FIRE],
    ),
    PokemonGen3.PORYGON: Pokemon(
        name=PokemonGen3.PORYGON,
        gen=2,
        types=[Types.NORMAL],
        evolves_to=[
            Evolution(name=PokemonGen3.PORYGON2, evolution_type=EvolutionType.TRADE, item=Item.UPGRADE, should_hold=True)
        ],
        colors=[Colors.BLUE, Colors.PINK],
        categories=[
            Categories.ITEM,
        ],
        num_legs=0,
        stats=Stats(
            attack=60,
            defence=70,
            special_attack=85,
            special_defence=75,
        ),
        supported_abilities=[Abilities.TRACE, Abilities.DOWNLOAD],
    ),
    PokemonGen3.OMANYTE: Pokemon(
        name=PokemonGen3.OMANYTE,
        gen=2,
        types=[Types.ROCK, Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen3.OMASTAR)
        ],
        colors=[Colors.BLUE, Colors.BROWN],
        categories=[
            Categories.PREHISTORIC,
            Categories.WATERMON,
            Categories.FOOD,
        ],
        num_legs=0,
        stats=Stats(
            attack=35,
            defence=40,
            special_attack=100,
            special_defence=90,
        ),
        supported_abilities=[Abilities.SWIFT_SWIM, Abilities.SHELL_ARMOR],
    ),
    PokemonGen3.OMASTAR: Pokemon(
        name=PokemonGen3.OMASTAR,
        gen=2,
        types=[Types.ROCK, Types.WATER],
        colors=[Colors.BLUE, Colors.BROWN],
        categories=[
            Categories.PREHISTORIC,
            Categories.WATERMON,
            Categories.FOOD,
        ],
        num_legs=0,
        stats=Stats(
            attack=55,
            defence=105,
            special_attack=100,
            special_defence=50,
        ),
        supported_abilities=[Abilities.SWIFT_SWIM, Abilities.SHELL_ARMOR],
    ),
    PokemonGen3.KABUTO: Pokemon(
        name=PokemonGen3.KABUTO,
        gen=2,
        types=[Types.ROCK, Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen3.KABUTOPS)
        ],
        colors=[Colors.BROWN, Colors.BLACK],
        categories=[
            Categories.PREHISTORIC,
            Categories.CRAB,
            Categories.WATERMON,
            Categories.FOOD,
        ],
        num_legs=0,
        stats=Stats(
            attack=55,
            defence=105,
            special_attack=100,
            special_defence=50,
        ),
        supported_abilities=[Abilities.SWIFT_SWIM, Abilities.BATTLE_ARMOR],
    ),
    PokemonGen3.KABUTOPS: Pokemon(
        name=PokemonGen3.KABUTOPS,
        gen=2,
        types=[Types.ROCK, Types.WATER],
        colors=[Colors.BROWN, Colors.BLACK],
        categories=[
            Categories.PREHISTORIC,
            Categories.CRAB,
            Categories.WATERMON,
            Categories.FOOD,
            Categories.WEAPON,
        ],
        num_legs=2,
        stats=Stats(
            attack=55,
            defence=105,
            special_attack=100,
            special_defence=50,
        ),
        supported_abilities=[Abilities.SWIFT_SWIM, Abilities.BATTLE_ARMOR],
    ),
    PokemonGen3.AERODACTYL: Pokemon(
        name=PokemonGen3.AERODACTYL,
        gen=2,
        types=[Types.ROCK, Types.FLYING],
        colors=[Colors.GRAY, Colors.PURPLE],
        categories=[
            Categories.PREHISTORIC,
            Categories.WING,
            Categories.REPTILE,
        ],
        num_legs=2,
        stats=Stats(
            attack=80,
            defence=105,
            special_attack=60,
            special_defence=70,
        ),
        supported_abilities=[Abilities.ROCK_HEAD, Abilities.PRESSURE],
    ),
    PokemonGen3.SNORLAX: Pokemon(
        name=PokemonGen3.SNORLAX,
        gen=2,
        types=[Types.NORMAL],
        colors=[Colors.GREEN, Colors.WHITE],
        categories=[
            Categories.MAMMAL,
            Categories.BEAR,
        ],
        num_legs=2,
        stats=Stats(
            attack=160,
            defence=110,
            special_attack=65,
            special_defence=110,
        ),
        supported_abilities=[Abilities.IMMUNITY, Abilities.THICK_FAT],
    ),
    PokemonGen3.ARTICUNO: Pokemon(
        name=PokemonGen3.ARTICUNO,
        gen=2,
        types=[Types.ICE, Types.FLYING],
        colors=[Colors.BLUE],
        categories=[
            Categories.WING,
            Categories.BIRD,
        ],
        num_legs=2,
        stats=Stats(
            attack=90,
            defence=85,
            special_attack=100,
            special_defence=95,
        ),
        supported_abilities=[Abilities.PRESSURE],
    ),
    PokemonGen3.ZAPDOS: Pokemon(
        name=PokemonGen3.ZAPDOS,
        gen=2,
        types=[Types.ELECTRIC, Types.FLYING],
        colors=[Colors.YELLOW],
        categories=[
            Categories.WING,
            Categories.BIRD,
        ],
        num_legs=2,
        stats=Stats(
            attack=90,
            defence=85,
            special_attack=100,
            special_defence=95,
        ),
        supported_abilities=[Abilities.PRESSURE],
    ),
    PokemonGen3.MOLTRES: Pokemon(
        name=PokemonGen3.MOLTRES,
        gen=2,
        types=[Types.FIRE, Types.FLYING],
        colors=[Colors.RED, Colors.YELLOW, Colors.ORANGE],
        categories=[
            Categories.WING,
            Categories.BIRD,
        ],
        num_legs=2,
        stats=Stats(
            attack=90,
            defence=85,
            special_attack=100,
            special_defence=95,
        ),
        supported_abilities=[Abilities.PRESSURE],
    ),
    PokemonGen3.DRATINI: Pokemon(
        name=PokemonGen3.DRATINI,
        gen=2,
        types=[Types.DRAGON],
        evolves_to=[
            Evolution(name=PokemonGen3.DRAGONAIR)
        ],
        colors=[Colors.BLUE, Colors.WHITE],
        categories=[
            Categories.REPTILE,
            Categories.WATERMON,
            Categories.FANTASY,
            Categories.DRAGON,
            Categories.SNAKE,
        ],
        num_legs=0,
        stats=Stats(
            attack=61,
            defence=84,
            special_attack=65,
            special_defence=70,
        ),
        supported_abilities=[Abilities.SHED_SKIN],
    ),
    PokemonGen3.DRAGONAIR: Pokemon(
        name=PokemonGen3.DRAGONAIR,
        gen=2,
        types=[Types.DRAGON],
        evolves_to=[
            Evolution(name=PokemonGen3.DRAGONITE)
        ],
        colors=[Colors.BLUE, Colors.WHITE],
        categories=[
            Categories.REPTILE,
            Categories.WATERMON,
            Categories.FANTASY,
            Categories.DRAGON,
            Categories.SNAKE,
        ],
        num_legs=0,
        stats=Stats(
            attack=61,
            defence=84,
            special_attack=65,
            special_defence=70,
        ),
        supported_abilities=[Abilities.SHED_SKIN],
    ),
    PokemonGen3.DRAGONITE: Pokemon(
        name=PokemonGen3.DRAGONITE,
        gen=2,
        types=[Types.DRAGON, Types.FLYING],
        colors=[Colors.ORANGE, Colors.GREEN, Colors.WHITE],
        categories=[
            Categories.WING,
            Categories.REPTILE,
            Categories.FANTASY,
            Categories.DRAGON,
        ],
        num_legs=2,
        stats=Stats(
            attack=106,
            defence=90,
            special_attack=130,
            special_defence=90,
        ),
        supported_abilities=[Abilities.INNER_FOCUS],
    ),
    PokemonGen3.MEWTWO: Pokemon(
        name=PokemonGen3.MEWTWO,
        gen=2,
        types=[Types.PSYCHIC],
        colors=[Colors.GRAY, Colors.PURPLE],
        categories=[
            Categories.MAMMAL,
            Categories.HUMAN,
        ],
        num_legs=2,
        stats=Stats(
            attack=106,
            defence=90,
            special_attack=130,
            special_defence=90,
        ),
        supported_abilities=[Abilities.PRESSURE],
    ),
    PokemonGen3.MEW: Pokemon(
        name=PokemonGen3.MEW,
        gen=2,
        types=[Types.PSYCHIC],
        colors=[Colors.PINK],
        categories=[
            Categories.RODENT,
            Categories.MOUSE,
        ],
        num_legs=2,
        stats=Stats(
            attack=100,
            defence=100,
            special_attack=100,
            special_defence=100,
        ),
        supported_abilities=[Abilities.SYNCHRONIZE],
    ),
    PokemonGen3.CHIKORITA: Pokemon(
        name=PokemonGen3.CHIKORITA,
        gen=2,
        types=[Types.GRASS],
        evolves_to=[
            Evolution(name=PokemonGen3.BAYLEEF)
        ],
        colors=[Colors.GREEN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=49,
            defence=65,
            special_attack=49,
            special_defence=65,
        ),
        categories=[
            Categories.PREHISTORIC,
            Categories.REPTILE,
            Categories.PLANT,
        ],
        num_legs=4,
    ),
    PokemonGen3.BAYLEEF: Pokemon(
        name=PokemonGen3.BAYLEEF,
        gen=2,
        types=[Types.GRASS],
        evolves_to=[
            Evolution(name=PokemonGen3.MEGANIUM)
        ],
        colors=[Colors.GREEN, Colors.YELLOW],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=62,
            defence=80,
            special_attack=63,
            special_defence=80,
        ),
        categories=[
            Categories.PREHISTORIC,
            Categories.REPTILE,
            Categories.PLANT,
        ],
        num_legs=4,
    ),
    PokemonGen3.MEGANIUM: Pokemon(
        name=PokemonGen3.MEGANIUM,
        gen=2,
        types=[Types.GRASS],
        colors=[Colors.GREEN, Colors.PINK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=82,
            defence=100,
            special_attack=83,
            special_defence=100,
        ),
        categories=[
            Categories.PREHISTORIC,
            Categories.REPTILE,
            Categories.PLANT,
        ],
        num_legs=4,
    ),
    PokemonGen3.CYNDAQUIL: Pokemon(
        name=PokemonGen3.CYNDAQUIL,
        gen=2,
        types=[Types.FIRE],
        evolves_to=[
            Evolution(name="Quilava")
        ],
        colors=[Colors.WHITE, Colors.BLUE, Colors.RED, Colors.YELLOW],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=52,
            defence=43,
            special_attack=60,
            special_defence=50,
        ),
        categories=[
            Categories.MAMMAL,
        ],
        num_legs=4,
    ),
    PokemonGen3.QUILAVA: Pokemon(
        name=PokemonGen3.QUILAVA,
        gen=2,
        types=[Types.FIRE],
        evolves_to=[
            Evolution(name="Typhlosion")
        ],
        colors=[Colors.WHITE, Colors.BLUE, Colors.RED, Colors.YELLOW],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=64,
            defence=58,
            special_attack=80,
            special_defence=65,
        ),
        categories=[
            Categories.MAMMAL,
        ],
        num_legs=4,
    ),
    PokemonGen3.TYPHLOSION: Pokemon(
        name=PokemonGen3.TYPHLOSION,
        gen=2,
        types=[Types.FIRE],
        colors=[Colors.WHITE, Colors.BLUE, Colors.RED, Colors.YELLOW],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=84,
            defence=78,
            special_attack=109,
            special_defence=85,
        ),
        categories=[
            Categories.MAMMAL,
        ],
        num_legs=4,
    ),
    PokemonGen3.TOTODILE: Pokemon(
        name=PokemonGen3.TOTODILE,
        gen=2,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name="Croconaw")
        ],
        colors=[Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=65,
            defence=64,
            special_attack=44,
            special_defence=48,
        ),
        categories=[
            Categories.REPTILE,
            Categories.WATERMON,
        ],
        num_legs=2,
    ),
    PokemonGen3.CROCONAW: Pokemon(
        name=PokemonGen3.CROCONAW,
        gen=2,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name="Feraligatr")
        ],
        colors=[Colors.BLUE, Colors.YELLOW],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=80,
            defence=80,
            special_attack=59,
            special_defence=63,
        ),
        categories=[
            Categories.REPTILE,
            Categories.WATERMON,
        ],
        num_legs=2,
    ),
    PokemonGen3.FERALIGATR: Pokemon(
        name=PokemonGen3.FERALIGATR,
        gen=2,
        types=[Types.WATER],
        colors=[Colors.BLUE, Colors.YELLOW],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=105,
            defence=100,
            special_attack=79,
            special_defence=83,
        ),
        categories=[
            Categories.REPTILE,
            Categories.WATERMON,
        ],
        num_legs=2,
    ),
    PokemonGen3.SENTRET: Pokemon(
        name=PokemonGen3.SENTRET,
        gen=2,
        types=[Types.NORMAL],
        evolves_to=[
            Evolution(name=PokemonGen3.FURRET)
        ],
        colors=[Colors.BROWN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=49,
            defence=34,
            special_attack=35,
            special_defence=45,
        ),
        categories=[
            Categories.MAMMAL,
        ],
        num_legs=4,
    ),
    PokemonGen3.FURRET: Pokemon(
        name=PokemonGen3.FURRET,
        gen=2,
        types=[Types.NORMAL],
        colors=[Colors.BROWN, Colors.WHITE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=76,
            defence=64,
            special_attack=45,
            special_defence=55,
        ),
        categories=[
            Categories.MAMMAL,
        ],
        num_legs=4,
    ),
    PokemonGen3.HOOTHOOT: Pokemon(
        name=PokemonGen3.HOOTHOOT,
        gen=2,
        types=[Types.NORMAL, Types.FLYING],
        evolves_to=[
            Evolution(name=PokemonGen3.NOCTOWL)
        ],
        colors=[Colors.BROWN, Colors.WHITE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=30,
            defence=30,
            special_attack=36,
            special_defence=56,
        ),
        categories=[
            Categories.WING,
            Categories.BIRD,
        ],
        num_legs=2,
    ),
    PokemonGen3.NOCTOWL: Pokemon(
        name=PokemonGen3.NOCTOWL,
        gen=2,
        types=[Types.NORMAL, Types.FLYING],
        colors=[Colors.BROWN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=50,
            defence=50,
            special_attack=86,
            special_defence=96,
        ),
        categories=[
            Categories.WING,
            Categories.BIRD,
        ],
        num_legs=2,
    ),
    PokemonGen3.LEDYBA: Pokemon(
        name=PokemonGen3.LEDYBA,
        gen=2,
        types=[Types.BUG, Types.FLYING],
        evolves_to=[
            Evolution(name=PokemonGen3.LEDIAN)
        ],
        colors=[Colors.WHITE, Colors.RED, Colors.BLACK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=20,
            defence=30,
            special_attack=40,
            special_defence=80,
        ),
        categories=[
            Categories.WING,
            Categories.BUG,
        ],
        num_legs=6,
    ),
    PokemonGen3.LEDIAN: Pokemon(
        name=PokemonGen3.LEDIAN,
        gen=2,
        types=[Types.BUG, Types.FLYING],
        colors=[Colors.WHITE, Colors.RED, Colors.BLACK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=35,
            defence=50,
            special_attack=55,
            special_defence=110,
        ),
        categories=[
            Categories.WING,
            Categories.BUG,
        ],
        num_legs=2,
    ),
    PokemonGen3.SPINARAK: Pokemon(
        name=PokemonGen3.SPINARAK,
        gen=2,
        types=[Types.BUG, Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen3.ARIADOS)
        ],
        colors=[Colors.GREEN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=60,
            defence=40,
            special_attack=40,
            special_defence=40,
        ),
        categories=[
            Categories.BUG,
        ],
        num_legs=6,
    ),
    PokemonGen3.ARIADOS: Pokemon(
        name=PokemonGen3.ARIADOS,
        gen=2,
        types=[Types.BUG, Types.POISON],
        colors=[Colors.RED, Colors.BLACK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=90,
            defence=70,
            special_attack=60,
            special_defence=70,
        ),
        categories=[
            Categories.BUG,
        ],
        num_legs=4,
    ),
    PokemonGen3.CROBAT: Pokemon(
        name=PokemonGen3.CROBAT,
        gen=2,
        types=[Types.POISON, Types.FLYING],
        colors=[Colors.PURPLE, Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=90,
            defence=80,
            special_attack=70,
            special_defence=80,
        ),
        categories=[
            Categories.WING,
            Categories.MAMMAL,
        ],
        num_legs=2,
    ),
    PokemonGen3.CHINCHOU: Pokemon(
        name=PokemonGen3.CHINCHOU,
        gen=2,
        types=[Types.WATER, Types.ELECTRIC],
        evolves_to=[
            Evolution(name=PokemonGen3.LANTURN)
        ],
        colors=[Colors.BLUE, Colors.YELLOW],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=38,
            defence=38,
            special_attack=56,
            special_defence=56,
        ),
        categories=[
            Categories.WATERMON,
            Categories.FISH,
        ],
        num_legs=0,
    ),
    PokemonGen3.LANTURN: Pokemon(
        name=PokemonGen3.LANTURN,
        gen=2,
        types=[Types.WATER, Types.ELECTRIC],
        colors=[Colors.BLUE, Colors.YELLOW],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=58,
            defence=58,
            special_attack=76,
            special_defence=76,
        ),
        categories=[
            Categories.WATERMON,
            Categories.FISH,
        ],
        num_legs=0,
    ),
    PokemonGen3.PICHU: Pokemon(
        name=PokemonGen3.PICHU,
        gen=2,
        types=[Types.ELECTRIC],
        evolves_to=[Evolution(name='Pikachu', evolution_type=EvolutionType.FRIENDSHIP, level=11)],
        colors=[Colors.YELLOW, Colors.BLACK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=40,
            defence=15,
            special_attack=35,
            special_defence=35,
        ),
        categories=[
            Categories.RODENT,
            Categories.MOUSE,
        ],
        num_legs=2,
    ),
    PokemonGen3.CLEFFA: Pokemon(
        name=PokemonGen3.CLEFFA,
        gen=2,
        types=[Types.NORMAL],
        evolves_to=[
            Evolution(name='Clefairy', evolution_type=EvolutionType.FRIENDSHIP, level=13)
        ],
        colors=[Colors.PINK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=25,
            defence=28,
            special_attack=45,
            special_defence=55,
        ),
        categories=[
            Categories.FANTASY,
            Categories.MAMMAL,
            Categories.HUMAN,
        ],
        num_legs=2,
        ),
    PokemonGen3.IGGLYBUFF: Pokemon(
        name=PokemonGen3.IGGLYBUFF,
        gen=2,
        types=[Types.NORMAL],
        evolves_to=[
            Evolution(name='Jigglypuff', evolution_type=EvolutionType.FRIENDSHIP, level=14)
        ],
        colors=[Colors.PINK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=30,
            defence=15,
            special_attack=40,
            special_defence=20,
        ),
        categories=[
            Categories.ITEM,
            Categories.FOOD,
        ],
        num_legs=2,
    ),
    PokemonGen3.TOGEPI: Pokemon(
        name=PokemonGen3.TOGEPI,
        gen=2,
        types=[Types.NORMAL],
        evolves_to=[
            Evolution(name='Togetic', evolution_type=EvolutionType.FRIENDSHIP)
        ],
        colors=[Colors.WHITE, Colors.BLUE, Colors.RED],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=20,
            defence=65,
            special_attack=40,
            special_defence=65,
        ),
        categories=[
            Categories.ITEM,
            Categories.FOOD,
        ],
        num_legs=2,
    ),
    PokemonGen3.TOGETIC: Pokemon(
        name=PokemonGen3.TOGETIC,
        gen=2,
        types=[Types.NORMAL, Types.FLYING],
        colors=[Colors.WHITE, Colors.BLUE, Colors.RED],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=40,
            defence=85,
            special_attack=80,
            special_defence=105,
        ),
        categories=[
            Categories.ITEM,
            Categories.FOOD,
            Categories.WING,
        ],
        num_legs=2,
    ),
    PokemonGen3.NATU: Pokemon(
        name=PokemonGen3.NATU,
        gen=2,
        types=[Types.PSYCHIC, Types.FLYING],
        evolves_to=[
            Evolution(name=PokemonGen3.XATU)
        ],
        colors=[Colors.GREEN, Colors.YELLOW, Colors.RED],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=50,
            defence=45,
            special_attack=70,
            special_defence=45,
        ),
        categories=[
            Categories.BIRD,
            Categories.WING,
        ],
        num_legs=2,
    ),
    PokemonGen3.XATU: Pokemon(
        name=PokemonGen3.XATU,
        gen=2,
        types=[Types.PSYCHIC, Types.FLYING],
        colors=[Colors.GREEN, Colors.WHITE, Colors.RED],
        supported_genders=[Genders.MALE, Genders.FEMALE],stats=Stats(
            attack=75,
            defence=70,
            special_attack=95,
            special_defence=70,
        ),
        categories=[
            Categories.BIRD,
            Categories.WING,
        ],
        num_legs=2,
    ),
    PokemonGen3.MAREEP: Pokemon(
        name=PokemonGen3.MAREEP,
        gen=2,
        types=[Types.ELECTRIC],
        evolves_to=[
            Evolution(name=PokemonGen3.FLAAFFY)
        ],
        colors=[Colors.WHITE, Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=40,
            defence=40,
            special_attack=65,
            special_defence=45,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.FOOD,
            Categories.CATTLE,
        ],
        num_legs=4,
    ),
    PokemonGen3.FLAAFFY: Pokemon(
        name=PokemonGen3.FLAAFFY,
        gen=2,
        types=[Types.ELECTRIC],
        evolves_to=[
            Evolution(name=PokemonGen3.AMPHAROS)
        ],
        colors=[Colors.WHITE, Colors.PINK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=55,
            defence=55,
            special_attack=80,
            special_defence=60,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.FOOD,
            Categories.CATTLE,
        ],
        num_legs=2,
    ),
    PokemonGen3.AMPHAROS: Pokemon(
        name=PokemonGen3.AMPHAROS,
        gen=2,
        types=[Types.ELECTRIC],
        colors=[Colors.WHITE, Colors.BLACK, Colors.YELLOW],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=75,
            defence=85,
            special_attack=115,
            special_defence=90,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.FOOD,
            Categories.CATTLE,
        ],
        num_legs=2,
    ),
    PokemonGen3.BELLOSSOM: Pokemon(
        name=PokemonGen3.BELLOSSOM,
        gen=2,
        types=[Types.GRASS],
        colors=[Colors.YELLOW, Colors.GREEN, Colors.RED],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=80,
            defence=95,
            special_attack=90,
            special_defence=100,
        ),
        categories=[
            Categories.PLANT,
            Categories.MAMMAL,
            Categories.HUMAN,
        ],
        num_legs=2,
    ),
    PokemonGen3.MARILL: Pokemon(
        name=PokemonGen3.MARILL,
        gen=2,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen3.AZUMARILL)
        ],
        colors=[Colors.BLUE, Colors.WHITE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=20,
            defence=50,
            special_attack=20,
            special_defence=50,
        ),
        categories=[
            Categories.RODENT,
            Categories.MOUSE,
        ],
        num_legs=2,
    ),
    PokemonGen3.AZUMARILL: Pokemon(
        name=PokemonGen3.AZUMARILL,
        gen=2,
        types=[Types.WATER],
        colors=[Colors.BLUE, Colors.WHITE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=50,
            defence=80,
            special_attack=60,
            special_defence=80,
        ),
        categories=[
            Categories.RODENT,
            Categories.MOUSE,
        ],
        num_legs=2,
    ),
    PokemonGen3.SUDOWOODO: Pokemon(
        name=PokemonGen3.SUDOWOODO,
        gen=2,
        types=[Types.ROCK],
        colors=[Colors.BROWN, Colors.GREEN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=100,
            defence=115,
            special_attack=30,
            special_defence=65,
        ),
        categories=[
            Categories.PLANT,
        ],
        num_legs=2,
    ),
    PokemonGen3.POLITOED: Pokemon(
        name=PokemonGen3.POLITOED,
        gen=2,
        types=[Types.WATER],
        colors=[Colors.GREEN, Colors.YELLOW],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=75,
            defence=75,
            special_attack=90,
            special_defence=100,
        ),
        categories=[
            Categories.WATERMON,
            Categories.FOOD,
            Categories.FROG,
            Categories.REPTILE,
        ],
        num_legs=2,
    ),
    PokemonGen3.HOPPIP: Pokemon(
        name=PokemonGen3.HOPPIP,
        gen=2,
        types=[Types.GRASS, Types.FLYING],
        evolves_to=[
            Evolution(name=PokemonGen3.SKIPLOOM)
        ],
        colors=[Colors.PINK, Colors.GREEN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=35,
            defence=40,
            special_attack=35,
            special_defence=55,
        ),
        categories=[
            Categories.PREHISTORIC,
            Categories.PLANT,
        ],
        num_legs=2,
    ),
    PokemonGen3.SKIPLOOM: Pokemon(
        name=PokemonGen3.SKIPLOOM,
        gen=2,
        types=[Types.GRASS, Types.FLYING],
        evolves_to=[
            Evolution(name=PokemonGen3.JUMPLUFF)
        ],
        colors=[Colors.GREEN, Colors.YELLOW],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=45,
            defence=50,
            special_attack=45,
            special_defence=65,
        ),
        categories=[
            Categories.PREHISTORIC,
            Categories.PLANT,
        ],
        num_legs=2,
    ),
    PokemonGen3.JUMPLUFF: Pokemon(
        name=PokemonGen3.JUMPLUFF,
        gen=2,
        types=[Types.GRASS, Types.FLYING],
        colors=[Colors.BLUE, Colors.WHITE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=55,
            defence=75,
            special_attack=55,
            special_defence=95,
        ),
        categories=[
            Categories.PREHISTORIC,
            Categories.PLANT,
        ],
        num_legs=2,
    ),
    PokemonGen3.AIPOM: Pokemon(
        name=PokemonGen3.AIPOM,
        gen=2,
        types=[Types.NORMAL],
        colors=[Colors.PURPLE, Colors.WHITE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=70,
            defence=55,
            special_attack=40,
            special_defence=55,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.APE,
        ],
        num_legs=2,
    ),
    PokemonGen3.SUNKERN: Pokemon(
        name=PokemonGen3.SUNKERN,
        gen=2,
        types=[Types.GRASS],
        evolves_to=[
            Evolution(name=PokemonGen3.SUNFLORA)
        ],
        colors=[Colors.YELLOW, Colors.BROWN, Colors.GREEN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=30,
            defence=30,
            special_attack=30,
            special_defence=30,
        ),
        categories=[
            Categories.PLANT,
        ],
        num_legs=0,
    ),
    PokemonGen3.SUNFLORA: Pokemon(
        name=PokemonGen3.SUNFLORA,
        gen=2,
        types=[Types.GRASS],
        colors=[Colors.GREEN, Colors.YELLOW, Colors.WHITE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=75,
            defence=55,
            special_attack=105,
            special_defence=85,
        ),
        categories=[
            Categories.PLANT,
        ],
        num_legs=2,
    ),
    PokemonGen3.YANMA: Pokemon(
        name=PokemonGen3.YANMA,
        gen=2,
        types=[Types.BUG, Types.FLYING],
        colors=[Colors.RED, Colors.WHITE, Colors.GREEN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=65,
            defence=45,
            special_attack=75,
            special_defence=45,
        ),
        categories=[
            Categories.WING,
            Categories.BUG,
            Categories.WATERMON,
            Categories.DRAGON,
        ],
        num_legs=6,
    ),
    PokemonGen3.WOOPER: Pokemon(
        name=PokemonGen3.WOOPER,
        gen=2,
        types=[Types.WATER, Types.GROUND],
        evolves_to=[
            Evolution(name=PokemonGen3.QUAGSIRE)
        ],
        colors=[Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=45,
            defence=45,
            special_attack=25,
            special_defence=25,
        ),
        categories=[
            Categories.WATERMON,
            Categories.FROG,
        ],
        num_legs=2,
    ),
    PokemonGen3.QUAGSIRE: Pokemon(
        name=PokemonGen3.QUAGSIRE,
        gen=2,
        types=[Types.WATER, Types.GROUND],
        colors=[Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=85,
            defence=85,
            special_attack=65,
            special_defence=65,
        ),
        categories=[
            Categories.WATERMON,
            Categories.FROG,
        ],
        num_legs=2,
    ),
    PokemonGen3.ESPEON: Pokemon(
        name=PokemonGen3.ESPEON,
        gen=2,
        types=[Types.PSYCHIC],
        colors=[Colors.PINK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=65,
            defence=60,
            special_attack=130,
            special_defence=95,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.DOG,
        ],
        num_legs=4,
    ),
    PokemonGen3.UMBREON: Pokemon(
        name=PokemonGen3.UMBREON,
        gen=2,
        types=[Types.DARK],
        colors=[Colors.BLACK, Colors.YELLOW],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=65,
            defence=110,
            special_attack=60,
            special_defence=130,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.DOG,
        ],
        num_legs=4,
    ),
    PokemonGen3.MURKROW: Pokemon(
        name=PokemonGen3.MURKROW,
        gen=2,
        types=[Types.DARK, Types.FLYING],
        colors=[Colors.BLACK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=85,
            defence=42,
            special_attack=85,
            special_defence=42,
        ),
        categories=[
            Categories.WING,
            Categories.BIRD,
            Categories.FANTASY,
        ],
        num_legs=2,
    ),
    PokemonGen3.SLOWKING: Pokemon(
        name=PokemonGen3.SLOWKING,
        gen=2,
        types=[Types.WATER, Types.PSYCHIC],
        colors=[Colors.PINK, Colors.GRAY],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=75,
            defence=80,
            special_attack=100,
            special_defence=110,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.WATERMON,
            Categories.SLOTH,
        ],
        num_legs=2,
    ),
    PokemonGen3.MISDREAVUS: Pokemon(
        name=PokemonGen3.MISDREAVUS,
        gen=2,
        types=[Types.GHOST],
        colors=[Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=60,
            defence=60,
            special_attack=85,
            special_defence=85,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.HUMAN,
        ],
        num_legs=0,
    ),
    PokemonGen3.UNOWN: Pokemon(
        name=PokemonGen3.UNOWN,
        gen=2,
        types=[Types.PSYCHIC],
        colors=[Colors.BLACK, Colors.WHITE],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=72,
            defence=48,
            special_attack=72,
            special_defence=48,
        ),
        categories=[
            Categories.PREHISTORIC,
            Categories.ITEM,
            Categories.FOOD,
        ],
        num_legs=0,
    ),
    PokemonGen3.WOBBUFFET: Pokemon(
        name=PokemonGen3.WOBBUFFET,
        gen=2,
        types=[Types.PSYCHIC],
        colors=[Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=33,
            defence=58,
            special_attack=33,
            special_defence=58,
        ),
        categories=[
            Categories.ITEM,
        ],
        num_legs=2,
    ),
    PokemonGen3.GIRAFARIG: Pokemon(
        name=PokemonGen3.GIRAFARIG,
        gen=2,
        types=[Types.NORMAL, Types.PSYCHIC],
        colors=[Colors.YELLOW, Colors.BROWN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=80,
            defence=65,
            special_attack=90,
            special_defence=65,
        ),
        categories=[
            Categories.MAMMAL,
        ],
        num_legs=4,
    ),
    PokemonGen3.PINECO: Pokemon(
        name=PokemonGen3.PINECO,
        gen=2,
        types=[Types.BUG],
        evolves_to=[
            Evolution(name=PokemonGen3.FORRETRESS)
        ],
        colors=[Colors.BLUE, Colors.GREEN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=65,
            defence=90,
            special_attack=35,
            special_defence=35,
        ),
        categories=[
            Categories.PLANT,
        ],
        num_legs=0,
    ),
    PokemonGen3.FORRETRESS: Pokemon(
        name=PokemonGen3.FORRETRESS,
        gen=2,
        types=[Types.BUG, Types.STEEL],
        colors=[Colors.GRAY, Colors.RED],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=90,
            defence=140,
            special_attack=60,
            special_defence=60,
        ),
        categories=[
            Categories.PLANT,
        ],
        num_legs=0,
    ),
    PokemonGen3.DUNSPARCE: Pokemon(
        name=PokemonGen3.DUNSPARCE,
        gen=2,
        types=[Types.NORMAL],
        colors=[Colors.YELLOW, Colors.BLUE, Colors.WHITE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=70,
            defence=70,
            special_attack=65,
            special_defence=65,
        ),
        categories=[
            Categories.REPTILE,
            Categories.SNAKE,
        ],
        num_legs=0,
    ),
    PokemonGen3.GLIGAR: Pokemon(
        name=PokemonGen3.GLIGAR,
        gen=2,
        types=[Types.GROUND, Types.FLYING],
        colors=[Colors.PINK, Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=75,
            defence=105,
            special_attack=35,
            special_defence=65,
        ),
        categories=[
            Categories.BUG,
        ],
        num_legs=2,
    ),
    PokemonGen3.STEELIX: Pokemon(
        name=PokemonGen3.STEELIX,
        gen=2,
        types=[Types.STEEL, Types.GROUND],
        colors=[Colors.GRAY],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=85,
            defence=200,
            special_attack=55,
            special_defence=65,
        ),
        categories=[
            Categories.REPTILE,
            Categories.SNAKE,
        ],
        num_legs=0,
    ),
    PokemonGen3.SNUBBULL: Pokemon(
        name=PokemonGen3.SNUBBULL,
        gen=2,
        types=[Types.NORMAL],
        evolves_to=[
            Evolution(name=PokemonGen3.GRANBULL)
        ],
        colors=[Colors.PINK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=85,
            defence=50,
            special_attack=40,
            special_defence=40,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.DOG,
        ],
        num_legs=2,
    ),
    PokemonGen3.GRANBULL: Pokemon(
        name=PokemonGen3.GRANBULL,
        gen=2,
        types=[Types.NORMAL],
        colors=[Colors.PINK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=120,
            defence=75,
            special_attack=60,
            special_defence=60,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.DOG,
        ],
        num_legs=2,
    ),
    PokemonGen3.QWILFISH: Pokemon(
        name=PokemonGen3.QWILFISH,
        gen=2,
        types=[Types.WATER, Types.POISON],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        colors=[Colors.BLUE, Colors.YELLOW],
        stats=Stats(
            attack=95,
            defence=85,
            special_attack=55,
            special_defence=55,
        ),
        categories=[
            Categories.WATERMON,
            Categories.FISH,
        ],
        num_legs=0,
    ),
    PokemonGen3.SCIZOR: Pokemon(
        name=PokemonGen3.SCIZOR,
        gen=2,
        types=[Types.BUG, Types.STEEL],
        colors=[Colors.RED],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=130,
            defence=100,
            special_attack=55,
            special_defence=80,
        ),
        categories=[
            Categories.WING,
            Categories.BUG,
            Categories.WEAPON,
        ],
        num_legs=2,
    ),
    PokemonGen3.SHUCKLE: Pokemon(
        name=PokemonGen3.SHUCKLE,
        gen=2,
        types=[Types.BUG, Types.ROCK],
        colors=[Colors.RED, Colors.YELLOW, Colors.WHITE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=10,
            defence=230,
            special_attack=10,
            special_defence=230,
        ),
        categories=[
            Categories.REPTILE,
            Categories.FOOD,
            Categories.TURTLE,
        ],
        num_legs=4,
    ),
    PokemonGen3.HERACROSS: Pokemon(
        name=PokemonGen3.HERACROSS,
        gen=2,
        types=[Types.BUG, Types.FIGHTING],
        colors=[Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=125,
            defence=75,
            special_attack=40,
            special_defence=95,
        ),
        categories=[
            Categories.WING,
            Categories.BUG,
        ],
        num_legs=2,
    ),
    PokemonGen3.SNEASEL: Pokemon(
        name=PokemonGen3.SNEASEL,
        gen=2,
        types=[Types.DARK, Types.ICE],
        colors=[Colors.PURPLE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=95,
            defence=55,
            special_attack=35,
            special_defence=75,
        ),
        categories=[
            Categories.MAMMAL,
        ],
        num_legs=2,
    ),
    PokemonGen3.TEDDIURSA: Pokemon(
        name=PokemonGen3.TEDDIURSA,
        gen=2,
        types=[Types.NORMAL],
        evolves_to=[
            Evolution(name=PokemonGen3.URSARING)
        ],
        colors=[Colors.BROWN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=80,
            defence=50,
            special_attack=50,
            special_defence=50,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.BEAR,
        ],
        num_legs=2,
    ),
    PokemonGen3.URSARING: Pokemon(
        name=PokemonGen3.URSARING,
        gen=2,
        types=[Types.NORMAL],
        colors=[Colors.BROWN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=130,
            defence=75,
            special_attack=75,
            special_defence=75,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.BEAR,
        ],
        num_legs=2,
    ),
    PokemonGen3.SLUGMA: Pokemon(
        name=PokemonGen3.SLUGMA,
        gen=2,
        types=[Types.FIRE],
        colors=[Colors.RED],
        evolves_to=[
            Evolution(name=PokemonGen3.MAGCARGO)
        ],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=40,
            defence=40,
            special_attack=70,
            special_defence=40,
        ),
        categories=[
            Categories.FOOD,
            Categories.BUG,
        ],
        num_legs=0,
    ),
    PokemonGen3.MAGCARGO: Pokemon(
        name=PokemonGen3.MAGCARGO,
        gen=2,
        types=[Types.FIRE, Types.ROCK],
        colors=[Colors.RED, Colors.GRAY],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=50,
            defence=120,
            special_attack=90,
            special_defence=80,
        ),
        categories=[
            Categories.FOOD,
            Categories.BUG,
        ],
        num_legs=0,
    ),
    PokemonGen3.SWINUB: Pokemon(
        name=PokemonGen3.SWINUB,
        gen=2,
        types=[Types.ICE, Types.GROUND],
        evolves_to=[
            Evolution(name=PokemonGen3.PILOSWINE)
        ],
        colors=[Colors.BROWN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=50,
            defence=40,
            special_attack=30,
            special_defence=30,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.FOOD,
            Categories.PIG,
        ],
        num_legs=4,
    ),
    PokemonGen3.PILOSWINE: Pokemon(
        name=PokemonGen3.PILOSWINE,
        gen=2,
        types=[Types.ICE, Types.GROUND],
        colors=[Colors.BROWN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=100,
            defence=80,
            special_attack=60,
            special_defence=60,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.FOOD,
            Categories.PIG,
            Categories.PREHISTORIC,
        ],
        num_legs=4,
    ),
    PokemonGen3.CORSOLA: Pokemon(
        name=PokemonGen3.CORSOLA,
        gen=2,
        types=[Types.WATER, Types.ROCK],
        colors=[Colors.PINK, Colors.WHITE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=55,
            defence=95,
            special_attack=65,
            special_defence=95,
        ),
        categories=[
            Categories.ITEM,
            Categories.WATERMON,
        ],
        num_legs=4,
    ),
    PokemonGen3.REMORAID: Pokemon(
        name=PokemonGen3.REMORAID,
        gen=2,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen3.OCTILLERY)
        ],
        colors=[Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=65,
            defence=35,
            special_attack=65,
            special_defence=35,
        ),
        categories=[
            Categories.WATERMON,
            Categories.FISH,
        ],
        num_legs=0,
    ),
    PokemonGen3.OCTILLERY: Pokemon(
        name=PokemonGen3.OCTILLERY,
        gen=2,
        types=[Types.WATER],
        colors=[Colors.RED],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=105,
            defence=75,
            special_attack=105,
            special_defence=75,
        ),
        categories=[
            Categories.WATERMON,
            Categories.FOOD,
        ],
        num_legs=0,
    ),
    PokemonGen3.DELIBIRD: Pokemon(
        name=PokemonGen3.DELIBIRD,
        gen=2,
        types=[Types.ICE, Types.FLYING],
        colors=[Colors.RED, Colors.WHITE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=55,
            defence=45,
            special_attack=65,
            special_defence=45,
        ),
        categories=[
            Categories.BIRD,
            Categories.FANTASY,
        ],
        num_legs=2,
    ),
    PokemonGen3.MANTINE: Pokemon(
        name=PokemonGen3.MANTINE,
        gen=2,
        types=[Types.WATER, Types.FLYING],
        colors=[Colors.PURPLE, Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=40,
            defence=70,
            special_attack=80,
            special_defence=140,
        ),
        categories=[
            Categories.WATERMON,
            Categories.FISH,
            Categories.WING,
            Categories.FOOD,
        ],
        num_legs=0,
    ),
    PokemonGen3.SKARMORY: Pokemon(
        name=PokemonGen3.SKARMORY,
        gen=2,
        types=[Types.STEEL, Types.FLYING],
        colors=[Colors.GRAY, Colors.RED],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=80,
            defence=140,
            special_attack=40,
            special_defence=70,
        ),
        categories=[
            Categories.WING,
            Categories.ITEM,
            Categories.WEAPON,
        ],
        num_legs=2,
    ),
    PokemonGen3.HOUNDOUR: Pokemon(
        name=PokemonGen3.HOUNDOUR,
        gen=2,
        types=[Types.DARK, Types.FIRE],
        evolves_to=[
            Evolution(name=PokemonGen3.HOUNDOOM)
        ],
        colors=[Colors.BLACK, Colors.RED, Colors.WHITE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=60,
            defence=30,
            special_attack=80,
            special_defence=50,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.DOG,
        ],
        num_legs=4,
    ),
    PokemonGen3.HOUNDOOM: Pokemon(
        name=PokemonGen3.HOUNDOOM,
        gen=2,
        types=[Types.DARK, Types.FIRE],
        colors=[Colors.BLACK, Colors.RED, Colors.WHITE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=90,
            defence=50,
            special_attack=110,
            special_defence=80,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.DOG,
        ],
        num_legs=4,
    ),
    PokemonGen3.KINGDRA: Pokemon(
        name=PokemonGen3.KINGDRA,
        gen=2,
        types=[Types.WATER, Types.DRAGON],
        colors=[Colors.BLUE, Colors.YELLOW],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=95,
            defence=95,
            special_attack=95,
            special_defence=95,
        ),
        categories=[
            Categories.WATERMON,
            Categories.FISH,
            Categories.DRAGON,
        ],
        num_legs=0,
    ),
    PokemonGen3.PHANPY: Pokemon(
        name=PokemonGen3.PHANPY,
        gen=2,
        types=[Types.GROUND],
        evolves_to=[
            Evolution(name=PokemonGen3.DONPHAN)
        ],
        colors=[Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=60,
            defence=60,
            special_attack=40,
            special_defence=40,
        ),
        categories=[
            Categories.MAMMAL,
        ],
        num_legs=4,
    ),
    PokemonGen3.DONPHAN: Pokemon(
        name=PokemonGen3.DONPHAN,
        gen=2,
        types=[Types.GROUND],
        colors=[Colors.GRAY, Colors.BLACK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=120,
            defence=120,
            special_attack=60,
            special_defence=60,
        ),
        categories=[
            Categories.MAMMAL,
        ],
        num_legs=4,
    ),
    PokemonGen3.PORYGON2: Pokemon(
        name=PokemonGen3.PORYGON2,
        gen=2,
        types=[Types.NORMAL],
        colors=[Colors.PINK, Colors.BLUE],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=80,
            defence=90,
            special_attack=105,
            special_defence=95,
        ),
        categories=[
            Categories.ITEM,
        ],
        num_legs=0,
    ),
    PokemonGen3.STANTLER: Pokemon(
        name=PokemonGen3.STANTLER,
        gen=2,
        types=[Types.NORMAL],
        colors=[Colors.BROWN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=95,
            defence=62,
            special_attack=85,
            special_defence=65,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.FOOD,
        ],
        num_legs=4,
    ),
    PokemonGen3.SMEARGLE: Pokemon(
        name=PokemonGen3.SMEARGLE,
        gen=2,
        types=[Types.NORMAL],
        colors=[Colors.WHITE, Colors.BROWN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=20,
            defence=35,
            special_attack=20,
            special_defence=45,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.DOG,
        ],
        num_legs=2,
    ),
    PokemonGen3.TYROGUE: Pokemon(
        name=PokemonGen3.TYROGUE,
        gen=2,
        types=[Types.FIGHTING],
        evolves_to=[
            Evolution(name='Hitmontop', evolution_type=EvolutionType.RANDOM, special_information="Attack = Defense", level=20),
            Evolution(name='Hitmonchan', evolution_type=EvolutionType.RANDOM, special_information="Attack < Defense", level=20),
            Evolution(name='Hitmonlee', evolution_type=EvolutionType.RANDOM, special_information="Attack > Defense", level=20),
        ],
        colors=[Colors.PURPLE, Colors.BROWN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=35,
            defence=35,
            special_attack=35,
            special_defence=35,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.HUMAN,
        ],
        num_legs=2,
    ),
    PokemonGen3.HITMONTOP: Pokemon(
        name=PokemonGen3.HITMONTOP,
        gen=2,
        types=[Types.FIGHTING],
        colors=[Colors.BROWN, Colors.BLUE],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=95,
            defence=95,
            special_attack=35,
            special_defence=110,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.HUMAN,
        ],
        num_legs=2,
    ),
    PokemonGen3.SMOOCHUM: Pokemon(
        name=PokemonGen3.SMOOCHUM,
        gen=2,
        types=[Types.ICE, Types.PSYCHIC],
        evolves_to=[
            Evolution(name=PokemonGen3.JYNX)
        ],
        colors=[Colors.PURPLE, Colors.YELLOW],
        supported_genders=[Genders.FEMALE],
        stats=Stats(
            attack=30,
            defence=15,
            special_attack=85,
            special_defence=65,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.FANTASY,
            Categories.HUMAN,
        ],
        num_legs=2,
    ),
    PokemonGen3.ELEKID: Pokemon(
        name=PokemonGen3.ELEKID,
        gen=2,
        types=[Types.ELECTRIC],
        evolves_to=[
            Evolution(name=PokemonGen3.ELECTABUZZ)
        ],
        colors=[Colors.YELLOW, Colors.BLACK],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=63,
            defence=37,
            special_attack=65,
            special_defence=55,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.HUMAN,
            Categories.ITEM,
        ],
        num_legs=2,
    ),
    PokemonGen3.MAGBY: Pokemon(
        name=PokemonGen3.MAGBY,
        gen=2,
        types=[Types.FIRE],
        evolves_to=[
            Evolution(name=PokemonGen3.MAGMAR)
        ],
        colors=[Colors.RED, Colors.YELLOW],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=75,
            defence=37,
            special_attack=70,
            special_defence=55,
        ),
        categories=[
            Categories.BIRD,
            Categories.WATERMON,
            Categories.FOOD,
            Categories.DUCK,
        ],
        num_legs=2,
    ),
    PokemonGen3.MILTANK: Pokemon(
        name=PokemonGen3.MILTANK,
        gen=2,
        types=[Types.NORMAL],
        colors=[Colors.PINK, Colors.WHITE],
        supported_genders=[Genders.FEMALE],
        stats=Stats(
            attack=80,
            defence=105,
            special_attack=40,
            special_defence=70,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.FOOD,
            Categories.CATTLE,
            Categories.COW,
        ],
        num_legs=4,
    ),
    PokemonGen3.BLISSEY: Pokemon(
        name=PokemonGen3.BLISSEY,
        gen=2,
        types=[Types.NORMAL],
        colors=[Colors.PINK, Colors.WHITE],
        supported_genders=[Genders.FEMALE],
        stats=Stats(
            attack=10,
            defence=10,
            special_attack=75,
            special_defence=135,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.FOOD,
            Categories.HUMAN,
        ],
        num_legs=2,
    ),
    PokemonGen3.RAIKOU: Pokemon(
        name=PokemonGen3.RAIKOU,
        gen=2,
        types=[Types.ELECTRIC],
        colors=[Colors.YELLOW, Colors.BLACK,Colors.WHITE],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=85,
            defence=75,
            special_attack=115,
            special_defence=100,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.CAT,
        ],
        num_legs=4,
    ),
    PokemonGen3.ENTEI: Pokemon(
        name=PokemonGen3.ENTEI,
        gen=2,
        types=[Types.FIRE],
        colors=[Colors.BROWN, Colors.GRAY, Colors.WHITE],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=115,
            defence=85,
            special_attack=90,
            special_defence=75,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.CAT,
        ],
        num_legs=4,
    ),
    PokemonGen3.SUICUNE: Pokemon(
        name=PokemonGen3.SUICUNE,
        gen=2,
        types=[Types.WATER],
        colors=[Colors.BLUE, Colors.WHITE, Colors.PURPLE],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=75,
            defence=115,
            special_attack=90,
            special_defence=115,
        ),
        categories=[
            Categories.MAMMAL,
            Categories.CAT,
        ],
        num_legs=4,
    ),
    PokemonGen3.LARVITAR: Pokemon(
        name=PokemonGen3.LARVITAR,
        gen=2,
        types=[Types.ROCK, Types.GROUND],
        evolves_to=[
            Evolution(name=PokemonGen3.PUPITAR)
        ],
        colors=[Colors.GREEN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=64,
            defence=50,
            special_attack=45,
            special_defence=50,
        ),
        categories=[
            Categories.PREHISTORIC,
            Categories.REPTILE,
            Categories.FANTASY,
        ],
        num_legs=2,
    ),
    PokemonGen3.PUPITAR: Pokemon(
        name=PokemonGen3.PUPITAR,
        gen=2,
        types=[Types.ROCK, Types.GROUND],
        evolves_to=[
            Evolution(name=PokemonGen3.TYRANITAR)
        ],
        colors=[Colors.GRAY],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=84,
            defence=70,
            special_attack=65,
            special_defence=70,
        ),
        categories=[
            Categories.PREHISTORIC,
            Categories.REPTILE,
            Categories.FANTASY,
        ],
        num_legs=0,
    ),
    PokemonGen3.TYRANITAR: Pokemon(
        name=PokemonGen3.TYRANITAR,
        gen=2,
        types=[Types.ROCK, Types.DARK],
        colors=[Colors.GREEN],
        supported_genders=[Genders.MALE, Genders.FEMALE],
        stats=Stats(
            attack=134,
            defence=110,
            special_attack=95,
            special_defence=100,
        ),
        categories=[
            Categories.PREHISTORIC,
            Categories.REPTILE,
            Categories.FANTASY,
        ],
        num_legs=2,
    ),
    PokemonGen3.LUGIA: Pokemon(
        name=PokemonGen3.LUGIA,
        gen=2,
        types=[Types.PSYCHIC, Types.FLYING],
        colors=[Colors.WHITE, Colors.BLUE],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=90,
            defence=130,
            special_attack=90,
            special_defence=154,
        ),
        categories=[
            Categories.WING,
            Categories.DRAGON,
        ],
        num_legs=2,
    ),
    PokemonGen3.HO_OH: Pokemon(
        name=PokemonGen3.HO_OH,
        gen=2,
        types=[Types.FIRE, Types.FLYING],
        colors=[Colors.RED, Colors.WHITE],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=130,
            defence=90,
            special_attack=110,
            special_defence=154,
        ),
        categories=[
            Categories.WING,
            Categories.BIRD,
        ],
        num_legs=2,
    ),
    PokemonGen3.CELEBI: Pokemon(
        name=PokemonGen3.CELEBI,
        gen=2,
        types=[Types.PSYCHIC, Types.GRASS],
        colors=[Colors.GREEN],
        supported_genders=[Genders.GENDERLESS],
        stats=Stats(
            attack=100,
            defence=100,
            special_attack=100,
            special_defence=100,
        ),
        categories=[
            Categories.WING,
            Categories.FANTASY,
        ],
        num_legs=2,
    ),
}
