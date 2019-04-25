from core.rest_client import RestClient


class Traffic(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(Traffic, self).__init__(api_root_url, **kwargs)

    def list_referrers(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/traffic/#list-referrers
        """
        return self.get("/repos/{}/{}/traffic/popular/referrers".format(owner, repo), **kwargs)