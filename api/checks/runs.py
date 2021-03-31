from core.rest_client import RestClient

class Runs(RestClient):

    def list_check_runs(self,owner,repo,ref, **kwargs):
        """
        https://docs.github.com/en/rest/reference/checks#list-check-runs-for-a-git-reference
        """
         return self.get("/repos/{}/{}/commits/{}/check-runs".format(owner,repo,ref), **kwargs)

