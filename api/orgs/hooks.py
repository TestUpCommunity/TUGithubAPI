from core.rest_client import RestClient


class Hooks(RestClient):

    def ping_a_hook(self,org,hook_id, **kwargs):
        """
        https://developer.github.com/v3/orgs/hooks#ping-a-hook
        """
        return self.post('/orgs/{}/hooks/{}/pings'.format(org, hook_id), **kwargs)

    def delete_a_hook(self,org,hook_id, **kwargs):
        """
        https://developer.github.com/v3/orgs/hooks/#delete-a-hook
        """
        return self.delete('/orgs/{}/hooks/{}'.format(org,hook_id), **kwargs)

    def list_hooks(self,org, **kwargs):
        """
        https://developer.github.com/v3/orgs/hooks/#list-hooks
        """
        return self.get('/orgs/{}/hooks'.format(org), **kwargs)

    def edit_a_hook(self,org,hook_id, **kwargs):
        """
        https://developer.github.com/v3/orgs/hooks/#edit-a-hook
        """
        return self.patch('/orgs/{}/hooks/{}'.format(org,hook_id),**kwargs)

    def create_a_hook(self,org, **kwargs):
        """
        https://developer.github.com/v3/orgs/hooks/#create-a-hook
        """
        return self.post('/orgs/{}/hooks'.format(org), **kwargs)

    def get_single_hook(self,org,hook_id, **kwargs):
        """
        https://developer.github.com/v3/orgs/hooks/#get-single-hook
        """
        return self.get('/orgs/{}/hooks/{}'.format(org,hook_id), **kwargs)

