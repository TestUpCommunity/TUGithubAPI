from core.rest_client import RestClient


class Refs(RestClient):
    def create_a_reference(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/git/refs/#create-a-reference
        """
        return self.post("/repos/{}/{}/git/refs".format(owner, repo), **kwargs)

    def get_a_reference(self, owner, repo, ref, **kwargs):
        """
        https://developer.github.com/v3/git/refs/#get-a-reference
        """
        return self.get("/repos/{}/{}/git/refs/heads/{}".format(owner, repo, ref), **kwargs)

