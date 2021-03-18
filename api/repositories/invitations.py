from core.rest_client import RestClient

class Invitations(RestClient):

    def list_invitations_for_a_repository(self, owner, repo):
        """
        https://developer.github.com/v3/repos/invitations/#invite-a-user-to-a-repository
        """
        return self.get("/repos/{}/{}/invitations".format(owner, repo))

    def delete_a_repository_invitation(self, owner, repo, invitation_id):
        """
        https://developer.github.com/v3/repos/invitations/#delete-a-repository-invitation
        """
        return self.delete("/repos/{}/{}/invitations/{}".format(owner, repo, invitation_id))

    def update_a_repository_invitation(self, owner, repo, invitation_id, **kwargs):
        """
        https://developer.github.com/v3/repos/invitations/#update-a-repository-invitation
        """
        return self.patch("/repos/{}/{}/invitations/{}".format(owner, repo, invitation_id), **kwargs)

    def list_a_user_repository_invitations(self):
        """
        https://developer.github.com/v3/repos/invitations/#list-a-users-repository-invitations
        """
        return self.get("/user/repository_invitations")

    def accept_a_repository_inviation(self, invitation_id):
        """
        https://developer.github.com/v3/repos/invitations/#accept-a-repository-invitation
        """
        return self.patch("/user/repository_invitations/{}".format(invitation_id))

    def decline_a_repository_invitation(self, invitation_id):
        """
        https://developer.github.com/v3/repos/invitations/#decline-a-repository-invitation
        """
        self.delete("/user/repository_invitations/{}".format(invitation_id))

