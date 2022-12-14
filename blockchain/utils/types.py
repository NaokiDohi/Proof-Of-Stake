from enum import Enum


class TransactionTypes(str, Enum):
    STAKE = "STAKE"
    EXCHANGE = "EXCHANGE"
    TRANFER = "TRANFER"
