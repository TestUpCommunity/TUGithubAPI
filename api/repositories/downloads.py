from core.rest_client import RestClient

class Downloads(RestClient):

    def list_downloads_for_a_repository(self, owner, repo):
        """
        https://developer.github.com/v3/repos/downloads/#list-downloads-for-a-repository
        """
        return self.get("/repos/{}/{}/downloads".format(owner, repo))

    def get_a_single_downloads(self, owner, repo, download_id):
        """
        https://developer.github.com/v3/repos/downloads/#get-a-single-download
        """
        return self.get("/repos/{}/{}/downloads/{}".format(owner, repo, download_id))

    def delete_a_downlaod(self, owner, repo, download_id):
        """
        https://developer.github.com/v3/repos/downloads/#delete-a-download
        """
        return self.delete("/repos/{}/{}/downloads/{}".format(owner, repo, download_id))