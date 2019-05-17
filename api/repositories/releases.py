from core.rest_client import RestClient


class Releases(RestClient):
    def list_releases_for_repos(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/releases/#list-releases-for-a-repository
        """
        return self.get("/repos/{}/{}/releases".format(owner, repo), **kwargs)

    def get_single_release(self, owner, repo, release_id, **kwargs):
        """
        https://developer.github.com/v3/repos/releases/#get-a-single-release
        """
        return self.get("/repos/{}/{}/releases/{}".format(owner, repo, release_id), **kwargs)

    def get_latest_release(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/releases/#get-the-latest-release
        """
        return self.get("/repos/{}/{}/releases/latest".format(owner, repo), **kwargs)

    def get_release_by_tag_name(self, owner, repo, tag, **kwargs):
        """
        https://developer.github.com/v3/repos/releases/#get-a-release-by-tag-name
        """
        return self.get("/repos/{}/{}/releases/tags/{}".format(owner, repo, tag), **kwargs)

    def create_release(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/releases/#create-a-release
        """
        return self.post("/repos/{}/{}/releases".format(owner, repo), **kwargs)

    def edit_release(self, owner, repo, release_id, **kwargs):
        """
        https://developer.github.com/v3/repos/releases/#edit-a-release
        """
        return self.patch("/repos/{}/{}/releases/{}".format(owner, repo, release_id), **kwargs)

    def delete_release(self, owner, repo, release_id, **kwargs):
        """
        https://developer.github.com/v3/repos/releases/#delete-a-release
        """
        return self.delete("/repos/{}/{}/releases/{}".format(owner, repo, release_id), **kwargs)

    def delete_release_asset(self, owner, repo, asset_id, **kwargs):
        """
        https://developer.github.com/v3/repos/releases/#delete-a-release-asset
        """
        return self.delete("/repos/{}/{}/releases/assets/{}".format(owner, repo, asset_id), **kwargs)

    def edit_realease_asset(self, owner, repo, asset_id, **kwargs):
        """
        https://developer.github.com/v3/repos/releases/#edit-a-release-asset
        """
        return self.patch("/repos/{}/{}/releases/assets/{}".format(owner, repo, asset_id), **kwargs)

    def get_single_release_asset(self, owner, repo, asset_id, **kwargs):
        """
        https://developer.github.com/v3/repos/releases/#get-a-single-release-asset
        """
        return self.get("/repos/{}/{}/releases/assets/{}".format(owner, repo, asset_id), **kwargs)

    def upload_release_asset(self, upload_url, **kwargs):
        """
        https://developer.github.com/v3/repos/releases/#upload-a-release-asset
        """
        return self.post("{}".format(upload_url), **kwargs)

    def list_assets_for_release(self, owner, repo, release_id, **kwargs):
        """
        https://developer.github.com/v3/repos/releases/#list-assets-for-a-release
        """
        return self.get("/repos/{}/{}/releases/{}/assets".format(owner, repo, release_id), **kwargs)
