from api.repositories.repos import Repos
from api.issues.issues import Issues
from api.hooks.hooks import Hooks


class Github():
    def __init__(self, **kwargs):
        self.api_root_url = "https://api.github.com"
        self.repos = Repos(self.api_root_url, **kwargs)
        self.issues = Issues(self.api_root_url, **kwargs)
        self.hooks = Hooks(self.api_root_url, **kwargs)

if __name__ == '__main__':
    r = Github(token="xxx")
    username = "zhangting85"
    orgname = "TestUpCommunity"
    reponame ="simpleWebtest"
    # case 1
    x = r.repos.get_repo(username, reponame)
    print(x.status_code)
    assert x.status_code == 200
    print(x.text)
    x = r.repos.traffic.list_clones(username, reponame)
    assert x.status_code == 200
    print(x.text)

