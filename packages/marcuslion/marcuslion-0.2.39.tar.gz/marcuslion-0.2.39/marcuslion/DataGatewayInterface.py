from marcuslion.restcontroller import RestController


class DataGatewayInterface(RestController):
    def __init__(self, url):
        super().__init__(url)

    def list(self):
        pass

    def search(self, query, params):
        pass

    def query(self, ident):
        pass

    def metadata(self, ident):
        pass

    def download(self, ident, params):
        pass

    def subscribe(self, ident, params):
        pass
