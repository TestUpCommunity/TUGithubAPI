from core.rest_client import RestClient
from copy import deepcopy


class Timeline(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(Timeline, self).__init__(api_root_url, **kwargs)

    def List_events_for_issue(self, owner, repo, issue_number, **kwargs):
        """

        https://developer.github.com/v3/issues/timeline/#list-events-for-an-issue

        """
        copied_headers = deepcopy(self.session.headers)
        # copied_headers["Accept"] = "application/vnd.github.starfox-preview+json,application/vnd.github.mockingbird-preview"
        copied_headers["Accept"] = "application/vnd.github.starfox-preview+json"
        return self.get("/repos/{}/{}/issues/{}/timeline".format(owner, repo, issue_number), headers=copied_headers,
                        **kwargs)
