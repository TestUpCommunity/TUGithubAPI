from core.rest_client import RestClient


class Reactioons(RestClient):
    def list_reactions_for_a_commit_comment(self, owner, repo, comments,**kwargs):
        """
        https://developer.github.com/v3/reactions/#list-reactions-for-a-commit-comment
        :param owner:
        :param repo: 
        :param comments:
        :param kwargs:
        :return:
        """
        return self.get("/repos/{}/{}/comments/{}/reactions".format(owner, repo,comments), **kwargs)
