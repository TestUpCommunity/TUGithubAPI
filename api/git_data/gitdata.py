from core.rest_client import RestClient
from api.git_data.refs import Refs


class GitData(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(GitData, self).__init__(api_root_url, **kwargs)
        self.refs = Refs(self.api_root_url, **kwargs)
