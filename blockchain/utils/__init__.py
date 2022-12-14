import json
import jsonpickle
from Crypto.Hash import SHA256


class Utils():

    @staticmethod
    def hash(data):
        data_string = json.dumps(data)  # dict => string
        data_bytes = data_string.encode('utf-8')  # string => bytes
        data_hash = SHA256.new(data_bytes)
        return data_hash

    @staticmethod
    def encode(object):
        return jsonpickle.encode(object)

    @staticmethod
    def decode(object):
        return jsonpickle.decode(object)
