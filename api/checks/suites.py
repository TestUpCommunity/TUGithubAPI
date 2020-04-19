from core.rest_client import RestClient
from copy import deepcopy


class Suites(RestClient):
    def list_check_suites(self, owner, repo, ref, **kwargs):
        """
        https://developer.github.com/v3/checks/suites/#list-check-suites-for-a-git-reference
        """
        copied_headers = deepcopy(self.session.headers)
        copied_headers['Accept'] = 'application/vnd.github.antiope-preview+json'
        return self.get("/repos/{}/{}/commits/{}/check-suites".format(owner, repo, ref), headers=copied_headers, **kwargs)
