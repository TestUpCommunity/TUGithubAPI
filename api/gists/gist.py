from core.rest_client import RestClient
from api.gists.comment import Comment


class Gists(RestClient):

    def __init__(self, api_root_url, **kwargs):
        super(Gists, self).__init__(api_root_url, **kwargs)
        self.comment  = Comment(self.api_root_url, **kwargs)

    def list_gists_for_a_user(self, username, **kwargs):
        """
        https://developer.github.com/v3/gists/#list-a-users-gists  #616
        """
        return self.get('/users/{}/gists'.format(username),**kwargs)

    def list_all_public_gists(self, **kwargs):
        """
        https://developer.github.com/v3/gists#list-all-public-gists  #617
        """
        return self.get('/gists/public', **kwargs)

    def list_starred_gists(self, **kwargs):
        """
        https://developer.github.com/v3/gists#list-starred-gists  #618
        """
        return self.get('/gists/starred', **kwargs)

    def get_a_single_gist(self, gist_id, **kwargs):
        """
        https://developer.github.com/v3/gists#get-a-single-gist  #619
        """
        return self.get('/gists/{}'.format(gist_id), **kwargs)

    def get_a_specific_revision_of_a_gist(self,gist_id, sha, **kwargs):
        """
        https://developer.github.com/v3/gists#get-a-specific-revision-of-a-gist  #620
        """
        return self.get('/gists/{}/{}'.format(gist_id, sha), **kwargs)

    def create_a_gist(self, **kwargs):
        """
        https://developer.github.com/v3/gists#create-a-gist  #621
        """
        return self.post('/gists', **kwargs)

    def list_gist_commits(self, gist_id, **kwargs):
        """
        https://developer.github.com/v3/gists#list-gist-commits  #623
        """
        return self.get('/gists/{}/commits'.format(gist_id), **kwargs)

    def star_a_gist(self, gist_id, **kwargs):
        """
        https://developer.github.com/v3/gists#star-a-gist  #624
        """
        return self.put('/gists/{}/star'.format(gist_id), **kwargs)

    def unstar_a_gist(self, gist_id, **kwargs):
        """
        https://developer.github.com/v3/gists#unstar-a-gist  #625
        """
        return self.delete('/gists/{}/star'.format(gist_id), **kwargs)

    def check_if_a_gist_is_starred(self, gist_id, **kwargs):
        """
        https://developer.github.com/v3/gists#check-if-a-gist-is-starred  #626
        """
        return self.get('/gists/{}/star'.format(gist_id), **kwargs)

    def fork_a_gist(self, gist_id, **kwargs):
        """
        https://developer.github.com/v3/gists#fork-a-gist  #627
        """
        return self.post('/gists/{}/forks'.format(gist_id), **kwargs)

    def list_gist_forks(self, gist_id, **kwargs):
        """
        https://developer.github.com/v3/gists#list-gist-forks  #628
        """
        return self.get('/gists/{}/forks'.format(gist_id), **kwargs)

    def delete_a_gist(self, gist_id, **kwargs):
        """
        https://developer.github.com/v3/gists#delete-a-gist  #629
        """
        return self.delete('/gists/{}'.format(gist_id), **kwargs)