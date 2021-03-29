from api.repositories.repos import Repos
from api.issues.issues import Issues
from api.checks.checks import Checks
from api.interactions.interactions import Interactions
from api.apps.apps import Apps

class Github():
    def __init__(self, **kwargs):
        self.api_root_url = "https://api.github.com"
        self.repos = Repos(self.api_root_url, **kwargs)
        self.issues = Issues(self.api_root_url, **kwargs)
        self.checks = Checks(self.api_root_url, **kwargs)
        self.interactions = Interactions(self.api_root_url, **kwargs)
        self.apps = Apps(self.api_root_url, **kwargs)

