from core.rest_client import RestClient


class Repos(RestClient):
    def __init__(self):
        self.headers = {'Accept': 'application/vnd.github.sombra-preview'}

    def get_interaction_restrictions_for_repo(self, owner, **kwargs):
        """
        https://developer.github.com/v3/interactions/repos#get-interaction-restrictions-for-a-repository
        :param owner: organization owner
        """
        return self.get('/repos/{}/:repo/interaction-limits'.format(owner), headers=self.headers, **kwargs)

    def update_interaction_restrictions_for_repo(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/interactions/repos/#add-or-update-interaction-restrictions-for-a-repository
        :param owner: organization owner
        :param repo: repository
        """
        return self.put('/repos/{}/{}/interaction-limits'.format(owner, repo), headers=self.headers, **kwargs)

    def remove_interaction_restrictions_for_repo(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/interactions/repos/#remove-interaction-restrictions-for-a-repository
        :param owner: organization owner
        :param repo: repository
        """
        return self.delete('/repos/{}/{}/interaction-limits'.format(owner, repo), header=self.headers, **kwargs)
