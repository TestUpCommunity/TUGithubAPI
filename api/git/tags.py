from core.rest_client import RestClient


class Tags(RestClient):

    def create_a_tag_object(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/git/tags/#create-a-tag-object
        """
        return self.post("/repos/{}/{}/git/tags".format(owner, repo), **kwargs)
