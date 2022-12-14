
class Message():

    def __init__(self, sender_connector, message_types, data):
        self.sender_connector = sender_connector
        self.message_types = message_types
        self.data = data
