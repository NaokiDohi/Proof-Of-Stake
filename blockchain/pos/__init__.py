
class ProofOfStake():

    def __init__(self):
        self.stakers = {}

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
