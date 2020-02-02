from core.rest_client import RestClient

class Contents(RestClient):

    def get_the_readme(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/contents/#get-the-readme
        """
        return self.get("/repos/{}/{}/readme".format(owner, repo), **kwargs)

    def get_contents(self, owner, repo, path, **kwargs):
        """
        https://developer.github.com/v3/repos/contents/#get-contents
        """
        return self.get("/repos/{}/{}/contents/{}".format(owner, repo, path), **kwargs)

    def create_or_update_file(self, owner, repo, path, **kwargs):
        """
        https://developer.github.com/v3/repos/contents/#create-or-update-a-file
        """
        return self.put("/repo/{}/{}/contents/{}".format(owner, repo, path), **kwargs)

    def delete_a_file(self, owner, repo, path, **kwargs):
        """
        https://developer.github.com/v3/repos/contents/#delete-a-file
        """
        return self.delete("/repo/{}/{}/contents/{}".format(owner, repo, path), **kwargs)

    def get_archive_link(self, owner, repo, archive_format, ref):
        """
        https://developer.github.com/v3/repos/contents/#get-archive-link
        """
        return self.get("/repos/{}/{}/{}/".format(owner, repo, archive_format, ref))
