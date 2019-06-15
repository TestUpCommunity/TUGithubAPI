from core.rest_client import RestClient

class Collaborators(RestClient):

    def add_user_as_a_collaborator(self, project_id, username, **kwargs):
        """
        https://developer.github.com/v3/projects/collaborators/#add-user-as-a-collaborator
        """
        headers ={'Accept':'application/vnd.github.inertia-preview+json'}
        return self.put('/projects/{}/collaborators/{}'.format(project_id, username),headers = headers, **kwargs)

    def list_collaborator(self, project_id, **kwargs):
        """
        https://developer.github.com/v3/projects/collaborators/#list-collaborators
        """
        headers = {'Accept': 'application/vnd.github.inertia-preview+json'}
        return self.get('/projects/{}/collaborators'.format(project_id), headers = headers, **kwargs)

    def review_a_users_permission_level(self, project_id, username, **kwargs):
        """
        https://developer.github.com/v3/projects/collaborators/#review-a-users-permission-level
        """
        headers = {'Accept':'application/vnd.github.inertia-preview+json'}
        return self.get('/projects/{}/collaborators/{}/permission'.format(project_id,username), headers = headers, **kwargs)

    def remove_user_as_a_collaborator(self, project_id, username):
        """
        https://developer.github.com/v3/projects/collaborators/#remove-user-as-a-collaborator
        """
        headers = {'Accept':'application/vnd.github.inertia-preview+json'}
        return self.delete('/projects/{}/collaborators/{}'.format(project_id,username), headers = headers)

