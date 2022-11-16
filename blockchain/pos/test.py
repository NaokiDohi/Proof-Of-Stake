import os  # noqa
import sys  # noqa
import string
import random
sys.path.append("../../")  # noqa
from blockchain.pos import ProofOfStake
from blockchain.pos.lot import Lot


def get_random(length) -> str:
    letters = string.ascii_lowercase
    result: str = ''.join(random.choice(letters) for i in range(length))
    return result


if __name__ == '__main__':
    pos = ProofOfStake()
    pos.update('Alice', 100)
    pos.update('Bob', 10)
    print(
        f'Alice:{pos.get("Alice")}\
        \nBob:{pos.get("Bob")}\
        \nJack:{pos.get("Jack")}'
    )

    alice_wins = 0
    bob_wins = 0

    for i in range(100):
        forger = pos.forger(get_random(i))
        if forger == 'Alice':
            alice_wins += 1
        elif forger == 'Bob':
            bob_wins += 1

    print(f'Alice won:{alice_wins}times\nBob won:{bob_wins}times')
