from core.rest_client import RestClient


class Hooks(RestClient):

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
      
    def list_hooks(self,owner,repo, **kwargs):
        """
        https://developer.github.com/v3/repos/hooks#list-hooks
        """
        return self.get("/repos/{}/{}/hooks".format(owner, repo), **kwargs)

    def pubSubHubbub(self, owner, repo, event, **kwargs):
        """
        https://developer.github.com/v3/repos/hooks/#pubsubhubbub
        """
        return self.post("/repos/{}/{}/events/{}".format(owner, repo, event), **kwargs)