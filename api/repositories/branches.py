from core.rest_client import RestClient


class Branches(RestClient):

    # 135
    def list_branches(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/branches/#list-branches
        """
        return self.get('/repos/{}/{}/branches'.format(owner, repo), **kwargs)

    # 136
    def get_branch(self, owner, repo, branch, **kwargs):
        """
        https://developer.github.com/v3/repos/branches/#get-branch
        """
        return self.get('/repos/{}/{}/branches/{}'.format(owner, repo, branch), **kwargs)

    # 137
    def get_branch_protection(self, owner, repo, branch, **kwargs):
        """
        https://developer.github.com/v3/repos/branches/#get-branch-protection
        """
        return self.get('/repos/{}/{}/branches/{}/protection'.format(owner, repo, branch), **kwargs)

    # 138
    def update_branch_protection(self, owner, repo, branch, **kwargs):
        """
        https://developer.github.com/v3/repos/branches/#update-branch-protection
        """
        return self.put('/repos/{}/{}/branches/{}/protection'.format(owner, repo, branch), **kwargs)

    # 139
    def remove_branch_protection(self, owner, repo, branch, **kwargs):
        """
        https://developer.github.com/v3/repos/branches/#remove-branch-protection
        """
        return self.delete('/repos/{}/{}/branches/{}/protection'.format(owner, repo, branch), **kwargs)

    # 140
    def get_required_status_checks_of_protected_branch(self, owner, repo, branch, **kwargs):
        """
        https://developer.github.com/v3/repos/branches/#get-required-status-checks-of-protected-branch
        """
        return self.get('/repos/{}/{}/branches/{}/protection/required_status_checks'.format(owner, repo, branch), **kwargs)

    # 141
    def update_required_status_checks_of_protected_branch(self, owner, repo, branch, **kwargs):
        """
        https://developer.github.com/v3/repos/branches/#update-required-status-checks-of-protected-branch
        """
        return self.patch('/repos/{}/{}/branches/{}/protection/required_status_checks'.format(owner, repo, branch), **kwargs)

    # 142
    def remove_required_status_checks_of_protected_branch(self, owner, repo, branch, **kwargs):
        """
        https://developer.github.com/v3/repos/branches/#remove-required-status-checks-of-protected-branch
        """
        return self.delete('/repos/{}/{}/branches/{}/protection/required_status_checks'.format(owner, repo, branch), **kwargs)

    # 143
    def list_required_status_checks_contexts_of_protected_branch(self, owner, repo, branch, **kwargs):
        """
        https://developer.github.com/v3/repos/branches/#list-required-status-checks-contexts-of-protected-branch
        """
        return self.get('/repos/{}/{}/branches/{}/protection/required_status_checks/contexts'.format(owner, repo, branch), **kwargs)

    # 144
    def replace_required_status_checks_contexts_of_protected_branch(self, owner, repo, branch, **kwargs):
        """
        https://developer.github.com/v3/repos/branches/#replace-required-status-checks-contexts-of-protected-branch
        """
        return self.put('/repos/{}/{}/branches/{}/protection/required_status_checks/contexts'.format(owner, repo, branch), **kwargs)

    # 145
    def add_required_status_checks_contexts_of_protected_branch(self, owner, repo, branch, **kwargs):
        """
        https://developer.github.com/v3/repos/branches/#add-required-status-checks-contexts-of-protected-branch
        """
        return self.post('/repos/{}/{}/branches/{}/protection/required_status_checks/contexts'.format(owner, repo, branch), **kwargs)

    # 146
    def remove_required_status_checks_contexts_of_protected_branch(self, owner, repo, branch, **kwargs):
        """
        https://developer.github.com/v3/repos/branches/#remove-required-status-checks-contexts-of-protected-branch
        """
        return self.delete('/repos/{}/{}/branches/{}/protection/required_status_checks/contexts'.format(owner, repo, branch), **kwargs)

    # 147
    def get_pull_request_review_enforcement_of_protected_branch(self, owner, repo, branch, **kwargs):
        """
        https://developer.github.com/v3/repos/branches/#get-pull-request-review-enforcement-of-protected-branch
        """
        return self.get('/repos/{}/{}/branches/{}/protection/required_pull_request_reviews'.format(owner, repo, branch), **kwargs)

    # 148
    def update_pull_request_review_enforcement_of_protected_branch(self, owner, repo, branch, **kwargs):
        """
        https://developer.github.com/v3/repos/branches/#update-pull-request-review-enforcement-of-protected-branch
        """
        return self.patch('/repos/{}/{}/branches/{}/protection/required_pull_request_reviews'.format(owner, repo, branch), **kwargs)

    # 149
    def remove_pull_request_review_enforcement_of_protected_branch(self, owner, repo, branch, **kwargs):
        """
        https://developer.github.com/v3/repos/branches/#remove-pull-request-review-enforcement-of-protected-branch
        """
        return self.delete('/repos/{}/{}/branches/{}/protection/required_pull_request_reviews'.format(owner, repo, branch), **kwargs)

    # 150
    def get_required_signatures_of_protected_branch(self, owner, repo, branch, **kwargs):
        """
        https://developer.github.com/v3/repos/branches/#get-required-signatures-of-protected-branch
        """
        return self.get('/repos/{}/{}/branches/{}/protection/required_signatures'.format(owner, repo, branch), **kwargs)

    # 151
    def add_required_signatures_of_protected_branch(self, owner, repo, branch, **kwargs):
        """
        https://developer.github.com/v3/repos/branches/#add-required-signatures-of-protected-branch
        """
        return self.post('/repos/{}/{}/branches/{}/protection/required_signatures'.format(owner, repo, branch),
                         **kwargs)

    # 152
    def remove_required_signatures_of_protected_branch(self, owner, repo, branch, **kwargs):
        """
        https://developer.github.com/v3/repos/branches/#remove-required-signatures-of-protected-branch
        """
        return self.delete('/repos/{}/{}/branches/{}/protection/required_signatures'.format(owner, repo, branch), **kwargs)

    # 153
    def get_admin_enforcement_of_protected_branch(self, owner, repo, branch, **kwargs):
        """
        https://developer.github.com/v3/repos/branches/#get-admin-enforcement-of-protected-branch
        """
        return self.get('/repos/{}/{}/branches/{}/protection/enforce_admins'.format(owner, repo, branch), **kwargs)

    # 154
    def add_admin_enforcement_of_protected_branch(self, owner, repo, branch, **kwargs):
        """
        https://developer.github.com/v3/repos/branches/#add-admin-enforcement-of-protected-branch
        """
        return self.post('/repos/{}/{}/branches/{}/protection/enforce_admins'.format(owner, repo, branch), **kwargs)

    # 155
    def remove_admin_enforcement_of_protected_branch(self, owner, repo, branch, **kwargs):
        """
        https://developer.github.com/v3/repos/branches/#remove-admin-enforcement-of-protected-branch
        """
        return self.delete('/repos/{}/{}/branches/{}/protection/enforce_admins'.format(owner, repo, branch), **kwargs)

    # 156
    def get_restrictions_of_protected_branch(self, owner, repo, branch, **kwargs):
        """
        https://developer.github.com/v3/repos/branches/#get-restrictions-of-protected-branch
        """
        return self.get('/repos/{}/{}/branches/{}/protection/restrictions'.format(owner, repo, branch), **kwargs)

    # 157
    def remove_restrictions_of_protected_branch(self, owner, repo, branch, **kwargs):
        """
        https://developer.github.com/v3/repos/branches/#remove-restrictions-of-protected-branch
        """
        return self.delete('/repos/{}/{}/branches/{}/protection/restrictions'.format(owner, repo, branch), **kwargs)

    # 158
    def list_team_restrictions_of_protected_branch(self, owner, repo, branch, **kwargs):
        """
        https://developer.github.com/v3/repos/branches/#list-team-restrictions-of-protected-branch
        """
        return self.get('/repos/{}/{}/branches/{}/protection/restrictions/teams'.format(owner, repo, branch), **kwargs)

    # 159
    def replace_team_restrictions_of_protected_branch(self, owner, repo, branch, **kwargs):
        """
        https://developer.github.com/v3/repos/branches/#replace-team-restrictions-of-protected-branch
        """
        return self.put('/repos/{}/{}/branches/{}/protection/restrictions/teams'.format(owner, repo, branch), **kwargs)

    # 160
    def add_team_restrictions_of_protected_branch(self, owner, repo, branch, **kwargs):
        """
        https://developer.github.com/v3/repos/branches/#add-team-restrictions-of-protected-branch
        """
        return self.post('/repos/{}/{}/branches/{}/protection/restrictions/teams'.format(owner, repo, branch), **kwargs)

    # 161
    def remove_team_restrictions_of_protected_branch(self, owner, repo, branch, **kwargs):
        """
        https://developer.github.com/v3/repos/branches/#remove-team-restrictions-of-protected-branch
        """
        return self.delete('/repos/{}/{}/branches/{}/protection/restrictions/teams'.format(owner, repo, branch), **kwargs)

    # 162
    def list_user_restrictions_of_protected_branch(self, owner, repo, branch, **kwargs):
        """
        https://developer.github.com/v3/repos/branches/#list-user-restrictions-of-protected-branch
        """
        return self.get('/repos/{}/{}/branches/{}/protection/restrictions/users'.format(owner, repo, branch), **kwargs)

    # 163
    def replace_user_restrictions_of_protected_branch(self, owner, repo, branch, **kwargs):
        """
        https://developer.github.com/v3/repos/branches/#replace-user-restrictions-of-protected-branch
        """
        return self.put('/repos/{}/{}/branches/{}/protection/restrictions/users'.format(owner, repo, branch), **kwargs)

    # 164
    def add_user_restrictions_of_protected_branch(self, owner, repo, branch, **kwargs):
        """
        https://developer.github.com/v3/repos/branches/#add-user-restrictions-of-protected-branch
        """
        return self.post('/repos/{}/{}/branches/{}/protection/restrictions/users'.format(owner, repo, branch), **kwargs)

    # 165
    def remove_user_restrictions_of_protected_branch(self, owner, repo, branch, **kwargs):
        """
        https://developer.github.com/v3/repos/branches/#remove-user-restrictions-of-protected-branch

        """
        return self.delete('/repos/{}/{}/branches/{}/protection/restrictions/users'.format(owner, repo, branch), **kwargs)
