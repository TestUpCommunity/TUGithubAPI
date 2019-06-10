from core.rest_client import RestClient

class Collaborators(RestClient):

    def list_collaborators(self,owner,repo,**kwargs):
        """
        https://developer.github.com/v3/repos/collaborators/#list-collaborators
        """
        headlers = {'Accept':'application/vnd.github.hellcat-preview+json'}
        return self.get('/repos/{}/{}/collaborators'.format(owner, repo), headlers=headlers, **kwargs)

    def Check_if_a_user_is_a_collaborator(self,owner,repo,username,**kwargs):
        """
        https://developer.github.com/v3/repos/collaborators/#check-if-a-user-is-a-collaborator
        """
        headlers = {'Accept': 'application/vnd.github.hellcat-preview+json'}
        return self.get('/repos/{}/{}/collaborators/{}'.format(owner,repo,username), headlers=headlers, **kwargs)

    def Review_a_user_permission_level(self,owner,repo,username,**kwargs):
        """
        https://developer.github.com/v3/repos/collaborators/#review-a-users-permission-level
        permission: admin, write, read, none
        """
        return self.get('/repos/{}/{}/collaborators/{}/permission'.format(owner,repo,username), **kwargs)

    def Add_user_as_a_collaborator(self,owner,repo,username,**kwargs):
        """
        https://developer.github.com/v3/repos/collaborators/#add-user-as-a-collaborator
        """
        return self.put('/repos/:owner/{}/collaborators/{}'.format(owner,repo,username), **kwargs)

    def Remove_user_as_a_collaborator(self,owner,repo,username,**kwargs):
        """
        https://developer.github.com/v3/repos/collaborators/#remove-user-as-a-collaborator
        """
        return self.delete('/repos/{}/{}/collaborators/{}'.format(owner,repo,username), **kwargs)