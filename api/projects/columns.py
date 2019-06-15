from core.rest_client import RestClient

class Columns(RestClient):

    def create_a_project_column(self, project_id, **kwargs):
        """
        https://developer.github.com/v3/projects/columns/#create-a-project-column
        """
        headers ={'Accept':'application/vnd.github.inertia-preview+json'}
        return self.post('/projects/{}/columns'.format(project_id), headers, **kwargs)

    def delete_a_project_column(self, column_id):
        """
        https://developer.github.com/v3/projects/columns/#delete-a-project-column
        """
        hearders = {'Accept':'application/vnd.github.inertia-preview+json'}
        return self.delete('/projects/columns/{}'.format(column_id), hearders = hearders)

    def update_a_project_column(self, column_id):
        """
        https://developer.github.com/v3/projects/columns/#update-a-project-column
        """
        hearders = {'Accept':'application/vnd.github.inertia-preview+json'}
        return self.patch('/projects/columns/{}'.format(column_id), hearders = hearders)

    def move_a_project_column(self, column_id, **kwargs):
        """
        https://developer.github.com/v3/projects/columns/#move-a-project-column
        """
        hearders = {'Accept':'application/vnd.github.inertia-preview+json'}
        return self.post('/projects/columns/{}/moves'.format(column_id), hearders = hearders, **kwargs)

    def get_a_project_column(self, column_id):
        """
        https://developer.github.com/v3/projects/columns/#get-a-project-column
        """
        hearders = {'Accept':'application/vnd.github.inertia-preview+json'}
        return self.get('/projects/columns/{}'.format(column_id), hearders = hearders)

    def list_project_columns(self, project_id):
        """
        https://developer.github.com/v3/projects/columns/#list-project-columns
        """
        hearders = {'Accept': 'application/vnd.github.inertia-preview+json'}
        return self.get('/projects/{}/columns'.format(project_id), hearders=hearders)



