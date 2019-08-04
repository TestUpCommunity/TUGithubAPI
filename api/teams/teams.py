from core.rest_client import RestClient

class Teams(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(Teams, self).__init__(api_root_url, **kwargs)

    def list_teams(self, org, **kwargs):
        '''
        https://developer.github.com/v3/teams/#list-teams
        '''
        return self.get('/orgs/%s/teams' %(org), **kwargs)

    def get_team(self, team_id, **kwargs):
        '''
        https://developer.github.com/v3/teams/#get-team
        '''
        return self.get('/teams/%s' %(team_id), **kwargs)

    def get_team_by_name(self, org, team_slug, **kwargs):
        '''
        https://developer.github.com/v3/teams/#get-team-by-name
        '''
        return self.get('/orgs/%s/teams/%s' %(org, team_slug), **kwargs)

    def create_team(self, org, **kwargs):
        '''
        https://developer.github.com/v3/teams/#create-team
        '''
        return self.post('/org/%s/teams' %(org), **kwargs)

    def edit_team(self, team_id, **kwargs):
        '''
        https://developer.github.com/v3/teams/#edit-team
        '''
        return self.patch('/teams/%s' %(team_id), **kwargs)

    def delete_team(self, team_id, **kwargs):
        '''
        https://developer.github.com/v3/teams/#delete-team
        '''
        return self.delete('teams/%s' %(team_id), **kwargs)

    def list_child_teams(self, team_id, **kwargs):
        '''
        https://developer.github.com/v3/teams/#list-child-teams
        '''
        return self.get('/teams/%s/teams' %(team_id), **kwargs)

    def list_team_repos(self, team_id, **kwargs):
        '''
        https://developer.github.com/v3/teams/#list-team-repos
        '''
        return self.get('/teams/%s/repos' %(team_id), **kwargs)

    def check_team_manages_repository(self, team_id, owner, repo, **kwargs):
        '''
        https://developer.github.com/v3/teams/#check-if-a-team-manages-a-repository
        '''
        return self.get('/teams/%s/repos/%s/%s' %(team_id, owner, repo), **kwargs)

    def add_update_team_repository(self, team_id, owner, repo, **kwargs):
        '''
        https://developer.github.com/v3/teams/#add-or-update-team-repository
        '''
        return self.put('/teams/%s/repos/%s/%s' %(team_id, owner, repo), **kwargs)

    def remove_team_repository(self, team_id, owner, repo, **kwargs):
        '''
        https://developer.github.com/v3/teams/#remove-team-repository
        '''
        return self.delete('/teams/%s/repos/%s/%s' %(team_id, owner, repo), **kwargs)

    def list_user_teams(self, **kwargs):
        '''
        https://developer.github.com/v3/teams/#list-user-teams
        '''
        return self.get('/user/teams', **kwargs)

    def list_team_projects(self, team_id, **kwargs):
        '''
        https://developer.github.com/v3/teams/#list-team-projects
        '''
        return self.get('/trams/%s/projects' %(team_id), **kwargs)

    def reviewa_team_project(self, team_id, project_id, **kwargs):
        '''
        https://developer.github.com/v3/teams/#reviewa-team-project
        '''
        return self.get('/teams/%s/projects/%s' %(team_id, project_id), **kwargs)

    def add_or_update_team_project(self, team_id, project_id, **kwargs):
        '''
        https://developer.github.com/v3/teams/#add-or-update-team-project
        '''
        return self.put('/teams/%s/projects/%s' %(team_id, project_id), **kwargs)

    def remove_team_project(self, team_id, project_id, **kwargs):
        '''
        https://developer.github.com/v3/teams/#remove-team-project
        '''
        return self.delete('/teams/%s/projects/%s' %(team_id, project_id), **kwargs)

