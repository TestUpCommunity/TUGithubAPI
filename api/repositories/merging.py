from core.rest_client import RestClient


class Merging(RestClient):

    def Perform_a_merge(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/merging/#perform-a-merge
        """
        return self.post('/repos/{}/{}/merges'.format(owner, repo), **kwargs)