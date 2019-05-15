from core.teamsrepo import Teamsrepo

class Teams(Teamsrepo):
    def __init__(self, api_root_url, **kwargs):
        super(Teams, self).__init__(api_root_url, **kwargs)

    def list_teams(self, org, **kwargs):
        '''
        https://developer.github.com/v3/teams#list-teams
        '''
        return self.get('/orgs/{}/teams'.format(org), **kwargs)

    def get_teams(self, team_id, **kwargs):
        '''
        https://developer.github.com/v3/teams/#get-team
        '''
        return self.get('/teams/{}'.format(team_id), **kwargs)

    def get_team_by_name(self, org, team_slug, **kwargs):
        '''
        https://developer.github.com/v3/teams#get-team-by-name
        '''
        return self.get('/orgs/{}/teams/{}'.format(org, team_slug), **kwargs)

    def create_team(self, org, **kwargs):
        '''
        https://developer.github.com/v3/teams#create-team
        '''
        return self.post('/orgs/{}/teams'.format(org), **kwargs)

    def edit_team(self, tram_id, **kwargs):
        '''
        https://developer.github.com/v3/teams/#edit-team
        '''
        return self.patch('/teams/{}'.format(tram_id), **kwargs)

    def delete_team(self, tram_id, **kwargs):
        '''
        https://developer.github.com/v3/teams/#edit-team
        '''
        return self.delete('/teams/{}'.format(tram_id), **kwargs)

    def list_child_teams(self, team_id, **kwargs):
        '''
        https://developer.github.com/v3/teams#list-child-teams
        '''
        return self.get('/teams/{}/teams'.format(team_id), **kwargs)

    def list_team_repos(self, team_id, **kwargs):
        '''
        https://developer.github.com/v3/teams#list-team-repos
        '''
        return self.get('/teams/{}/repos'.format(team_id), **kwargs)

    def check_manages_repository(self, team_id, owner, repo, **kwargs):
        '''
        https://developer.github.com/v3/teams#check-if-a-team-manages-a-repository
        '''
        return self.get('/teams/{}/repos/{}/{}'.format(team_id, owner, repo), **kwargs)

    def add_update_repository(self, team_id, owner, repo, **kwargs):
        '''
        https://developer.github.com/v3/teams#add-or-update-team-repository
        '''
        return self.put('/teams/{}/repos/{}/{}'.format(team_id, owner, repo), **kwargs)

    def remove_team_repository(self, team_id, owner, repo, **kwargs):
        '''
        https://developer.github.com/v3/teams#remove-team-repository
        '''
        return self.delete('/trams/{}/repos/{}/{}'.format(team_id, owner, repo), **kwargs)

    def list_user_teams(self, **kwargs):
        '''
        https://developer.github.com/v3/teams#list-user-teams
        '''
        return self.get('/user/teams', **kwargs)

    def list_team_projects(self, team_id, **kwargs):
        '''
        https://developer.github.com/v3/teams/#list-team-projects
        '''
        return self.get('/teams/{}/projects'.format(team_id), **kwargs)

    def review_team_project(self, team_id, project_id, **kwargs):
        '''
        https://developer.github.com/v3/teams#review-a-team-project
        '''
        return self.get('/teams/{}/projects/{}'.format(team_id, project_id), **kwargs)

    def add_update_team_project(self, team_id, project_id, **kwargs):
        '''
        https://developer.github.com/v3/teams#add-or-update-team-project
        '''
        return self.put('/teams/{}/projects/{}'.format(team_id, project_id), **kwargs)

    def teams_remove_project(self, team_id, project_id, **kwargs):
        '''
        https://developer.github.com/v3/teams#remove-team-project
        '''
        return self.delete('/teams/{}/projects/{}'.format(team_id, project_id), **kwargs)

