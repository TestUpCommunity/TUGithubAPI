from core.rest_client import RestClient

class Repos(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(Repos, self).__init__(api_root_url, **kwargs)

    def list_your_repos(self, username, **kwargs):
    # def list_your_repos(self,**kwargs):
        # params={
        #     "visibility":visibility,
        #     "affiliation":affiliation,
        #     "type":type,
        #     "sort":sort,
        #     "direction":direction
        #
        #
        # }
        # return self.get("/user/repos",params = params)
        # return self.get("/user/repos", **kwargs)
        return self.get("/users/{}/repos".format(username), **kwargs)

    def list_organizition(self, org, **kwargs):
        return self.get("/orgs/{}/repos".format(org), **kwargs)

    def list_all_repositories(self, **kwargs):
        return self.get("/repositories", **kwargs)

    def create_user_repositories(self, **kwargs):
        return self.post("/user/repos",  **kwargs)

    def create_org_repositories(self, org, **kwargs):
        return self.post("/orgs/{}/repos".format(org),  **kwargs)

    def get_a_repositories(self, owner, repos, **kwargs ):
        return self.get("/repos/{}/{}".format(owner, repos), **kwargs)

    def edit_repositories(self, owner, repos, **kwargs):
        return self.patch("/repos/{}/{}".format(owner, repos), **kwargs)
    """
    以下函数为项目实战
    """

    def list_pull_requests(self, owner, repos, **kwargs):
        return self.get("/repos/{}/{}/pulls".format(owner, repos), **kwargs)

    def get_a_pull_request(self, owner, repos, pull_num, **kwargs):
        return self.get("/repos/{}/{}/pulls/{}".format(owner, repos, pull_num), **kwargs)

    def create_a_pull_request(self, owner, repos, **kwargs):
        return self.post("/repos/{}/{}/pulls".format(owner, repos), **kwargs)

    def update_a_pull_request_branch(self, owner, repos, pull_num, **kwargs):
        return self.put("/repos/{}/{}/pulls/{}/update-branch".format(owner, repos, pull_num), **kwargs)

    def update_a_pull_request(self, owner, repos, pull_num, **kwargs ):
        return self.patch("/repos/{}/{}/pulls/{}".format(owner, repos, pull_num), **kwargs)

    def list_commits(self, owner, repos, pull_num, **kwargs):
        return self.get("/repos/{}/{}/pulls/{}/commits".format(owner, repos, pull_num), **kwargs)

    def list_pull_requests_files(self, owner, repos, pull_num, **kwargs):
        return self.get("/repos/{}/{}/pulls/{}/files".format(owner, repos, pull_num), **kwargs)

    def check_merged(self, owner, repos, pull_num, **kwargs):
        return self.get("/repos/{}/{}/pulls/{}/merge".format(owner, repos, pull_num), **kwargs)

    def merge_pull_request(self, owner, repos, pull_num, **kwargs):
        return self.put("/repos/{}/{}/pulls/{}/merge".format(owner, repos, pull_num), **kwargs)








