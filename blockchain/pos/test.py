import sys  # noqa
import os  # noqa
sys.path.append("../../")  # noqa
from blockchain.pos import ProofOfStake
from blockchain.pos.lot import Lot

if __name__ == '__main__':
    # pos = ProofOfStake()
    # pos.update('Alice', 100)
    # pos.update('Bob', 10)
    # print(
    #     f'Alice:{pos.get("Alice")}\
    #     \nBob:{pos.get("Bob")}\
    #     \nJack:{pos.get("Jack")}'
    # )
    lot = Lot('bob', 1, 'lastHash')
    print(lot.lot_hash())
