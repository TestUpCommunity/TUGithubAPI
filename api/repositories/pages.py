from core.rest_client import RestClient
from copy import deepcopy

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

    def request_a_page_build(self, owner, repo):
        """
        https://developer.github.com/v3/repos/pages/#request-a-page-build
        """
        copied_headers = deepcopy(self.session.headers)
        copied_headers['Accept'] = 'application/vnd.github.mister-fantastic-preview+json'
        return self.post("/repos/{}/{}/pages/builds".format(owner, repo),headers = copied_headers)

    def update_information_about_a_pages_site(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/pages/#update-information-about-a-pages-site
        """
        copied_headers = deepcopy(self.session.headers)
        copied_headers['Accept'] = 'application/vnd.github.mister-fantastic-preview+json'
        return  self.put("/repos/{}/{}/pages".format(owner, repo), headers = copied_headers, **kwargs)

    def disable_a_pages_site(self, owner, repo):
        """
        https://developer.github.com/v3/repos/pages/#disable-a-pages-site
        """
        copied_headers = deepcopy(self.session.headers)
        copied_headers['Accept'] = 'application/vnd.github.switcheroo-preview+json'
        return self.delete("/repos/{}/{}/pages".format(owner, repo),headers = copied_headers)

    def enable_a_pages_site(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/pages/#enable-a-pages-site
        """
        copied_headers = deepcopy(self.session.headers)
        copied_headers['Accept'] = 'application/vnd.github.switcheroo-preview+json ' \
                                   ',application/vnd.github.mister-fantastic-preview+json'
        return self.post("/repos/{}/{}/pages".format(owner, repo), **kwargs)

    def get_information_about_a_pages_site(self, owner, repo):
        """
        https://developer.github.com/v3/repos/pages/#get-information-about-a-pages-site
        """
        copied_headers = deepcopy(self.session.headers)
        copied_headers['Accept'] = 'application/vnd.github.mister-fantastic-preview+json'
        return self.get("/repos/{}/{}/pages".format(owner, repo), headers = copied_headers)