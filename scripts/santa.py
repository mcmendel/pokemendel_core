from copy import copy
from typing import Tuple, Optional
import random
PEOPLE = {"Vera", "Nir", "Yamit", "Nadav", "Rimon", "Yuvi"}


def _match_last_two_people(receivers: set, givers: set) -> Tuple[Tuple[str, str], Tuple[str, str]]:
    receiver1 = receivers.pop()
    receiver2 = receivers.pop()
    giver1 = givers.pop()
    giver2 = givers.pop()
    assert not givers
    assert not receivers

    if receiver1 in {giver1, giver2}:
        if receiver1 == giver1:
            return (giver1, receiver2), (giver2, receiver1)
        return (giver1, receiver1), (giver2, receiver2)
    if receiver2 in {giver1, giver2}:
        if receiver2 == giver1:
            return (giver1, receiver1), (giver2, receiver2)
        return (giver1, receiver2), (giver2, receiver1)
    return (giver1, receiver1), (giver2, receiver2)


def _match_santa(receivers: set, givers: set) -> Optional[Tuple[str, str]]:
    if len(receivers) == 2:
        return

    santa = random.choice(list(givers))
    potential_receivers = {receiver for receiver in receivers if receiver != santa}
    santa_receiver = random.choice(list(potential_receivers))
    receivers.remove(santa_receiver)
    givers.remove(santa)
    return santa, santa_receiver


def set_secret_santa(people: set) -> dict:
    assert len(people) > 2, "Can't set secret santa for less than 3 people"
    secret_santa_map = dict()
    receives = copy(people)
    givers = copy(people)
    santa_map = _match_santa(receives, givers)
    while santa_map:
        santa, secret = santa_map
        secret_santa_map[santa] = secret
        santa_map = _match_santa(receives, givers)

    assert len(receives) == len(givers) == 2
    for santa, secret in _match_last_two_people(receives, givers):
        secret_santa_map[santa] = secret

    return secret_santa_map


if __name__ == "__main__":
    santa_map = set_secret_santa(PEOPLE)
    with open("./santa.txt", 'w') as f:
        f.writelines([
            f"{k} -> {v}\n"
            for k, v in santa_map.items()
        ])
