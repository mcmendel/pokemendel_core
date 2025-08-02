from .gen1 import NAME_TO_POKEMON as GEN1_NAME_TO_POKEMON, Pokemon
from .gen2 import NAME_TO_POKEMON as GEN2_NAME_TO_POKEMON
from .gen3 import NAME_TO_POKEMON as GEN3_NAME_TO_POKEMON

__all__ = ["GEN1_NAME_TO_POKEMON", "GEN2_NAME_TO_POKEMON"]


def fetch_pokemon(name: str, gen: int) -> Pokemon:
    if gen == 1:
        return GEN1_NAME_TO_POKEMON[name]
    elif gen == 2:
        return GEN2_NAME_TO_POKEMON[name]
    elif gen == 3:
        return GEN3_NAME_TO_POKEMON[name]
    raise ValueError(f"No data for generation {gen}")


def list_gen_pokemons(gen: int) -> list[Pokemon]:
    if gen == 1:
        return GEN1_NAME_TO_POKEMON.values()
    elif gen == 2:
        return GEN2_NAME_TO_POKEMON.values()
    elif gen == 3:
        return GEN3_NAME_TO_POKEMON.values()
    raise ValueError(f"No data for generation {gen}")
