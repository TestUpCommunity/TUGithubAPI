from core.rest_client import RestClient
from api.issues.events import Events


class Issues(RestClient):

    def __init__(self, api_root_url, **kwargs):
        super(Issues, self).__init__(api_root_url, **kwargs)
        self.event = Events(self.api_root_url, **kwargs)

    def create_issue(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/issues/#create-an-issue
        """
        return self.post("/repos/{}/{}/issues".format(owner, repo), **kwargs)

    def list_issue(self, **kwargs):
        """
        https://developer.github.com/v3/issues/#list-issues
        """
        header = {'Accept': 'application/vnd.github.machine-man-preview'}
        return self.get("/issues", headers=header, **kwargs)


