from core.rest_client import RestClient

class Commits(RestClient):

    def list_commits_on_a_repository(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/commits/#list-commits-on-a-repository
        """
        return self.get("/repos/{}/{}/commits".format(owner, repo), **kwargs)

    def get_a_single_commit(self, owner, repo, ref, **kwargs):
        """
        https://developer.github.com/v3/repos/commits/#get-a-single-commit
        """
        return self.get("/repoe/{}/{}/commits/{}".format(owner, repo, ref),**kwargs)

    def compare_two_commits(self, owner, repo, base, head, **kwargs):
        """
        https://developer.github.com/v3/repos/commits/#compare-two-commits
        """
        return self.get("/repos/{}/{}/compare/{}...{}".format(owner, repo, base, head), **kwargs)

    def list_branchese_for_HEAD_commit(self, owner, repo, commit_sha):
        """
        https://developer.github.com/v3/repos/commits/#list-branches-for-head-commit
        """
        headers = {"Accept":"application/vnd.github.groot-preview+json"}
        return self.get("/repos/{}/{}/commits/{}/branches-where-head".format(owner, repo, commit_sha), headers = headers)

    def list_pull_requests_associated_with_commit(self, owner, repo, commit_sha):
        """
        https://developer.github.com/v3/repos/commits/#list-pull-requests-associated-with-commit
        """
        return self.get("/repos/{}/{}/commits/{}/pulls".format(owner, repo, commit_sha))

