from core.rest_client import RestClient


class Issues(RestClient):

    def create_issue(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/issues/#create-an-issue
        """
        return self.post("/repos/{}/{}/issues".format(owner, repo), **kwargs)
