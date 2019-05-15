from core.rest_client import RestClient


class Statistics(RestClient):
    def get_contributors_list(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/statistics/#get-contributors-list-with-additions-deletions-and-commit-counts
        """
        return self.get("/repos/{}/{}/stats/contributors".format(owner, repo), **kwargs)

    def get_last_year_commit(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/statistics/#get-the-last-year-of-commit-activity-data
        """
        return self.get("/repos/{}/{}/stats/commit_activity".format(owner, repo), **kwargs)

    def get_number_of_additions_deletions(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/statistics/#get-the-number-of-additions-and-deletions-per-week
        """
        return self.get("/repos/{}/{}/stats/code_frequency".format(owner, repo), **kwargs)

    def get_weekly_commit_count(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/statistics/#get-the-weekly-commit-count-for-the-repository-owner-and-everyone-else
        """
        return self.get("/repos/{}/{}/stats/participation".format(owner, repo), **kwargs)

    def get_numbers_commits_hour(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/statistics/#get-the-number-of-commits-per-hour-in-each-day
        """
        return self.get("/repos/{}/{}/stats/punch_card".format(owner, repo), **kwargs)
