#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:zhongxin
# datetime:2019/5/8 11:56 PM
from core.rest_client import RestClient


class Search(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(Search, self).__init__(api_root_url, **kwargs)

    def text_match_metadata(self, **kwargs):
        """
        https://developer.github.com/v3/search#text-match-metadata
        """
        self.session.headers["Accept"] = "application/vnd.github.v3.text-match+json"
        return self.get("/search/issues", **kwargs)

    def search_labels(self, **kwargs):
        """
        https://developer.github.com/v3/search#search-labels
        """
        return self.get("/search/labels", **kwargs)

    def search_topics(self, **kwargs):
        """
        https://developer.github.com/v3/search#search-topics
        """
        return self.get("/search/topics", **kwargs)

    def search_users(self, **kwargs):
        """
        https://developer.github.com/v3/search#search-users
        """
        return self.get("/search/users", **kwargs)

    def search_issues_and_pull_requests(self, **kwargs):
        """
        https://developer.github.com/v3/search/#search-issues-and-pull-requests
        """
        return self.get("/search/issues", **kwargs)

    def search_code(self, **kwargs):
        """
        https://developer.github.com/v3/search/#search-code
        """
        return self.get("/search/code", **kwargs)

    def search_commits(self, **kwargs):
        """
        https://developer.github.com/v3/search#search-commits
        """
        self.session.headers["Accept"] = "application/vnd.github.cloak-preview"
        return self.get("/search/commits", **kwargs)

    def search_repositories(self, style="base", **kwargs):
        """
        https://developer.github.com/v3/search/#search-repositories
        """
        if style == "base":
            pass
        else:
            self.session.headers["Accept"] = "application/vnd.github.mercy-preview+json"
        return self.get("/search/repositories", **kwargs)