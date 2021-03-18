from core.rest_client import RestClient

class Comments(RestClient):

    def list_commit_comments_for_a_repository(self, owner, repo):
        """
        https://developer.github.com/v3/repos/comments/#list-commit-comments-for-a-repository
        """
        return self.get("/repos/{}/{}/comments".format(owner, repo))

    def list_comment_for_a_single_commit(self, owner, repo, commit_sha):
        """
        https://developer.github.com/v3/repos/comments/#list-comments-for-a-single-commit
        """
        return self.get("/repos/{}/{}/commits/{}".format(owner, repo, commit_sha))

    def create_a_commit_comment(self, owner, repo, commit_sha, **kwargs):
        """
        https://developer.github.com/v3/repos/comments/#create-a-commit-comment
        """
        return self.post("/repos/{}/{}/commits/{}".format(owner, repo, commit_sha), **kwargs)

    def get_a_single_commit_comment(self, owner, repo, comment_id):
        """
        https://developer.github.com/v3/repos/comments/#get-a-single-commit-comment
        """
        return self.get("/repos/{}/{}/comments/{}".format(owner, repo, comment_id))

    def update_a_commit_comment(self, owner, repo, comment_id, **kwargs):
        """
        https://developer.github.com/v3/repos/comments/#update-a-commit-comment
        """
        return self.patch("/repos/{}/{}/comments/{}".format(owner, repo, comment_id), **kwargs)

    def delete_a_comment_commit(self, owner, repo, comment_id):
        """
        https://developer.github.com/v3/repos/comments/#delete-a-commit-comment
        """
        return self.delete("/repos/{}/{}/comments/{}".format(owner, repo, comment_id))