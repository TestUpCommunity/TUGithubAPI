from core.rest_client import RestClient


class Events(RestClient):
    def list_events_for_an_issue(self, owner, repo, issue_number, **kwargs):
        """
        https://developer.github.com/v3/issues/events/#list-events-for-an-issue
        """
        headers = {'Accept': 'application/vnd.github.starfox-preview+json,'
                             'application/vnd.github.sailor-v-preview+json'}
        return self.get('/repos/{}/{}/issues/{}/events'.format(owner, repo, issue_number), **kwargs, headers = headers)


    def list_events_for_a_repository(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/issues/events/#list-issue-events-for-a-repository
        """
        headers = {'Accept': 'application/vnd.github.starfox-preview+json,'
                             'application/vnd.github.sailor-v-preview+json'}
        return self.get('/repos/{}/{}/issues/events'.format(owner, repo), **kwargs, headers = headers)

    def get_a_single_event(self, owner, repo, event_id, **kwargs):
        """
        https://developer.github.com/v3/issues/events/#get-an-issue-event
        """
        headers = {'Accept': 'application/vnd.github.starfox-preview+json,'
                             'application/vnd.github.machine-man-preview,'
                             'application/vnd.github.sailor-v-preview+json'}
        return self.get('/repos/{}/{}/issues/events/{}'.format(owner, repo, event_id), **kwargs, headers = headers)

