from blockchain.utils import Utils
from blockchain.pos.lot import Lot


class ProofOfStake():

    def __init__(self):
        self.stakers = {}
        self.set_genesis_node_stake()

    def set_genesis_node_stake(self):
        genesis_publickey = open('keys/genesisPublicKey.pem', 'r').read()
        self.stakers[genesis_publickey] = 1

    def update(self, public_key: str, stake):
        if public_key in self.stakers.keys():
            self.stakers[public_key] += stake
        else:
            self.stakers[public_key] = stake

    def get(self, public_key: str):
        if public_key in self.stakers.keys():
            return self.stakers[public_key]
        else:
            return None

    def validator_lots(self, seed):
        lots = []
        for validator in self.stakers.keys():
            for stake in range(self.get(validator)):
                lots.append(Lot(validator, stake+1, seed))
        return lots

    def winner_lot(self, lots, seed):
        winner_lot = None
        least_offset = None
        reference_hash_int = int(Utils.hash(seed).hexdigest(), 16)
        for lot in lots:
            lot_int = int(lot.lot_hash(), 16)
            offset = abs(lot_int - reference_hash_int)
            if least_offset is None or offset < least_offset:
                least_offset = offset
                winner_lot = lot
        return winner_lot

    def forger(self, last_block_hash):
        lots = self.validator_lots(last_block_hash)
        winner_lot = self.winner_lot(lots, last_block_hash)
        return winner_lot.public_key
