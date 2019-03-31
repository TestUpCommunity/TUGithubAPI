from core.rest_client import RestClient


class Repos(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(Repos, self).__init__(api_root_url, **kwargs)

    def list_your_repos(self, **kwargs):
        """
        https://developer.github.com/v3/repos/#list-your-repositories
        """
        return self.get("/user/repos", **kwargs)

    def list_user_repos(self, username, **kwargs):
        """
        https://developer.github.com/v3/repos/#list-user-repositories
        :param username:  username
        """
        return self.get("/users/{}/repos".format(username), **kwargs)

    def list_organization_repos(self,org,**kwargs):
        """
        https://developer.github.com/v3/repos/#list-organization-repositories
        :param org: orgnization name
        """
        return self.get("/orgs/{}/repos".format(org),**kwargs)

    def list_all_public_repos(self,**kwargs):
        """
        https://developer.github.com/v3/repos/#list-all-public-repositories
        """
        return self.get("/repositories",**kwargs)
