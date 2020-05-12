from core.rest_client import RestClient
from api.orgs.blocking import Blocking
from api.orgs.hooks import Hooks
from api.orgs.members import Members
from api.orgs.outside_collaborators import Outside_Collaborators

class Orgs(RestClient):

    def __init__(self, api_root_url, **kwargs):
        super(Orgs, self).__init__(api_root_url, **kwargs)
        self.blocking = Blocking(self.api_root_url, **kwargs)
        self.hooks = Hooks(self.api_root_url, **kwargs)
        self.member = Members(self.api_root_url, **kwargs)
        self.outside_collaborators = Outside_Collaborators(self.api_root_url, **kwargs)


    def remove_a_credential_authorization_for_an_organization(self,org,credential_id, **kwargs):
        """
        https://developer.github.com/v3/orgs/#remove-a-credential-authorization-for-an-organization
        """
        return self.delete('/orgs/{}/credential-authorizations/{}'.format(org,credential_id),**kwargs)

    def get_an_organization(self, org, **kwargs):
        """
        https://developer.github.com/v3/orgs/#get-an-organization
        """
        headers = {'Accept':'application/vnd.github.surtur-preview+json'}
        return self.get('/orgs/{}'.format(org), headers=headers ,**kwargs)

    def list_your_organizations(self, **kwargs):
        """
        https://developer.github.com/v3/orgs/#list-your-organizations
        """
        return self.get('/user/orgs' ,**kwargs)


