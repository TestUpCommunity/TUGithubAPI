from api.repositories.repos import Repos
from api.issues.issues import Issues
from api.checks.checks import Checks
from api.interactions.interactions import Interactions
from api.apps.apps import Apps
from api.orgs.orgs import Orgs
from operations.repo import delete_repo_from_user_by_name


class Github():
    def __init__(self, **kwargs):
        self.api_root_url = "https://api.github.com"
        self.repos = Repos(self.api_root_url, **kwargs)
        self.issues = Issues(self.api_root_url, **kwargs)
        self.checks = Checks(self.api_root_url, **kwargs)
        self.interactions = Interactions(self.api_root_url, **kwargs)
        self.apps = Apps(self.api_root_url, **kwargs)
        self.orgs = Orgs(self.api_root_url, **kwargs)


if __name__ == '__main__':
    g = Github(username="namelaowang", password ="ghl6032069")

    r = g.repos.branches.add_required_status_checks_contexts_of_protected_branch('namelaowang', 'TestapiTest', 'master')
    print(r)
    print(r.content)

