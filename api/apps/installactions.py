from core.rest_client import RestClient


class Installation(RestClient):
    def list_repositories(self, **kwargs):
        """
        https://developer.github.com/v3/apps/installations/#list-repositories
        :param kwargs:
        :return:
        """
        header = {'Accept': 'application/vnd.github.machine-man-preview+json'}
        return self.get("/installation/repositories", headers=header, **kwargs)

    def list_installations_for_a_user(self, **kwargs):
        """
        https://developer.github.com/v3/apps/installations/#list-installations-for-a-user
        :param kwargs:
        :return:
        """
        header = {'Accept': 'application/vnd.github.machine-man-preview+json'}
        return self.get("/user/installations", headers=header, **kwargs)