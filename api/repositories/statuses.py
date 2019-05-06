from core.rest_client import RestClient


class Statuses(RestClient):

    def create_a_status(self, owner, repo, sha, **kwargs):
        """
        https://developer.github.com/v3/repos/statuses/#create-a-status
        """
        return self.post("/repos/{}/{}/statuses/{}".format(owner, repo, sha), **kwargs)

    def list_statuses_for_specific_ref(self, owner, repo, ref, **kwargs):
        """
        https://developer.github.com/v3/repos/statuses/#list-statuses-for-a-specific-ref
        """
        return self.get("/repos/{}/{}/commits/{}/statuses".format(owner, repo, ref), **kwargs)

    def get_combined_status_for_specific_ref(self, owner, repo, ref, **kwargs):
        """
        https://developer.github.com/v3/repos/statuses/#get-the-combined-status-for-a-specific-ref
        """
        return self.get("/repos/{}/{}/commits/{}/status".format(owner, repo, ref), **kwargs)
