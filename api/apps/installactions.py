from core.rest_client import RestClient


class Installation(RestClient):
    def list_repositories(self, **kwargs):
        """
        https://developer.github.com/v3/apps/installations/#list-repositories
        :param kwargs:
        :return:
        """
        headers = {'Accept': 'application/vnd.github.machine-man-preview+json'}
        return self.get("/installation/repositories", headers=headers, **kwargs)

    def list_installations_for_a_user(self, **kwargs):
        """
        https://developer.github.com/v3/apps/installations/#list-installations-for-a-user
        :param kwargs:
        :return:
        """
        headers = {'Accept': 'application/vnd.github.machine-man-preview+json'}
        return self.get("/user/installations", headers=headers, **kwargs)

    def add_repository_to_installation(self, installation_id, repository_id, **kwargs):
        """
        https://developer.github.com/v3/apps/installations/#add-repository-to-installation
        """
        headers = {'Accept': 'application/vnd.github.machine-man-preview+json'}
        return self.put("/user/installations/{}/repositories/{}".format(installation_id, repository_id), headers = headers, **kwargs)

