from core.rest_client import RestClient
from api.projects.cards import Cards
from api.projects.columns import Columns
from api.projects.collaborators import Collaborators

class Projects(RestClient):
    def __int__(self, api_root_url, **kwargs):
        super(Projects, self).__init__(api_root_url, **kwargs)
        self.cards = Cards(self.api_root_url, **kwargs)
        self.columns = Columns(self.api_root_url, **kwargs)
        self.collaborators = Collaborators(self.api_root_url, **kwargs)

    def list_repository_projects(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/projects/#list-repository-projects
        """
        headers = {'Accept':'application/vnd.github.inertia-preview+json'}
        return self.get('/repos/:{}/{}/projects'.format(owner,repo), headers = headers, **kwargs)

    def list_organization_projects(self, org, **kwargs):
        """
        https://developer.github.com/v3/projects/#list-organization-projects
        """
        headers = {'Accept':'application/vnd.github.inertia-preview+json'}
        return self.get('/orgs/{}/projects'.format(org), headers =headers, **kwargs)

    def list_user_projects(self, username, **kwargs):
        """
        https://developer.github.com/v3/projects/#list-user-projects
        """
        headers = {'Accept':'application/vnd.github.inertia-preview+json'}
        return self.get('/users/{}/projects'.format(username),headers = headers, **kwargs)

    def get_a_project(self, project_id):
        """
        https://developer.github.com/v3/projects/#get-a-project
        """
        headers = {'Accept':'application/vnd.github.inertia-preview+json'}
        return self.get('/projects/{}'.format(project_id), headers = headers)

    def create_a_repository_projec(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/projects/#get-a-project
        """
        headers = {'Accept':'application/vnd.github.inertia-preview+json'}
        return self.post('/repos/{}/{}/projects'.format(owner,repo), headers = headers, **kwargs)

    def create_an_organization_project(self, org, **kwargs):
        """
        https://developer.github.com/v3/projects/#get-a-project
        """
        headers = {'Accept':'application/vnd.github.inertia-preview+json'}

        return self.post('/orgs/{}/projects'.format(org), headers = headers, **kwargs)

    def create_a_user_project(self, **kwargs):
        """
        https://developer.github.com/v3/projects/#get-a-project
        """
        headers = {'Accept':'application/vnd.github.inertia-preview+json'}
        return self.post('/user/projects', headers = headers, **kwargs)

    def update_a_project(self, project_id, **kwargs):
        """
        https://developer.github.com/v3/projects/#get-a-project
        """
        headers = {'Accept':'application/vnd.github.inertia-preview+json'}
        return self.patch('/projects/{}'.format(project_id), headers = headers, **kwargs)

    def delete_a_project(self, project_id):
        """
        https://developer.github.com/v3/projects/#get-a-project
        """
        headers = {'Accept':'application/vnd.github.inertia-preview+json'}

        return self.delete('/projects/'.format(project_id), headers = headers)