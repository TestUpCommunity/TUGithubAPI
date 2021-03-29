from core.rest_client import RestClient

class Review_requests(RestClient):

    def list_review_request(self, owner, repo, pull_number):
        """
        https://developer.github.com/v3/pulls/review_requests/#list-review-requests
        """
        return self.get('/repos/{}/{}/pulls/{}/requested_reviewers'.format(owner, repo, pull_number))

    def create_a_review_request(self, owner, repo, pull_number):
        """
        https://developer.github.com/v3/pulls/review_requests/#create-a-review-request
        """
        headers = {'Accept':'application/vnd.github.symmetra-preview+json'}
        return self.post('/repos/{}/{}/pulls/{}/requested_reviewers'.format(owner, repo, pull_number),headers = headers)

    def delete_a_review_request(self, owner, repo, pull_number):
        """
        https://developer.github.com/v3/pulls/review_requests/#delete-a-review-request
        """
        return self.delete('/repos/{}/{}/pulls/{}/requested_reviewers'.format(owner, repo, pull_number))
