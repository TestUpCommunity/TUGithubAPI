from core.rest_client import RestClient


class Pages(RestClient):

    def get_latest_pages_build(self, owner, repo):
        """
        https://developer.github.com/v3/repos/pages/#get-latest-pages-build
        """
        return self.get("/repos/{}/{}/pages/builds/latest".format(owner, repo))

    def List_pages_builds(self, owner, repo):
        """
        https://developer.github.com/v3/repos/pages/#list-pages-builds
        """
        return self.get("/repos/{}/{}/pages/builds".format(owner, repo))

    def request_a_page_build(self, owner, repo, access = False):
        """
        https://developer.github.com/v3/repos/pages/#request-a-page-build
        """
        if access:
            headers= {'Accept':'application/vnd.github.switcheroo-preview+json'}
            return self.post("/repos/{}/{}/pages/builds".format(owner, repo), headers)
        return self.post("/repos/{}/{}/pages/builds".format(owner, repo))

    def update_information_about_a_pages_site(self, owner, repo, developers = False, **kwargs):
        """
        https://developer.github.com/v3/repos/pages/#update-information-about-a-pages-site
        """
        if developers:
            headers = {'Accept':'application/vnd.github.mister-fantastic-preview+json'}
            return  self.put("/repos/{}/{}/pages".format(owner, repo), headers = headers, **kwargs)
        else:
            return  self.put("/repos/{}/{}/pages".format(owner, repo), **kwargs)

    def disable_a_pages_site(self, owner, repo, developers = False):
        """
        https://developer.github.com/v3/repos/pages/#disable-a-pages-site
        """
        if developers:
            headers = {'Accept':'application/vnd.github.switcheroo-preview+json'}
            self.delete("/repos/{}/{}/pages".format(owner, repo),headers = headers)
        else:
            self.delete("/repos/{}/{}/pages".format(owner, repo))

    def enable_a_pages_site(self, owner, repo, access  = False, developers = False, **kwargs):
        """
        https://developer.github.com/v3/repos/pages/#enable-a-pages-site
        """
        if access:
            headers = {'Accept':'application/vnd.github.switcheroo-preview+json'}
            return self.post("/repos/{}/{}/pages".format(owner, repo), headers = headers, **kwargs)
        elif developers:
            headers = {'Accept': 'application/vnd.github.mister-fantastic-preview+json'}
            return self.post("/repos/{}/{}/pages".format(owner, repo), headers = headers, **kwargs)
        else:
            return self.post("/repos/{}/{}/pages".format(owner, repo), **kwargs)

    def get_information_about_a_pages_site(self, owner, repo, developers = False):
        """
        https://developer.github.com/v3/repos/pages/#get-information-about-a-pages-site
        """
        if developers:
            headers = {'Accept': 'application/vnd.github.mister-fantastic-preview+json'}
            return self.get("/repos/{}/{}/pages".format(owner, repo), headers = headers)
        else:
            return self.get("/repos/{}/{}/pages".format(owner, repo))