from core.rest_client import RestClient

class Hooks(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(Hooks, self).__init__(api_root_url, **kwargs)

    def create_a_hook(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/hooks/#create-a-hook
        """
        return self.post("/repos/{}/{}/hooks".format(owner, repo), **kwargs)

    def edit_a_hook(self, owner,repo, hook_id, **kwargs):
        """
        https://developer.github.com/v3/repos/hooks/#edit-a-hook
        """
        return self.patch("/repos/{}/{}/hooks/{}".format(owner, repo, hook_id), **kwargs)

    def delete_a_hook(self, owner, repo, hook_id):
        """
        https://developer.github.com/v3/repos/hooks/#delete-a-hook
        """
        return self.delete_a_hook("/repos/{}/{}/hooks/{}".format(owner, repo, hook_id))

    def test_a_push_hook(self, owner, repo, hook_id):
        """
        https://developer.github.com/v3/repos/hooks/#test-a-push-hook
        """
        return self.post(("/repos/{}/{}/hooks/{}/test".format(owner, repo, hook_id)))

    def ping_a_hook(self, owner, repo, hook_id):
        """
        https://developer.github.com/v3/repos/hooks/#ping-a-hook
        """
        return self.post(("/repos/{}/{}/hooks/{}/pings".format(owner, repo, hook_id)))

