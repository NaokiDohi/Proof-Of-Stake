
class SocketConnector():

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def equals(self, connector):
        if connector.host == self.host and connector.port == self.port:
            return True
        else:
            return False
