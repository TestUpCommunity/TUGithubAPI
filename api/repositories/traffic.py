from core.rest_client import RestClient


class Traffic(RestClient):

    def list_referrers(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/traffic/#list-referrers
        """
        return self.get("/repos/{}/{}/traffic/popular/referrers".format(owner, repo), **kwargs)

    def list_paths(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/traffic/#list-paths
        """
        return self.get("/repos/{}/{}/traffic/popular/paths".format(owner, repo), **kwargs)

    def list_views(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/traffic/#views
        :param kwargs: day,week
        """
        return self.get("/repos/{}/{}/traffic/views".format(owner, repo), **kwargs)

    def list_clones(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/traffic/#clones
        :param kwargs: day,week
        """
        return self.get("/repos/{}/{}/traffic/clones".format(owner, repo), **kwargs)
