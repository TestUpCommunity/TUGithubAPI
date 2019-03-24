from core.rest_client import RestClient


class Repos(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(Repos, self).__init__(api_root_url, **kwargs)

    def list_your_repos(self, visibility=None, affiliation=None, type=None, sort=None, direction=None):
        params = {"visibility": visibility, "affiliation": affiliation, "type": type, "direction": direction}
        return self.get("/user/repos", params=params)
