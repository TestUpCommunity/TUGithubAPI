from core.rest_client import RestClient


class Hooks(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(Hooks, self).__init__(api_root_url, **kwargs)

    def list_hooks(self,owner,repo, **kwargs):
        """
        https://developer.github.com/v3/repos/hooks#list-hooks
        """
        return self.get("/repos/{}/{}/hooks".format(owner, repo), **kwargs)