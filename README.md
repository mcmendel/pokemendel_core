# Pokemendel Core

A Python package for Pokémon-related functionality, providing comprehensive data structures and utilities for working with Pokémon from Generations 1 and 2.

## Features

- Complete Pokémon data for Generation 1 (151 Pokémon) and Generation 2 (251 Pokémon total)
- Detailed information for each Pokémon including:
  - Types (including new Dark and Steel types in Gen 2)
  - Base stats
  - Evolution chains
  - Gender ratios
  - Colors and categories
  - Physical characteristics
- Support for special cases:
  - Baby Pokémon (e.g., Pichu, Cleffa)
  - New evolution methods (friendship, time-based, etc.)
  - Special naming conventions (e.g., "Ho-oh", "Porygon2")
  - Gender-specific forms (e.g., "Nidoran-F", "Nidoran-M")

## Installation

```bash
pip install -e .
```

## Usage

```python
from pokemendel_core.data.gen2 import PokemonGen2, NAME_TO_POKEMON

# Get a specific Pokémon
tyranitar = NAME_TO_POKEMON[PokemonGen2.TYRANITAR]
print(f"Tyranitar's types: {[t.value for t in tyranitar.types]}")  # ['ROCK', 'DARK']

# Check evolution chain
houndour = NAME_TO_POKEMON[PokemonGen2.HOUNDOUR]
evolution = houndour.evolves_to[0]
print(f"{houndour.name} evolves to {evolution.name}")  # "Houndour evolves to Houndoom"

# Get Pokémon stats
umbreon = NAME_TO_POKEMON[PokemonGen2.UMBREON]
print(f"Umbreon's special defence: {umbreon.stats.special_defence}")  # 130

# Check supported genders
scizor = NAME_TO_POKEMON[PokemonGen2.SCIZOR]
print(f"Scizor can be: {[g.value for g in scizor.supported_genders]}")  # ['MALE', 'FEMALE']
```

## Development

To set up the development environment:

1. Clone the repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
4. Install development dependencies: `pip install -e ".[dev]"`
5. Install package: `python -m build`
6. From other project: `pip install -e /Users/nirmendel/work/pokemendel_core` or `cp dist/pokemendel_core-0.*-py3-none-any.whl /Users/nirmendel/work/local_pypi/`

### Running Tests

To run the test suite:

```bash
python -m pytest
```

To run specific test files:

```bash
python -m pytest tests/data/test_gen1.py  # Test Gen 1 implementation
python -m pytest tests/data/test_gen2.py  # Test Gen 2 implementation
```

## Data Structure

The package uses a consistent data structure for both generations:

- `PokemonGen2`: Class containing string constants for all 251 Pokémon names
- `NAME_TO_POKEMON`: Dictionary mapping Pokémon names to their full data objects
- `Pokemon`: Data class containing all Pokémon attributes:
  - `name`: String name of the Pokémon
  - `gen`: Generation number (1 or 2)
  - `types`: List of Types enum values
  - `evolves_to`: List of Evolution objects (if any)
  - `colors`: List of Colors enum values
  - `supported_genders`: List of Genders enum values
  - `stats`: Stats object with attack, defence, special_attack, special_defence
  - `categories`: List of Categories enum values
  - `num_legs`: Integer number of legs
