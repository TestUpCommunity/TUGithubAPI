from core.rest_client import RestClient

class Reviews(RestClient):

    def list_reviews_on_a_pull_request(self, owner, repo, pull_number):
        """
        https://developer.github.com/v3/pulls/reviews/#list-reviews-on-a-pull-request
        """
        return self.get('/repos/{}/{}/pulls/{}/reviews'.format(owner, repo, pull_number))

    def get_a_single_review(self, owner, repo, pull_number, review_id):
        """
        https://developer.github.com/v3/pulls/reviews/#get-a-single-review
        """
        return self.get('/repos/{}/{}/pulls/{}/reviews/{}'.format(owner, repo, pull_number, review_id))

    def  delete_a_pending_review(self, owner, repo, pull_number, review_id):
        """
        https://developer.github.com/v3/pulls/reviews/#delete-a-pending-review
        """
        return self.delete('/repos/{}/{}/pulls/{}/reviews/{}'.format(owner, repo, pull_number, review_id))

    def get_a_comments_for_a_single_review(self, owner, repo, pull_number, review_id):
        """
        https://developer.github.com/v3/pulls/reviews/#delete-a-pending-review
        """
        return self.get('/repos/{}/{}/pulls/{}/reviews/{}/comments'.format(owner, repo, pull_number, review_id))

    def create_a_pull_request_review(self, owner, repo, pull_number, **kwargs):
        """
        https://developer.github.com/v3/pulls/reviews/#create-a-pull-request-review
        """
        headers = {'Accept':'application/vnd.github.v3.diff'}
        return self.post('/repos/{}/{}/pu lls/{}/reviews'.format(owner, repo, pull_number), **kwargs, headers =headers)

    def update_a_pull_request_review(self, owner, repo, pull_number, review_id, **kwargs):
        """
        https://developer.github.com/v3/pulls/reviews/#update-a-pull-request-review
        """
        return self.put('/repos/{}/{}/pulls/{}/reviews/{}'.format(owner, repo, pull_number, review_id), **kwargs)

    def submit_a_pull_request_review(self, owner, repo, pull_number, review_id, **kwargs):
        """
        https://developer.github.com/v3/pulls/reviews/#submit-a-pull-request-review
        """
        return self.post("/repos/{}/{}/pulls/{}/reviews/{}/events".format(owner, repo, pull_number, review_id), **kwargs)

    def dismiss_a_pull_request_review(self, owner, repo, pull_number, review_id, **kwargs):
        """
        https://developer.github.com/v3/pulls/reviews/#dismiss-a-pull-request-review
        """
        return self.put("/repos/{}/{}/pulls/{}/reviews/{}/dismissals".format(owner, repo, pull_number, review_id), **kwargs)