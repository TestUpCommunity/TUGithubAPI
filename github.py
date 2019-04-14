from api.repositories.repos import Repos


class Github():
    def __init__(self, **kwargs):
        self.api_root_url = "https://api.github.com"
        self.repos = Repos(self.api_root_url, **kwargs)


if __name__ == '__main__':
    r = Github(token="xxxxx")
    username = "zhangting85"
    orgnname = "xxxx"

    # case 1
    data = {
        "name": "Hello-WorldXXX",
        "description": "This is your first repository",
        "homepage": "https://github.com",
        "private": False,
        "has_issues": True,
        "has_projects": True,
        "has_wiki": True
    }
    x = r.repos.create_user_repo(json=data)
    print(x.status_code)
    assert x.status_code == 201

    # case 2
    x = r.repos.create_organization_repo(org=orgnname, json=data)
    print(x.status_code)
    assert x.status_code == 201

    # case 3
    x = r.repos.get_repo(username, "Hello-World")
    print(x.status_code)
    assert x.status_code == 200
    print(x.text)

    # case 4
    data = {
        "name": "Hello-World",
        "description": "YYYY:This is your first repository ",
        "homepage": "https://github.com",
        "private": False,
        "has_issues": True,
        "has_projects": True,
        "has_wiki": True
    }

    x = r.repos.edit_repo(username, "Hello-World", json=data)
    print(x.status_code)
    print(x.text)
    assert x.status_code == 200
