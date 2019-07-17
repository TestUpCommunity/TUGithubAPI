from core.rest_client import RestClient
from api.interactions.orgs import Orgs
from api.interactions.repos import Repos


class Interactions(RestClient):
    """
    https://developer.github.com/v3/interactions/#interactions
    """

    def __init__(self, api_root_url, **kwargs):
        super(Interactions, self).__init__(api_root_url, **kwargs)
        self.orgs = Orgs(self.api_root_url, **kwargs)
        self.repos = Repos(self.api_root_url, **kwargs)
