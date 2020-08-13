from api.repositories.repos import Repos

class Github():
    def __init__(self, **kwargs):
        self.api_root_url = "https://api.github.com"
        self.repos = Repos(self.api_root_url, **kwargs )

if __name__ == '__main__':
    # r = Github(token="67c64dcc041f10947fabdb067d821fac1a1aeef7")
    # username = "cassie01"
    # orgname = "hello0811world"
    #
    # # case 1
    # """注意GitHub类中的网址需要是https"""
    # data = {
    #     "name" : "Test01",
    #     "description":"this is your first repository in org",
    #     "homepage": "https://github.com",
    #     "private" : False,
    #     "has_issues": True,
    #     "has_projects": True,
    #     "has_wiki": True
    # }
    # x = r.repos.create_user_repositories(json=data)
    # print(x.status_code)
    # assert x.status_code == 201



    #case 2
    # """需要先在GitHub中建立organization"""
    # x = r.repos.create_org_repositories(org= orgname, json = data)
    # print(x.status_code)
    # assert x.status_code == 201

    #case 3
    # x = r.repos.get_a_repositories(username, "Test01")
    # print(x.status_code)
    # assert x.status_code == 200

    #case 4
    # data = {
    #     "name": "Test01",
    #     "description": "this is not your big  repository in org",
    #     "homepage": "https://github.com",
    #     "private": False,
    #     "has_issues": True,
    #     "has_projects": True,
    #     "has_wiki": True
    # }
    # x = r.repos.edit_repositories(username, 'Test01', json = data)
    # print(x.status_code)
    # assert x.status_code == 200

    """
    项目实战：
    API文档：https://developer.github.com/v3/pulls/#custom-media-types
    """
    r = Github(token="67c64dcc041f10947fabdb067d821fac1a1aeef7")
    username = "cassie01"
    orgname = "teach_005"
    #case 1
    # data = {
    #     "state": all,
    #     "direction": "desc"
    # }
    # x = r.repos.list_pull_requests(username, orgname, json = data)
    # print(x.text)
    # assert x.status_code == 200

    #case 2
    # x = r.repos.get_a_pull_request(username, orgname, 3)
    # print(x)
    # assert x.status_code == 200