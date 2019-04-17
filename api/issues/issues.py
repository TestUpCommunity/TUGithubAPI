from core.rest_client import RestClient


class Issues(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(Issues, self).__init__(api_root_url, **kwargs)

    def create_issue(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/issues/#create-an-issue
        """
        return self.post("/repos/{}/{}/issues".format(owner, repo), **kwargs)
