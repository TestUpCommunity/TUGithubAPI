from api.teamsapi.teams import Teams

class Gitteams():
    def __init__(self, **kwargs):
        self.api_root_url = 'https://developer.github.com'
        self.teams = Teams(self.api_root_url, **kwargs)

if __name__ == '__main__':
    r = Gitteams(token = '2a2e752e490224ea4bf2c0d1a2975a1acae8c99b')
    username = 'xiaoxieaichirou'
    x = r.teams.get_teams('')
    print(x.status_code)
    assert x.status_code == 200
    print(x.text)
