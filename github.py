from api.repositories.repos import Repos
from api.issues.issues import Issues
from api.issues.timeline import Timeline


class Github():
    def __init__(self, **kwargs):
        self.api_root_url = "https://api.github.com"
        self.repos = Repos(self.api_root_url, **kwargs)
        self.issues = Issues(self.api_root_url, **kwargs)
        self.timeline = Timeline(self.api_root_url, **kwargs)
