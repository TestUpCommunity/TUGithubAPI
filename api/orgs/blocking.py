from core.rest_client import RestClient


class Blocking(RestClient):

    def check_whether_a_user_is_blocked_from_an_organization(self, org, username, **kwargs):
        """
        https://developer.github.com/v3/orgs/blocking/#check-whether-a-user-is-blocked-from-an-organization
        """
        return self.get('/orgs/{}/blocks/{}'.format(org, username), **kwargs)

    def block_a_user(self,org,username, **kwargs):
        """
        https://developer.github.com/v3/orgs/blocking/#block-a-user
        """
        return self.put('/orgs/{}/blocks/{}'.format(org,username), **kwargs)

    def unblock_a_user(self,org,username, **kwargs):
        """
        https://developer.github.com/v3/orgs/blocking/#unblock-a-user
        """
        return self.delete('/orgs/{}/blocks/{}'.format(org,username), **kwargs)

