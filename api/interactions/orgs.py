from core.rest_client import RestClient


class Orgs(RestClient):
    def __init__(self):
        self.headers = {'Accept': 'application/vnd.github.sombra-preview'}

    def get_interactions_limits_for_org(self, org, **kwargs):
        """
        https://developer.github.com/v3/interactions/orgs/#get-interaction-restrictions-for-an-organization
        :param org: organization name
        """
        return self.get('/orgs/{}/interaction-limits'.format(org), headers=self.headers, **kwargs)

    def update_interactions_limits_for_org(self, org, **kwargs):
        """
        https://developer.github.com/v3/interactions/orgs#add-or-update-interaction-restrictions-for-an-organization
        :param org: organization name
        """
        return self.put('/orgs/{}/interaction-limits'.format(org), headers=self.headers, **kwargs)

    def remove_interaction_restrictions_for_org(self, org, **kwargs):
        """
        https://developer.github.com/v3/interactions/orgs#remove-interaction-restrictions-for-an-organization
        :param org: organization name
        """
        return self.delete('/orgs/{}/interaction-limits'.format(org), headers=self.headers, **kwargs)
