from core.rest_client import RestClient


class Outside_Collaborators(RestClient):

    def convert_member_to_outside_collaborator(self, org, username, **kwargs):
        """
        https://developer.github.com/v3/orgs/outside_collaborators/#convert-member-to-outside-collaborator
        """
        return self.put('/orgs/{}/outside_collaborators/{}'.format(org, username), **kwargs)

    def publicize_a_users_membership(self,org,username, **kwargs):
        """
        https://developer.github.com/v3/orgs/members/#publicize-a-users-membership
        """
        return self.put('/orgs/{}/public_members/{}'.format(org,username), **kwargs)

    def remove_outside_collaborator(self,org, username, **kwargs):
        """
        https://developer.github.com/v3/orgs/outside_collaborators/#remove-outside-collaborator
        """
        return self.delete('/orgs/{}/outside_collaborators/{}'.format(org,username), **kwargs)

    def list_outside_collaborators(self ,org,**kwargs):
        """
        https://developer.github.com/v3/orgs/outside_collaborators/#list-outside-collaborators
        """
        return self.get('/orgs/{}/outside_collaborators'.format(org), **kwargs)



