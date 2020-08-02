from core.rest_client import RestClient


class Reactions(RestClient):

    def list_reactions_for_a_commit_comment(self, owner, repo, comment_id, **kwargs):
        """
        https://developer.github.com/v3/reactions/#list-reactions-for-a-commit-comment
        """
        headers = {'Accept': "application/vnd.github.squirrel-girl-preview+json"}
        return self.get("/repos/{}/{}/comments/{}/reactions".format(owner, repo, comment_id), headers=headers, **kwargs)
