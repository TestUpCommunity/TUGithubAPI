from api.repositories.repos import Repos
from api.repositories.traffic import Traffic
from api.repositories.keys import Keys
from api.issues.issues import Issues


class Github():
    def __init__(self, **kwargs):
        self.api_root_url = "https://api.github.com"
        self.repos = Repos(self.api_root_url,**kwargs)
        self.issues = Issues(self.api_root_url,**kwargs)
        self.traffic = Traffic(self.api_root_url,**kwargs)
        self.keys = Keys(self.api_root_url,**kwargs)