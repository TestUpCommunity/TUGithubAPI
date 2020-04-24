from core.rest_client import RestClient
from api.apps.installations import Installation


class Apps(RestClient):

    def __init__(self, api_root_url, **kwargs):
        super(Apps, self).__init__(api_root_url, **kwargs)
        self.installation = Installation(api_root_url, **kwargs)

    def get_a_user_installation(self, username, **kwargs):
        """
        https://developer.github.com/v3/apps/#get-a-user-installation

        """
        header = {"Accept": "application/vnd.github.machine-man-preview+json"}
        return self.get("/users/{}/installation".format(username), headers=header, **kwargs)

    def create_a_gitHub_app_from_a_manifest(self, code, **kwargs):
        """
        https://developer.github.com/v3/apps/#create-a-github-app-from-a-manifest

        """
        return self.post("/app-manifests/{}/conversions".format(code), **kwargs)

