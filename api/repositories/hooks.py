from core.rest_client import RestClient


class Hooks(RestClient):
    def list_hooks(self,owner,repo, **kwargs):
        """
        https://developer.github.com/v3/repos/hooks#list-hooks
        """
        return self.get("/repos/{}/{}/hooks".format(owner, repo), **kwargs)