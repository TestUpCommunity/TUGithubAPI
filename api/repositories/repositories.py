from core.rest_client import RestClient

class Repositories(RestClient):

    def replace_all_topics_for_a_repository(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/#replace-all-topics-for-a-repository
        """
        headers = {'Accept':'application/vnd.github.mercy-preview+json'}
        return self.put("/repos/{}/{}/topics".format(owner, repo), headers = headers, **kwargs)

    def list_contributors(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/#list-contributors
        """
        return self.get('/repos/{}/{}/contributors'.format(owner, repo), **kwargs)

    def list_languages(self, owner, repo):
        """
        https://developer.github.com/v3/repos/#list-languages
        """
        return self.get('/repos/{}/{}/languages'.format(owner, repo))

    def list_tags(self, owner, repo):
        """
        https://developer.github.com/v3/repos/#list-tags
        """
        return self.get('/repos/{}/{}/tags'.format(owner, repo))

    def delete_a_repository(self, owner, repo):
        """
        https://developer.github.com/v3/repos/#delete-a-repository
        """
        return self.delete('/repos/{}/{}'.format(owner, repo))

    def transfer_a_repository(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/#transfer-a-repository
        """
        headers = {'Accept':'application/vnd.github.nightshade-preview+json'}
        return self.delete('/repos/{}/{}/transfer'.format(owner, repo), headers = headers ,**kwargs)





