from core.rest_client import RestClient


class Members(RestClient):

    def check_public_membership(self,org, username, **kwargs):
        """
        https://developer.github.com/v3/orgs/members/#check-public-membership
        """
        return self.get('orgs/{}/public_members/{}'.format(org, username) ,**kwargs)

    def members_list(self,org, **kwargs):
        """
        https://developer.github.com/v3/orgs/members/#members-list
        """
        return self.get('/orgs/{}/members'.format(org),**kwargs)

    def check_membership(self,org, members, **kwargs):
        """
        https://developer.github.com/v3/orgs/members/#check-membership
        """
        return self.get('/orgs/{}/members/{}'.format(org, members) ,**kwargs)

    def remove_a_member(self,org,username, **kwargs):
        """
        https://developer.github.com/v3/orgs/members#remove-a-member
        """
        return  self.delete('/orgs/{}/members/{}'.format(org,username), **kwargs)

    def public_members_list(self,org, **kwargs):
        """
        https://developer.github.com/v3/orgs/members/#public-members-list
        """
        return self.get('/orgs/{}/public_members'.format(org), **kwargs)

    def edit_your_organization_membership(self,org, **kwargs):
        """
        https://developer.github.com/v3/orgs/members/#edit-your-organization-membership
        """
        return self.patch('/user/memberships/orgs/{}'.format(org), **kwargs)

    def list_your_organization_memberships(self, **kwargs):
        """
        https://developer.github.com/v3/orgs/members/#list-your-organization-memberships
        """
        return self.get('/user/memberships/orgs', **kwargs)

    def get_your_organization_membership(self,org, **kwargs):
        """
        https://developer.github.com/v3/orgs/members/#get-your-organization-membership
        """
        return self.get('/user/memberships/orgs/{}'.format(org),**kwargs)

    def list_organization_invitation_teams(self,org,invitation_id, **kwargs):
        """
        https://developer.github.com/v3/orgs/members/#list-organization-invitation-teams
        """
        return self.get('/orgs/{}/invitations/{}/teams'.format(org,invitation_id), **kwargs)

    def create_organization_invitation(self,org, **kwargs):
        """
        https://developer.github.com/v3/orgs/members/#create-organization-invitation
        """
        return self.post('/orgs/{}/invitations'.format(org), **kwargs)

    def list_pending_organization_invitations(self,org, **kwargs):
        """
        https://developer.github.com/v3/orgs/members/#list-pending-organization-invitations
        """
        return self.get('/orgs/{}/invitations'.format(org), **kwargs)

    def add_or_update_organization_membership(self,org,username, **kwargs):
        """
        https://developer.github.com/v3/orgs/members/#add-or-update-organization-membership
        """
        return self.put('/orgs/{}/memberships/{}'.format(org,username), **kwargs)

    def remove_organization_membership(self,org,username, **kwargs):
        """
        https://developer.github.com/v3/orgs/members/#remove-organization-membership
        """
        return self.delete('/orgs/{}/memberships/{}'.format(org,username), **kwargs)

    def get_organization_membership(self,org,username, **kwargs):
        """
        https://developer.github.com/v3/orgs/members/#get-organization-membership
        """
        return self.delete('/orgs/{}/memberships/{}'.format(org,username), **kwargs)

    def conceal_a_users_membership(self,org,username, **kwargs):
        """
        https://developer.github.com/v3/orgs/members/#conceal-a-users-membership
        """
        return self.delete('/orgs/{}/public_members/{}'.format(org,username), **kwargs)