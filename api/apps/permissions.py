from core.rest_client import RestClient


class Permissions(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(Permissions, self).__init__(api_root_url, **kwargs)

    def list_users_blocked_by_an_oragnization(self, org, **kwargs):
        """
        https://developer.github.com/v3/orgs/blocking/#list-users-blocked-by-an-organization
        """
        headers = {"accept": "application/vnd.github.giant-sentry-fist-preview+json"}
        return self.get("/orgs/{}/blocks".format(org), **kwargs, headers=headers)

    def check_if_a_user_is_blocked_by_an_organization(self, org, username, **kwargs):
        """
        https://developer.github.com/v3/orgs/blocking/#check-if-a-user-is-blocked-by-an-organization 
        """
        headers = {"accept": "application/vnd.github.giant-sentry-fist-preview+json"}
        return self.get("/orgs/{}/blocks/{}".format(org, username), **kwargs, headers=headers)

    def block_a_user_from_an_organization(self,org, username, **kwargs):
        """
        https://developer.github.com/v3/orgs/blocking/#block-a-user-from-an-organization
        """
        headers = {"accept": "application/vnd.github.giant-sentry-fist-preview+json"}
        return self.put("/orgs/{}/blocks/{}".format(org, username), headers=headers, **kwargs)

    def unblock_a_user_from_an_organization(self, org, username, **kwargs):
        """
        https://developer.github.com/v3/orgs/blocking/#unblock-a-user-from-an-organization
        """
        headers = {"accept": "application/vnd.github.giant-sentry-fist-preview+json"}
        return  self.delete("/orgs/{}/blocks/{}".format(org, username), headers=headers, **kwargs)