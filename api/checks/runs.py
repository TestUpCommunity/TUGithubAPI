from core.rest_client import RestClient
from copy import deepcopy


class Runs(RestClient):

    def list_check_runs(self, owner, repo, ref, **kwargs):
        """
        https://developer.github.com/v3/checks/runs/#list-check-runs-for-a-specific-ref
        """
        copied_headers = deepcopy(self.session.headers)
        copied_headers['Accept'] = 'application/vnd.github.antiope-preview+json'
        return self.get("/repos/{}/{}/commits/{}/check-runs".format(owner, repo, ref), headers=copied_headers, **kwargs)
