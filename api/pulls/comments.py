from core.rest_client import RestClient

class Comments(RestClient):

    def list_comments_on_a_pull_request(self, owner, repo, pull_number, **kwargs):
        """
        https://developer.github.com/v3/pulls/comments/#list-comments-on-a-pull-request
        """
        headers = {'Accept':'application/vnd.github.squirrel-girl-preview'}
        return self.get('/repos/{}/{}/pulls/{}/comments'.format(owner, repo, pull_number), **kwargs, headers=headers)

    def list_comments_in_a_repository(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/pulls/comments/#list-comments-in-a-repository
        """
        headers = {'Accept':'application/vnd.github.squirrel-girl-preview'}
        return self.get('/repos//pulls/comments'.format(owner, repo), **kwargs, headers=headers)

    def get_a_single_comment(self, owner, repo, comment_id):
        """
        https://developer.github.com/v3/pulls/comments/#get-a-single-comment
        """
        headers = {'Accept': 'application/vnd.github.squirrel-girl-preview'}
        return self.get('/repos/{}/{}/pulls/comments/{}'.format(owner, repo, comment_id), headers=headers)

    def create_a_comment(self, owner, repo, pull_number, **kwargs):
        """
        https://developer.github.com/v3/pulls/comments/#create-a-comment
        """
        return self.post('/repos/{}/{}/pulls/{}/comments'.format(owner, repo, pull_number), **kwargs)

    def edit_a_comment(self, owner, repo, comment_id, **kwargs):
        """
        https://developer.github.com/v3/pulls/comments/#create-a-comment
        """
        return self.patch('/repos/{}/{}/pulls/comments/{}'.format(owner, repo, comment_id), **kwargs)

    def delete_a_comment(self, owner, repo, comment_id):
        """
        https://developer.github.com/v3/pulls/comments/#delete-a-comment
        """
        return self.delete('/repos/{}/{}/pulls/comments/{}'.format(owner, repo, comment_id))