from core.rest_client import RestClient
from api.checks.runs import Runs


class Checks(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(Checks, self).__init__(api_root_url, **kwargs)
        self.runs = Runs(self.api_root_url, **kwargs)
