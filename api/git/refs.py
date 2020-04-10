from core.rest_client import RestClient


class Refs(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(Refs, self).__init__(api_root_url, **kwargs)

    def delete_reference(self, owner, repo, ref, **kwargs):
        """
        https://developer.github.com/v3/git/refs/#delete-a-reference
        :param owner:
        :param repo:
        :param ref:
        :param kwargs:
        :return:
        """
        return self.delete("/repos/{}/{}/git/refs/{}".format(owner, repo, ref), **kwargs)