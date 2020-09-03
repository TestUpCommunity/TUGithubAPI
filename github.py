from api.repositories.repos import Repos


class Github():
    def __init__(self, **kwargs):
        self.api_root_url = "https://api.github.com"
        self.repos = Repos(self.api_root_url, **kwargs)


if __name__ == '__main__':
    r = Github(token="xxxxxxxxxxxxxx")
    x = r.repos.list_your_repos()
    print(x.text)

    r = Github(username="xxxxxx", password="xxxxx")
    x = r.repos.list_your_repos()
    print(x.text)
