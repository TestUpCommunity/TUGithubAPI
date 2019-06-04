from core.rest_client import RestClient


class Runs(RestClient):

    def list_check_runs(self, owner, repo, ref, **kwargs):
        """
        https://developer.github.com/v3/checks/runs/#list-check-runs-for-a-specific-ref
        """
        headers = {'Accept': 'application/vnd.github.antiope-preview+json'}
        return self.get("/repos/{}/{}/commits/{}/check-runs".format(owner, repo, ref), headers=headers, **kwargs)
