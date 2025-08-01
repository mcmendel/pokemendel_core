"""Generation 2 Pokemon data module."""

from ..models.pokemon import Pokemon
from ..models.evolution.evolution import Evolution
from ..models.evolution.evolution_type import EvolutionType
from ..models.evolution.items import Item
from ..utils.definitions.types import Types
from ..utils.definitions.colors import Colors
from ..utils.definitions.categories import Categories
from ..utils.definitions.stats import Stats
from ..utils.definitions.genders import Genders


class PokemonGen2:
    """Generation 1 and 2 Pokémon names.
    
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
    PokemonGen2.BULBASAUR: Pokemon(
        name=PokemonGen2.BULBASAUR,
        gen=2,  # All Pokemon in gen2.py should be gen=2 as this represents their Gen 2 data
        types=[Types.GRASS, Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen2.IVYSAUR)
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
    ),
    PokemonGen2.IVYSAUR: Pokemon(
        name=PokemonGen2.IVYSAUR,
        gen=2,  # All Pokemon in gen2.py should be gen=2 as this represents their Gen 2 data
        types=[Types.GRASS, Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen2.VENUSAUR)
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
    ),
    PokemonGen2.VENUSAUR: Pokemon(
        name=PokemonGen2.VENUSAUR,
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
    ),
    PokemonGen2.CHARMANDER: Pokemon(
        name=PokemonGen2.CHARMANDER,
        gen=2,
        types=[Types.FIRE],
        evolves_to=[
            Evolution(name=PokemonGen2.CHARMELEON)
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
    ),
    PokemonGen2.CHARMELEON: Pokemon(
        name=PokemonGen2.CHARMELEON,
        gen=2,
        types=[Types.FIRE],
        evolves_to=[
            Evolution(name=PokemonGen2.CHARIZARD)
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
    ),
    PokemonGen2.CHARIZARD: Pokemon(
        name=PokemonGen2.CHARIZARD,
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
    ),
    PokemonGen2.SQUIRTLE: Pokemon(
        name=PokemonGen2.SQUIRTLE,
        gen=2,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen2.WARTORTLE)
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
    ),
    PokemonGen2.WARTORTLE: Pokemon(
        name=PokemonGen2.WARTORTLE,
        gen=2,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen2.BLASTOISE)
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
    ),
    PokemonGen2.BLASTOISE: Pokemon(
        name=PokemonGen2.BLASTOISE,
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
    ),
    PokemonGen2.CATERPIE: Pokemon(
        name=PokemonGen2.CATERPIE,
        gen=2,
        types=[Types.BUG],
        evolves_to=[
            Evolution(name=PokemonGen2.METAPOD)
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
    ),
    PokemonGen2.METAPOD: Pokemon(
        name=PokemonGen2.METAPOD,
        gen=2,
        types=[Types.BUG],
        evolves_to=[
            Evolution(name=PokemonGen2.BUTTERFREE)
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
    ),
    PokemonGen2.BUTTERFREE: Pokemon(
        name=PokemonGen2.BUTTERFREE,
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
    ),
    PokemonGen2.WEEDLE: Pokemon(
        name=PokemonGen2.WEEDLE,
        gen=2,
        types=[Types.BUG, Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen2.KAKUNA)
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
    ),
    PokemonGen2.KAKUNA: Pokemon(
        name=PokemonGen2.KAKUNA,
        gen=2,
        types=[Types.BUG, Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen2.BEEDRILL)
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
    ),
    PokemonGen2.BEEDRILL: Pokemon(
        name=PokemonGen2.BEEDRILL,
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
    ),
    PokemonGen2.PIDGEY: Pokemon(
        name=PokemonGen2.PIDGEY,
        gen=2,
        types=[Types.NORMAL, Types.FLYING],
        evolves_to=[
            Evolution(name=PokemonGen2.PIDGEOTTO)
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
    ),
    PokemonGen2.PIDGEOTTO: Pokemon(
        name=PokemonGen2.PIDGEOTTO,
        gen=2,
        types=[Types.NORMAL, Types.FLYING],
        evolves_to=[
            Evolution(name=PokemonGen2.PIDGEOT)
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
    ),
    PokemonGen2.PIDGEOT: Pokemon(
        name=PokemonGen2.PIDGEOT,
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
    ),
    PokemonGen2.RATTATA: Pokemon(
        name=PokemonGen2.RATTATA,
        gen=2,
        types=[Types.NORMAL],
        evolves_to=[
            Evolution(name=PokemonGen2.RATICATE)
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
    ),
    PokemonGen2.RATICATE: Pokemon(
        name=PokemonGen2.RATICATE,
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
    ),
    PokemonGen2.SPEAROW: Pokemon(
        name=PokemonGen2.SPEAROW,
        gen=2,
        types=[Types.NORMAL, Types.FLYING],
        evolves_to=[
            Evolution(name=PokemonGen2.FEAROW)
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
    ),
    PokemonGen2.FEAROW: Pokemon(
        name=PokemonGen2.FEAROW,
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
    ),
    PokemonGen2.EKANS: Pokemon(
        name=PokemonGen2.EKANS,
        gen=2,
        types=[Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen2.ARBOK)
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
    ),
    PokemonGen2.ARBOK: Pokemon(
        name=PokemonGen2.ARBOK,
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
    ),
    PokemonGen2.PIKACHU: Pokemon(
        name=PokemonGen2.PIKACHU,
        gen=2,
        types=[Types.ELECTRIC],
        evolves_to=[
            Evolution(name=PokemonGen2.RAICHU, level=41, evolution_type=EvolutionType.STONE, item=Item.THUNDER_STONE)
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
    ),
    PokemonGen2.RAICHU: Pokemon(
        name=PokemonGen2.RAICHU,
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
    ),
    PokemonGen2.SANDSHREW: Pokemon(
        name=PokemonGen2.SANDSHREW,
        gen=2,
        types=[Types.GROUND],
        evolves_to=[
            Evolution(name=PokemonGen2.SANDSLASH)
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
    ),
    PokemonGen2.SANDSLASH: Pokemon(
        name=PokemonGen2.SANDSLASH,
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
    ),
    PokemonGen2.NIDORAN_F: Pokemon(
        name=PokemonGen2.NIDORAN_F,
        gen=2,
        types=[Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen2.NIDORINA)
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
    ),
    PokemonGen2.NIDORINA: Pokemon(
        name=PokemonGen2.NIDORINA,
        gen=2,
        types=[Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen2.NIDOQUEEN, level=19, evolution_type=EvolutionType.STONE, item=Item.MOON_STONE)
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
    ),
    PokemonGen2.NIDOQUEEN: Pokemon(
        name=PokemonGen2.NIDOQUEEN,
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
    ),
    PokemonGen2.NIDORAN_M: Pokemon(
        name=PokemonGen2.NIDORAN_M,
        gen=2,
        types=[Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen2.NIDORINO)
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
    ),
    PokemonGen2.NIDORINO: Pokemon(
        name=PokemonGen2.NIDORINO,
        gen=2,
        types=[Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen2.NIDOKING, level=19, evolution_type=EvolutionType.STONE, item=Item.MOON_STONE)
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
    ),
    PokemonGen2.NIDOKING: Pokemon(
        name=PokemonGen2.NIDOKING,
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
    ),
    PokemonGen2.CLEFAIRY: Pokemon(
        name=PokemonGen2.CLEFAIRY,
        gen=2,
        types=[Types.NORMAL],
        evolves_to=[
            Evolution(name=PokemonGen2.CLEFABLE, level=34, item=Item.MOON_STONE, evolution_type=EvolutionType.STONE)
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
    ),
    PokemonGen2.CLEFABLE: Pokemon(
        name=PokemonGen2.CLEFABLE,
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
    ),
    PokemonGen2.VULPIX: Pokemon(
        name=PokemonGen2.VULPIX,
        gen=2,
        types=[Types.FIRE],
        evolves_to=[
            Evolution(name=PokemonGen2.NINETALES, level=31, evolution_type=EvolutionType.STONE, item=Item.FIRE_STONE)
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
    ),
    PokemonGen2.NINETALES: Pokemon(
        name=PokemonGen2.NINETALES,
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
    ),
    PokemonGen2.JIGGLYPUFF: Pokemon(
        name=PokemonGen2.JIGGLYPUFF,
        gen=2,
        types=[Types.NORMAL],
        evolves_to=[
            Evolution(name=PokemonGen2.WIGGLYTUFF, level=34, evolution_type=EvolutionType.STONE, item=Item.MOON_STONE)
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
    ),
    PokemonGen2.WIGGLYTUFF: Pokemon(
        name=PokemonGen2.WIGGLYTUFF,
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
    ),
    PokemonGen2.ZUBAT: Pokemon(
        name=PokemonGen2.ZUBAT,
        gen=2,
        types=[Types.POISON, Types.FLYING],
        evolves_to=[
            Evolution(name=PokemonGen2.GOLBAT)
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
    ),
    PokemonGen2.GOLBAT: Pokemon(
        name=PokemonGen2.GOLBAT,
        gen=2,
        types=[Types.POISON, Types.FLYING],
        evolves_to=[Evolution(name=PokemonGen2.CROBAT, evolution_type=EvolutionType.FRIENDSHIP,)],
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
    ),
    PokemonGen2.ODDISH: Pokemon(
        name=PokemonGen2.ODDISH,
        gen=2,
        types=[Types.GRASS, Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen2.GLOOM)
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
    ),
    PokemonGen2.GLOOM: Pokemon(
        name=PokemonGen2.GLOOM,
        gen=2,
        types=[Types.GRASS, Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen2.VILEPLUME, level=44, evolution_type=EvolutionType.STONE, item=Item.LEAF_STONE),
            Evolution(name=PokemonGen2.BELLOSSOM, level=44, evolution_type=EvolutionType.STONE, item=Item.SUN_STONE)
        ],
        colors=[Colors.BLUE, Colors.RED],
        categories=[
            Categories.PLANT,
        ],
        num_legs=2,
    ),
    PokemonGen2.VILEPLUME: Pokemon(
        name=PokemonGen2.VILEPLUME,
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
    ),
    PokemonGen2.PARAS: Pokemon(
        name=PokemonGen2.PARAS,
        gen=2,
        types=[Types.BUG, Types.GRASS],
        evolves_to=[
            Evolution(name=PokemonGen2.PARASECT)
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
    ),
    PokemonGen2.PARASECT: Pokemon(
        name=PokemonGen2.PARASECT,
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
    ),
    PokemonGen2.VENONAT: Pokemon(
        name=PokemonGen2.VENONAT,
        gen=2,
        types=[Types.BUG, Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen2.VENOMOTH)
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
    ),
    PokemonGen2.VENOMOTH: Pokemon(
        name=PokemonGen2.VENOMOTH,
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
    ),
    PokemonGen2.DIGLETT: Pokemon(
        name=PokemonGen2.DIGLETT,
        gen=2,
        types=[Types.GROUND],
        evolves_to=[
            Evolution(name=PokemonGen2.DUGTRIO)
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
    ),
    PokemonGen2.DUGTRIO: Pokemon(
        name=PokemonGen2.DUGTRIO,
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
    ),
    PokemonGen2.MEOWTH: Pokemon(
        name=PokemonGen2.MEOWTH,
        gen=2,
        types=[Types.NORMAL],
        evolves_to=[
            Evolution(name=PokemonGen2.PERSIAN)
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
    ),
    PokemonGen2.PERSIAN: Pokemon(
        name=PokemonGen2.PERSIAN,
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
    ),
    PokemonGen2.PSYDUCK: Pokemon(
        name=PokemonGen2.PSYDUCK,
        gen=2,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen2.GOLDUCK)
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
    ),
    PokemonGen2.GOLDUCK: Pokemon(
        name=PokemonGen2.GOLDUCK,
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
    ),
    PokemonGen2.MANKEY: Pokemon(
        name=PokemonGen2.MANKEY,
        gen=2,
        types=[Types.FIGHTING],
        evolves_to=[
            Evolution(name=PokemonGen2.PRIMEAPE)
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
    ),
    PokemonGen2.PRIMEAPE: Pokemon(
        name=PokemonGen2.PRIMEAPE,
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
    ),
    PokemonGen2.GROWLITHE: Pokemon(
        name=PokemonGen2.GROWLITHE,
        gen=2,
        types=[Types.FIRE],
        evolves_to=[
            Evolution(name=PokemonGen2.ARCANINE, level=50, evolution_type=EvolutionType.STONE, item=Item.FIRE_STONE)
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
    ),
    PokemonGen2.ARCANINE: Pokemon(
        name=PokemonGen2.ARCANINE,
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
    ),
    PokemonGen2.POLIWAG: Pokemon(
        name=PokemonGen2.POLIWAG,
        gen=2,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen2.POLIWHIRL)
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
    ),
    PokemonGen2.POLIWHIRL: Pokemon(
        name=PokemonGen2.POLIWHIRL,
        gen=2,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen2.POLIWRATH, level=35, evolution_type=EvolutionType.STONE, item=Item.WATER_STONE),
            Evolution(name=PokemonGen2.POLITOED, evolution_type=EvolutionType.TRADE, should_hold=True, item=Item.KINGS_ROCK)
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
    ),
    PokemonGen2.POLIWRATH: Pokemon(
        name=PokemonGen2.POLIWRATH,
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
    ),
    PokemonGen2.ABRA: Pokemon(
        name=PokemonGen2.ABRA,
        gen=2,
        types=[Types.PSYCHIC],
        evolves_to=[
            Evolution(name=PokemonGen2.KADABRA)
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
    ),
    PokemonGen2.KADABRA: Pokemon(
        name=PokemonGen2.KADABRA,
        gen=2,
        types=[Types.PSYCHIC],
        evolves_to=[
            Evolution(name=PokemonGen2.ALAKAZAM, evolution_type=EvolutionType.TRADE)
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
    ),
    PokemonGen2.ALAKAZAM: Pokemon(
        name=PokemonGen2.ALAKAZAM,
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
    ),
    PokemonGen2.MACHOP: Pokemon(
        name=PokemonGen2.MACHOP,
        gen=2,
        types=[Types.FIGHTING],
        evolves_to=[
            Evolution(name=PokemonGen2.MACHOKE)
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
    ),
    PokemonGen2.MACHOKE: Pokemon(
        name=PokemonGen2.MACHOKE,
        gen=2,
        types=[Types.FIGHTING],
        evolves_to=[
            Evolution(name=PokemonGen2.MACHAMP, evolution_type=EvolutionType.TRADE)
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
    ),
    PokemonGen2.MACHAMP: Pokemon(
        name=PokemonGen2.MACHAMP,
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
    ),
    PokemonGen2.BELLSPROUT: Pokemon(
        name=PokemonGen2.BELLSPROUT,
        gen=2,
        types=[Types.GRASS, Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen2.WEEPINBELL)
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
    ),
    PokemonGen2.WEEPINBELL: Pokemon(
        name=PokemonGen2.WEEPINBELL,
        gen=2,
        types=[Types.GRASS, Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen2.VICTREEBEL, level=54, evolution_type=EvolutionType.STONE, item=Item.LEAF_STONE)
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
    ),
    PokemonGen2.VICTREEBEL: Pokemon(
        name=PokemonGen2.VICTREEBEL,
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
    ),
    PokemonGen2.TENTACOOL: Pokemon(
        name=PokemonGen2.TENTACOOL,
        gen=2,
        types=[Types.WATER, Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen2.TENTACRUEL)
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
    ),
    PokemonGen2.TENTACRUEL: Pokemon(
        name=PokemonGen2.TENTACRUEL,
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
    ),
    PokemonGen2.GEODUDE: Pokemon(
        name=PokemonGen2.GEODUDE,
        gen=2,
        types=[Types.ROCK, Types.GROUND],
        evolves_to=[
            Evolution(name=PokemonGen2.GRAVELER)
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
    ),
    PokemonGen2.GRAVELER: Pokemon(
        name=PokemonGen2.GRAVELER,
        gen=2,
        types=[Types.ROCK, Types.GROUND],
        evolves_to=[
            Evolution(name=PokemonGen2.GOLEM, evolution_type=EvolutionType.TRADE)
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
    ),
    PokemonGen2.GOLEM: Pokemon(
        name=PokemonGen2.GOLEM,
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
    ),
    PokemonGen2.PONYTA: Pokemon(
        name=PokemonGen2.PONYTA,
        gen=2,
        types=[Types.FIRE],
        evolves_to=[
            Evolution(name=PokemonGen2.RAPIDASH)
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
    ),
    PokemonGen2.RAPIDASH: Pokemon(
        name=PokemonGen2.RAPIDASH,
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
    ),
    PokemonGen2.SLOWPOKE: Pokemon(
        name=PokemonGen2.SLOWPOKE,
        gen=2,
        types=[Types.WATER, Types.PSYCHIC],
        evolves_to=[
            Evolution(name=PokemonGen2.SLOWBRO),
            Evolution(name=PokemonGen2.SLOWKING, evolution_type=EvolutionType.TRADE, should_hold=True, item=Item.KINGS_ROCK)
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
    ),
    PokemonGen2.SLOWBRO: Pokemon(
        name=PokemonGen2.SLOWBRO,
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
    ),
    PokemonGen2.MAGNEMITE: Pokemon(
        name=PokemonGen2.MAGNEMITE,
        gen=2,
        types=[Types.ELECTRIC, Types.STEEL],
        evolves_to=[
            Evolution(name=PokemonGen2.MAGNETON)
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
    ),
    PokemonGen2.MAGNETON: Pokemon(
        name=PokemonGen2.MAGNETON,
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
    ),
    PokemonGen2.FARFETCHD: Pokemon(
        name=PokemonGen2.FARFETCHD,
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
    ),
    PokemonGen2.DODUO: Pokemon(
        name=PokemonGen2.DODUO,
        gen=2,
        types=[Types.NORMAL, Types.FLYING],
        evolves_to=[
            Evolution(name=PokemonGen2.DODRIO)
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
    ),
    PokemonGen2.DODRIO: Pokemon(
        name=PokemonGen2.DODRIO,
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
    ),
    PokemonGen2.SEEL: Pokemon(
        name=PokemonGen2.SEEL,
        gen=2,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen2.DEWGONG)
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
    ),
    PokemonGen2.DEWGONG: Pokemon(
        name=PokemonGen2.DEWGONG,
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
    ),
    PokemonGen2.GRIMER: Pokemon(
        name=PokemonGen2.GRIMER,
        gen=2,
        types=[Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen2.MUK)
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
    ),
    PokemonGen2.MUK: Pokemon(
        name=PokemonGen2.MUK,
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
    ),
    PokemonGen2.SHELLDER: Pokemon(
        name=PokemonGen2.SHELLDER,
        gen=2,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen2.CLOYSTER, level=49, evolution_type=EvolutionType.STONE, item=Item.WATER_STONE)
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
    ),
    PokemonGen2.CLOYSTER: Pokemon(
        name=PokemonGen2.CLOYSTER,
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
    ),
    PokemonGen2.GASTLY: Pokemon(
        name=PokemonGen2.GASTLY,
        gen=2,
        types=[Types.GHOST, Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen2.HAUNTER)
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
    ),
    PokemonGen2.HAUNTER: Pokemon(
        name=PokemonGen2.HAUNTER,
        gen=2,
        types=[Types.GHOST, Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen2.GENGAR, evolution_type=EvolutionType.TRADE)
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
    ),
    PokemonGen2.GENGAR: Pokemon(
        name=PokemonGen2.GENGAR,
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
    ),
    PokemonGen2.ONIX: Pokemon(
        name=PokemonGen2.ONIX,
        gen=2,
        types=[Types.ROCK, Types.GROUND],
        evolves_to=[Evolution(name=PokemonGen2.STEELIX, evolution_type=EvolutionType.TRADE, item=Item.METAL_COAT, should_hold=True)],
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
    ),
    PokemonGen2.DROWZEE: Pokemon(
        name=PokemonGen2.DROWZEE,
        gen=2,
        types=[Types.PSYCHIC],
        evolves_to=[
            Evolution(name=PokemonGen2.HYPNO)
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
    ),
    PokemonGen2.HYPNO: Pokemon(
        name=PokemonGen2.HYPNO,
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
    ),
    PokemonGen2.KRABBY: Pokemon(
        name=PokemonGen2.KRABBY,
        gen=2,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen2.KINGLER)
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
    ),
    PokemonGen2.KINGLER: Pokemon(
        name=PokemonGen2.KINGLER,
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
    ),
    PokemonGen2.VOLTORB: Pokemon(
        name=PokemonGen2.VOLTORB,
        gen=2,
        types=[Types.ELECTRIC],
        evolves_to=[
            Evolution(name=PokemonGen2.ELECTRODE)
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
    ),
    PokemonGen2.ELECTRODE: Pokemon(
        name=PokemonGen2.ELECTRODE,
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
    ),
    PokemonGen2.EXEGGCUTE: Pokemon(
        name=PokemonGen2.EXEGGCUTE,
        gen=2,
        types=[Types.GRASS, Types.PSYCHIC],
        evolves_to=[
            Evolution(name=PokemonGen2.EXEGGUTOR, level=43, evolution_type=EvolutionType.STONE, item=Item.LEAF_STONE)
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
    ),
    PokemonGen2.EXEGGUTOR: Pokemon(
        name=PokemonGen2.EXEGGUTOR,
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
    ),
    PokemonGen2.CUBONE: Pokemon(
        name=PokemonGen2.CUBONE,
        gen=2,
        types=[Types.GROUND],
        evolves_to=[
            Evolution(name=PokemonGen2.MAROWAK)
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
    ),
    PokemonGen2.MAROWAK: Pokemon(
        name=PokemonGen2.MAROWAK,
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
    ),
    PokemonGen2.HITMONLEE: Pokemon(
        name=PokemonGen2.HITMONLEE,
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
    ),
    PokemonGen2.HITMONCHAN: Pokemon(
        name=PokemonGen2.HITMONCHAN,
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
    ),
    PokemonGen2.LICKITUNG: Pokemon(
        name=PokemonGen2.LICKITUNG,
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
    ),
    PokemonGen2.KOFFING: Pokemon(
        name=PokemonGen2.KOFFING,
        gen=2,
        types=[Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen2.WEEZING)
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
    ),
    PokemonGen2.WEEZING: Pokemon(
        name=PokemonGen2.WEEZING,
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
    ),
    PokemonGen2.RHYHORN: Pokemon(
        name=PokemonGen2.RHYHORN,
        gen=2,
        types=[Types.GROUND, Types.ROCK],
        evolves_to=[
            Evolution(name=PokemonGen2.RHYDON)
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
    ),
    PokemonGen2.RHYDON: Pokemon(
        name=PokemonGen2.RHYDON,
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
    ),
    PokemonGen2.CHANSEY: Pokemon(
        name=PokemonGen2.CHANSEY,
        gen=2,
        types=[Types.NORMAL],
        evolves_to=[
            Evolution(name=PokemonGen2.BLISSEY, evolution_type=EvolutionType.FRIENDSHIP, level=47)
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
    ),
    PokemonGen2.TANGELA: Pokemon(
        name=PokemonGen2.TANGELA,
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
    ),
    PokemonGen2.KANGASKHAN: Pokemon(
        name=PokemonGen2.KANGASKHAN,
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
    ),
    PokemonGen2.HORSEA: Pokemon(
        name=PokemonGen2.HORSEA,
        gen=2,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen2.SEADRA)
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
    ),
    PokemonGen2.SEADRA: Pokemon(
        name=PokemonGen2.SEADRA,
        gen=2,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen2.KINGDRA, evolution_type=EvolutionType.TRADE, item=Item.DRAGON_SCALE, should_hold=True)
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
    ),
    PokemonGen2.GOLDEEN: Pokemon(
        name=PokemonGen2.GOLDEEN,
        gen=2,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen2.SEAKING)
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
    ),
    PokemonGen2.SEAKING: Pokemon(
        name=PokemonGen2.SEAKING,
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
    ),
    PokemonGen2.STARYU: Pokemon(
        name=PokemonGen2.STARYU,
        gen=2,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen2.STARMIE, level=31, item=Item.WATER_STONE, evolution_type=EvolutionType.STONE)
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
    ),
    PokemonGen2.STARMIE: Pokemon(
        name=PokemonGen2.STARMIE,
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
    ),
    PokemonGen2.MR_MIME: Pokemon(
        name=PokemonGen2.MR_MIME,
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
    ),
    PokemonGen2.SCYTHER: Pokemon(
        name=PokemonGen2.SCYTHER,
        gen=2,
        types=[Types.BUG, Types.FLYING],
        evolves_to=[
            Evolution(name=PokemonGen2.SCIZOR, evolution_type=EvolutionType.TRADE, item=Item.MOON_STONE, should_hold=True),
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
    ),
    PokemonGen2.JYNX: Pokemon(
        name=PokemonGen2.JYNX,
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
    ),
    PokemonGen2.ELECTABUZZ: Pokemon(
        name=PokemonGen2.ELECTABUZZ,
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
    ),
    PokemonGen2.MAGMAR: Pokemon(
        name=PokemonGen2.MAGMAR,
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
    ),
    PokemonGen2.PINSIR: Pokemon(
        name=PokemonGen2.PINSIR,
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
    ),
    PokemonGen2.TAUROS: Pokemon(
        name=PokemonGen2.TAUROS,
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
    ),
    PokemonGen2.MAGIKARP: Pokemon(
        name=PokemonGen2.MAGIKARP,
        gen=2,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen2.GYARADOS)
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
    ),
    PokemonGen2.GYARADOS: Pokemon(
        name=PokemonGen2.GYARADOS,
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
    ),
    PokemonGen2.LAPRAS: Pokemon(
        name=PokemonGen2.LAPRAS,
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
    ),
    PokemonGen2.DITTO: Pokemon(
        name=PokemonGen2.DITTO,
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
    ),
    PokemonGen2.EEVEE: Pokemon(
        name=PokemonGen2.EEVEE,
        gen=2,
        types=[Types.NORMAL],
        evolves_to=[
            Evolution(name=PokemonGen2.VAPOREON, evolution_type=EvolutionType.STONE, item=Item.WATER_STONE),
            Evolution(name=PokemonGen2.JOLTEON, evolution_type=EvolutionType.STONE, item=Item.THUNDER_STONE),
            Evolution(name=PokemonGen2.FLAREON, evolution_type=EvolutionType.STONE, item=Item.FIRE_STONE),
            Evolution(name=PokemonGen2.UMBREON, evolution_type=EvolutionType.FRIENDSHIP, special_information="Nighttime"),
            Evolution(name=PokemonGen2.ESPEON, evolution_type=EvolutionType.FRIENDSHIP, special_information="Daytime"),
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
    ),
    PokemonGen2.VAPOREON: Pokemon(
        name=PokemonGen2.VAPOREON,
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
    ),
    PokemonGen2.JOLTEON: Pokemon(
        name=PokemonGen2.JOLTEON,
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
    ),
    PokemonGen2.FLAREON: Pokemon(
        name=PokemonGen2.FLAREON,
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
    ),
    PokemonGen2.PORYGON: Pokemon(
        name=PokemonGen2.PORYGON,
        gen=2,
        types=[Types.NORMAL],
        evolves_to=[
            Evolution(name=PokemonGen2.PORYGON2, evolution_type=EvolutionType.TRADE, item=Item.UPGRADE, should_hold=True)
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
    ),
    PokemonGen2.OMANYTE: Pokemon(
        name=PokemonGen2.OMANYTE,
        gen=2,
        types=[Types.ROCK, Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen2.OMASTAR)
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
    ),
    PokemonGen2.OMASTAR: Pokemon(
        name=PokemonGen2.OMASTAR,
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
    ),
    PokemonGen2.KABUTO: Pokemon(
        name=PokemonGen2.KABUTO,
        gen=2,
        types=[Types.ROCK, Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen2.KABUTOPS)
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
    ),
    PokemonGen2.KABUTOPS: Pokemon(
        name=PokemonGen2.KABUTOPS,
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
    ),
    PokemonGen2.AERODACTYL: Pokemon(
        name=PokemonGen2.AERODACTYL,
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
    ),
    PokemonGen2.SNORLAX: Pokemon(
        name=PokemonGen2.SNORLAX,
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
    ),
    PokemonGen2.ARTICUNO: Pokemon(
        name=PokemonGen2.ARTICUNO,
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
    ),
    PokemonGen2.ZAPDOS: Pokemon(
        name=PokemonGen2.ZAPDOS,
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
    ),
    PokemonGen2.MOLTRES: Pokemon(
        name=PokemonGen2.MOLTRES,
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
    ),
    PokemonGen2.DRATINI: Pokemon(
        name=PokemonGen2.DRATINI,
        gen=2,
        types=[Types.DRAGON],
        evolves_to=[
            Evolution(name=PokemonGen2.DRAGONAIR)
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
    ),
    PokemonGen2.DRAGONAIR: Pokemon(
        name=PokemonGen2.DRAGONAIR,
        gen=2,
        types=[Types.DRAGON],
        evolves_to=[
            Evolution(name=PokemonGen2.DRAGONITE)
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
    ),
    PokemonGen2.DRAGONITE: Pokemon(
        name=PokemonGen2.DRAGONITE,
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
    ),
    PokemonGen2.MEWTWO: Pokemon(
        name=PokemonGen2.MEWTWO,
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
    ),
    PokemonGen2.MEW: Pokemon(
        name=PokemonGen2.MEW,
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
    ),
    PokemonGen2.CHIKORITA: Pokemon(
        name=PokemonGen2.CHIKORITA,
        gen=2,
        types=[Types.GRASS],
        evolves_to=[
            Evolution(name=PokemonGen2.BAYLEEF)
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
    PokemonGen2.BAYLEEF: Pokemon(
        name=PokemonGen2.BAYLEEF,
        gen=2,
        types=[Types.GRASS],
        evolves_to=[
            Evolution(name=PokemonGen2.MEGANIUM)
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
    PokemonGen2.MEGANIUM: Pokemon(
        name=PokemonGen2.MEGANIUM,
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
    PokemonGen2.CYNDAQUIL: Pokemon(
        name=PokemonGen2.CYNDAQUIL,
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
    PokemonGen2.QUILAVA: Pokemon(
        name=PokemonGen2.QUILAVA,
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
    PokemonGen2.TYPHLOSION: Pokemon(
        name=PokemonGen2.TYPHLOSION,
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
    PokemonGen2.TOTODILE: Pokemon(
        name=PokemonGen2.TOTODILE,
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
    PokemonGen2.CROCONAW: Pokemon(
        name=PokemonGen2.CROCONAW,
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
    PokemonGen2.FERALIGATR: Pokemon(
        name=PokemonGen2.FERALIGATR,
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
    PokemonGen2.SENTRET: Pokemon(
        name=PokemonGen2.SENTRET,
        gen=2,
        types=[Types.NORMAL],
        evolves_to=[
            Evolution(name=PokemonGen2.FURRET)
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
    PokemonGen2.FURRET: Pokemon(
        name=PokemonGen2.FURRET,
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
    PokemonGen2.HOOTHOOT: Pokemon(
        name=PokemonGen2.HOOTHOOT,
        gen=2,
        types=[Types.NORMAL, Types.FLYING],
        evolves_to=[
            Evolution(name=PokemonGen2.NOCTOWL)
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
    PokemonGen2.NOCTOWL: Pokemon(
        name=PokemonGen2.NOCTOWL,
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
    PokemonGen2.LEDYBA: Pokemon(
        name=PokemonGen2.LEDYBA,
        gen=2,
        types=[Types.BUG, Types.FLYING],
        evolves_to=[
            Evolution(name=PokemonGen2.LEDIAN)
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
    PokemonGen2.LEDIAN: Pokemon(
        name=PokemonGen2.LEDIAN,
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
    PokemonGen2.SPINARAK: Pokemon(
        name=PokemonGen2.SPINARAK,
        gen=2,
        types=[Types.BUG, Types.POISON],
        evolves_to=[
            Evolution(name=PokemonGen2.ARIADOS)
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
    PokemonGen2.ARIADOS: Pokemon(
        name=PokemonGen2.ARIADOS,
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
    PokemonGen2.CROBAT: Pokemon(
        name=PokemonGen2.CROBAT,
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
    PokemonGen2.CHINCHOU: Pokemon(
        name=PokemonGen2.CHINCHOU,
        gen=2,
        types=[Types.WATER, Types.ELECTRIC],
        evolves_to=[
            Evolution(name=PokemonGen2.LANTURN)
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
    PokemonGen2.LANTURN: Pokemon(
        name=PokemonGen2.LANTURN,
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
    PokemonGen2.PICHU: Pokemon(
        name=PokemonGen2.PICHU,
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
    PokemonGen2.CLEFFA: Pokemon(
        name=PokemonGen2.CLEFFA,
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
    PokemonGen2.IGGLYBUFF: Pokemon(
        name=PokemonGen2.IGGLYBUFF,
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
    PokemonGen2.TOGEPI: Pokemon(
        name=PokemonGen2.TOGEPI,
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
    PokemonGen2.TOGETIC: Pokemon(
        name=PokemonGen2.TOGETIC,
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
    PokemonGen2.NATU: Pokemon(
        name=PokemonGen2.NATU,
        gen=2,
        types=[Types.PSYCHIC, Types.FLYING],
        evolves_to=[
            Evolution(name=PokemonGen2.XATU)
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
    PokemonGen2.XATU: Pokemon(
        name=PokemonGen2.XATU,
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
    PokemonGen2.MAREEP: Pokemon(
        name=PokemonGen2.MAREEP,
        gen=2,
        types=[Types.ELECTRIC],
        evolves_to=[
            Evolution(name=PokemonGen2.FLAAFFY)
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
    PokemonGen2.FLAAFFY: Pokemon(
        name=PokemonGen2.FLAAFFY,
        gen=2,
        types=[Types.ELECTRIC],
        evolves_to=[
            Evolution(name=PokemonGen2.AMPHAROS)
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
    PokemonGen2.AMPHAROS: Pokemon(
        name=PokemonGen2.AMPHAROS,
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
    PokemonGen2.BELLOSSOM: Pokemon(
        name=PokemonGen2.BELLOSSOM,
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
    PokemonGen2.MARILL: Pokemon(
        name=PokemonGen2.MARILL,
        gen=2,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen2.AZUMARILL)
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
    PokemonGen2.AZUMARILL: Pokemon(
        name=PokemonGen2.AZUMARILL,
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
    PokemonGen2.SUDOWOODO: Pokemon(
        name=PokemonGen2.SUDOWOODO,
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
    PokemonGen2.POLITOED: Pokemon(
        name=PokemonGen2.POLITOED,
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
    PokemonGen2.HOPPIP: Pokemon(
        name=PokemonGen2.HOPPIP,
        gen=2,
        types=[Types.GRASS, Types.FLYING],
        evolves_to=[
            Evolution(name=PokemonGen2.SKIPLOOM)
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
    PokemonGen2.SKIPLOOM: Pokemon(
        name=PokemonGen2.SKIPLOOM,
        gen=2,
        types=[Types.GRASS, Types.FLYING],
        evolves_to=[
            Evolution(name=PokemonGen2.JUMPLUFF)
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
    PokemonGen2.JUMPLUFF: Pokemon(
        name=PokemonGen2.JUMPLUFF,
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
    PokemonGen2.AIPOM: Pokemon(
        name=PokemonGen2.AIPOM,
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
    PokemonGen2.SUNKERN: Pokemon(
        name=PokemonGen2.SUNKERN,
        gen=2,
        types=[Types.GRASS],
        evolves_to=[
            Evolution(name=PokemonGen2.SUNFLORA)
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
    PokemonGen2.SUNFLORA: Pokemon(
        name=PokemonGen2.SUNFLORA,
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
    PokemonGen2.YANMA: Pokemon(
        name=PokemonGen2.YANMA,
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
    PokemonGen2.WOOPER: Pokemon(
        name=PokemonGen2.WOOPER,
        gen=2,
        types=[Types.WATER, Types.GROUND],
        evolves_to=[
            Evolution(name=PokemonGen2.QUAGSIRE)
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
    PokemonGen2.QUAGSIRE: Pokemon(
        name=PokemonGen2.QUAGSIRE,
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
    PokemonGen2.ESPEON: Pokemon(
        name=PokemonGen2.ESPEON,
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
    PokemonGen2.UMBREON: Pokemon(
        name=PokemonGen2.UMBREON,
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
    PokemonGen2.MURKROW: Pokemon(
        name=PokemonGen2.MURKROW,
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
    PokemonGen2.SLOWKING: Pokemon(
        name=PokemonGen2.SLOWKING,
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
    PokemonGen2.MISDREAVUS: Pokemon(
        name=PokemonGen2.MISDREAVUS,
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
    PokemonGen2.UNOWN: Pokemon(
        name=PokemonGen2.UNOWN,
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
    PokemonGen2.WOBBUFFET: Pokemon(
        name=PokemonGen2.WOBBUFFET,
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
    PokemonGen2.GIRAFARIG: Pokemon(
        name=PokemonGen2.GIRAFARIG,
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
    PokemonGen2.PINECO: Pokemon(
        name=PokemonGen2.PINECO,
        gen=2,
        types=[Types.BUG],
        evolves_to=[
            Evolution(name=PokemonGen2.FORRETRESS)
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
    PokemonGen2.FORRETRESS: Pokemon(
        name=PokemonGen2.FORRETRESS,
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
    PokemonGen2.DUNSPARCE: Pokemon(
        name=PokemonGen2.DUNSPARCE,
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
    PokemonGen2.GLIGAR: Pokemon(
        name=PokemonGen2.GLIGAR,
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
    PokemonGen2.STEELIX: Pokemon(
        name=PokemonGen2.STEELIX,
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
    PokemonGen2.SNUBBULL: Pokemon(
        name=PokemonGen2.SNUBBULL,
        gen=2,
        types=[Types.NORMAL],
        evolves_to=[
            Evolution(name=PokemonGen2.GRANBULL)
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
    PokemonGen2.GRANBULL: Pokemon(
        name=PokemonGen2.GRANBULL,
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
    PokemonGen2.QWILFISH: Pokemon(
        name=PokemonGen2.QWILFISH,
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
    PokemonGen2.SCIZOR: Pokemon(
        name=PokemonGen2.SCIZOR,
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
    PokemonGen2.SHUCKLE: Pokemon(
        name=PokemonGen2.SHUCKLE,
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
    PokemonGen2.HERACROSS: Pokemon(
        name=PokemonGen2.HERACROSS,
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
    PokemonGen2.SNEASEL: Pokemon(
        name=PokemonGen2.SNEASEL,
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
    PokemonGen2.TEDDIURSA: Pokemon(
        name=PokemonGen2.TEDDIURSA,
        gen=2,
        types=[Types.NORMAL],
        evolves_to=[
            Evolution(name=PokemonGen2.URSARING)
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
    PokemonGen2.URSARING: Pokemon(
        name=PokemonGen2.URSARING,
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
    PokemonGen2.SLUGMA: Pokemon(
        name=PokemonGen2.SLUGMA,
        gen=2,
        types=[Types.FIRE],
        colors=[Colors.RED],
        evolves_to=[
            Evolution(name=PokemonGen2.MAGCARGO)
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
    PokemonGen2.MAGCARGO: Pokemon(
        name=PokemonGen2.MAGCARGO,
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
    PokemonGen2.SWINUB: Pokemon(
        name=PokemonGen2.SWINUB,
        gen=2,
        types=[Types.ICE, Types.GROUND],
        evolves_to=[
            Evolution(name=PokemonGen2.PILOSWINE)
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
    PokemonGen2.PILOSWINE: Pokemon(
        name=PokemonGen2.PILOSWINE,
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
    PokemonGen2.CORSOLA: Pokemon(
        name=PokemonGen2.CORSOLA,
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
    PokemonGen2.REMORAID: Pokemon(
        name=PokemonGen2.REMORAID,
        gen=2,
        types=[Types.WATER],
        evolves_to=[
            Evolution(name=PokemonGen2.OCTILLERY)
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
    PokemonGen2.OCTILLERY: Pokemon(
        name=PokemonGen2.OCTILLERY,
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
    PokemonGen2.DELIBIRD: Pokemon(
        name=PokemonGen2.DELIBIRD,
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
    PokemonGen2.MANTINE: Pokemon(
        name=PokemonGen2.MANTINE,
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
    PokemonGen2.SKARMORY: Pokemon(
        name=PokemonGen2.SKARMORY,
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
    PokemonGen2.HOUNDOUR: Pokemon(
        name=PokemonGen2.HOUNDOUR,
        gen=2,
        types=[Types.DARK, Types.FIRE],
        evolves_to=[
            Evolution(name=PokemonGen2.HOUNDOOM)
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
    PokemonGen2.HOUNDOOM: Pokemon(
        name=PokemonGen2.HOUNDOOM,
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
    PokemonGen2.KINGDRA: Pokemon(
        name=PokemonGen2.KINGDRA,
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
    PokemonGen2.PHANPY: Pokemon(
        name=PokemonGen2.PHANPY,
        gen=2,
        types=[Types.GROUND],
        evolves_to=[
            Evolution(name=PokemonGen2.DONPHAN)
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
    PokemonGen2.DONPHAN: Pokemon(
        name=PokemonGen2.DONPHAN,
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
    PokemonGen2.PORYGON2: Pokemon(
        name=PokemonGen2.PORYGON2,
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
    PokemonGen2.STANTLER: Pokemon(
        name=PokemonGen2.STANTLER,
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
    PokemonGen2.SMEARGLE: Pokemon(
        name=PokemonGen2.SMEARGLE,
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
    PokemonGen2.TYROGUE: Pokemon(
        name=PokemonGen2.TYROGUE,
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
    PokemonGen2.HITMONTOP: Pokemon(
        name=PokemonGen2.HITMONTOP,
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
    PokemonGen2.SMOOCHUM: Pokemon(
        name=PokemonGen2.SMOOCHUM,
        gen=2,
        types=[Types.ICE, Types.PSYCHIC],
        evolves_to=[
            Evolution(name=PokemonGen2.JYNX)
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
    PokemonGen2.ELEKID: Pokemon(
        name=PokemonGen2.ELEKID,
        gen=2,
        types=[Types.ELECTRIC],
        evolves_to=[
            Evolution(name=PokemonGen2.ELECTABUZZ)
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
    PokemonGen2.MAGBY: Pokemon(
        name=PokemonGen2.MAGBY,
        gen=2,
        types=[Types.FIRE],
        evolves_to=[
            Evolution(name=PokemonGen2.MAGMAR)
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
    PokemonGen2.MILTANK: Pokemon(
        name=PokemonGen2.MILTANK,
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
    PokemonGen2.BLISSEY: Pokemon(
        name=PokemonGen2.BLISSEY,
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
    PokemonGen2.RAIKOU: Pokemon(
        name=PokemonGen2.RAIKOU,
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
    PokemonGen2.ENTEI: Pokemon(
        name=PokemonGen2.ENTEI,
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
    PokemonGen2.SUICUNE: Pokemon(
        name=PokemonGen2.SUICUNE,
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
    PokemonGen2.LARVITAR: Pokemon(
        name=PokemonGen2.LARVITAR,
        gen=2,
        types=[Types.ROCK, Types.GROUND],
        evolves_to=[
            Evolution(name=PokemonGen2.PUPITAR)
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
    PokemonGen2.PUPITAR: Pokemon(
        name=PokemonGen2.PUPITAR,
        gen=2,
        types=[Types.ROCK, Types.GROUND],
        evolves_to=[
            Evolution(name=PokemonGen2.TYRANITAR)
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
    PokemonGen2.TYRANITAR: Pokemon(
        name=PokemonGen2.TYRANITAR,
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
    PokemonGen2.LUGIA: Pokemon(
        name=PokemonGen2.LUGIA,
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
    PokemonGen2.HO_OH: Pokemon(
        name=PokemonGen2.HO_OH,
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
    PokemonGen2.CELEBI: Pokemon(
        name=PokemonGen2.CELEBI,
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
