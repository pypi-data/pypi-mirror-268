class Config:

    def __init__(self):
        self._api_key = None

    @property
    def api_key(self):
        if self._api_key is None:
            raise ValueError("API Key has not been set.")
        return self._api_key

    @api_key.setter
    def api_key(self, value):
        self._api_key = value

    def initialize(self, api_key):
        self.api_key = api_key

config = Config()
