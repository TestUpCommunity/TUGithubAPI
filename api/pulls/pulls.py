from core.rest_client import RestClient
from api.pulls.comments import Comments
from api.pulls.review_requests import Review_requests
from api.pulls.reviews import Reviews

class Pulls(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(Pulls, self).__init__(api_root_url, **kwargs)
        self.comments = Comments(self.api_root_url, **kwargs)
        self.review_requests = Review_requests(self.api_root_url, **kwargs)
        self.reviews = Reviews(self.api_root_url, **kwargs)

    def list_pull_request(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/pulls/#list-pull-requests
        """
        headers = {'Accept':'application/vnd.github.shadow-cat-preview+json,'
                            'application/vnd.github.symmetra-preview+json,'
                            'application/vnd.github.sailor-v-preview+json'}
        return self.get('/repes/{}/{}/pulls'.format(owner, repo), **kwargs, headers = headers)

    def get_a_single_pull_request(self, owner, repo, pull_number):
        """
        https://developer.github.com/v3/pulls/#get-a-single-pull-request
        """
        headers = {'Accept': 'application/vnd.github.shadow-cat-preview+json,'
                             'application/vnd.github.symmetra-preview+json,'
                             'application/vnd.github.sailor-v-preview+json'}
        return self.get('/repes/{}/{}/pulls/{}'.format(owner, repo, pull_number), headers = headers)

    def create_a_pull_request(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/pulls/#create-a-pull-request
        """
        headers = {'Accept': 'application/vnd.github.shadow-cat-preview+json,'
                             'application/vnd.github.symmetra-preview+json,'
                             'application/vnd.github.sailor-v-preview+json'}

        return self.post('/repos/{}/{}/pulls'.format(owner, repo),**kwargs, headers=headers)

    def update_a_pull_request_branch(self, owner, repo, pull_number, **kwargs):
        """
        https://developer.github.com/v3/pulls/#update-a-pull-request-branch
        """
        headers={'Accept':'application/vnd.github.lydian-preview+json'}
        return self.put('/repos/{}/{}/pulls/{}/update-branch'.format(owner, repo, pull_number),**kwargs, headers=headers)

    def update_a_pull_request(self, owner, repo, pull_number, **kwargs):
        """
        https://developer.github.com/v3/pulls/#update-a-pull-request
        """
        headers = {'Accept': 'application/vnd.github.shadow-cat-preview+json,'
                             'application/vnd.github.symmetra-preview+json,'
                             'application/vnd.github.sailor-v-preview+json'}
        return self.patch('/repos/{}/{}/pulls/{}'.format(owner, repo, pull_number), **kwargs, headers = headers)

    def list_a_commits_on_a_pull_request(self, owner ,repo, pull_number):
        """
        https://developer.github.com/v3/pulls/#list-commits-on-a-pull-request
        """
        return self.get('/repos/{}/{}/pulls/{}/commits'.format(owner, repo, pull_number))

    def list_pull_requests_files(self, owner, repo, pull_number):
        """
        https://developer.github.com/v3/pulls/#list-commits-on-a-pull-request
        """
        return self.get('/repos/{}/{}/pulls/{}/files'.format(owner, repo, pull_number))

    def get_a_if_pull_request_has_been_merged(self, owner, repo, pull_number):
        """
        https://developer.github.com/v3/pulls/#get-if-a-pull-request-has-been-merged
        """
        return self.get('/repos/{}/{}/pulls/{}/merge'.format(owner, repo, pull_number))

    def merged_a_pull_request(self, owner, repo, pull_number, **kwargs):
        """
        https://developer.github.com/v3/pulls/#merge-a-pull-request-merge-button
        """
        return self.put('/repos/{}/{}/pulls/{}/merge'.format(owner, repo, pull_number), **kwargs)


