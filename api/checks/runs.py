from core.rest_client import RestClient


class Runs(RestClient):

    def list_check_runs(self, owner, repo, ref, **kwargs):
        """
        https://developer.github.com/v3/checks/runs/#list-check-runs-for-a-specific-ref
        """
        headers = {'Accept': 'application/vnd.github.antiope-preview+json'}
        return self.get("/repos/{}/{}/commits/{}/check-runs".format(owner, repo, ref), headers=headers, **kwargs)

    def create_a_check_runs(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/checks/runs/#create-a-check-run
        """
        headers = {'Accept': 'application/vnd.github.antiope-preview+json'}
        return self.post('/repos/{}/{}/check-runs'.format(owner, repo), headers = headers, **kwargs)

    def updata_a_check_runs(self, owner, repo, check_run_id, **kwargs):
        """
        https://developer.github.com/v3/checks/runs/#update-a-check-run
        """
        headers = {'Accept': 'application/vnd.github.antiope-preview+json'}
        return self.patch('/repos/{}/{}/check-runs/{}'.format(owner, repo, check_run_id), headers = headers, **kwargs)

    def list_check_runs_in_a_check_suite(self, owner, repo, check_suite_id, **kwargs):
        """
        https://developer.github.com/v3/checks/runs/#list-check-runs-in-a-check-suite
        """
        headers = {'Accept': 'application/vnd.github.antiope-preview+json'}
        return self.get('/repos/{}/{}/check-suites/{}/check-runs'.format(owner, repo, check_suite_id), headers = headers, **kwargs)

    def get_a_single_check_run(self, owner, repo, check_run_id, **kwargs):
        """
        https://developer.github.com/v3/checks/runs/#get-a-check-run
        """
        headers = {'Accept': 'application/vnd.github.antiope-preview+json'}
        return self.get('/repos/{}/{}/check-runs/{}'.format(owner, repo, check_run_id), headers = headers, **kwargs)

    def list_annotations_for_a_check_run(self, owner, repo, check_run_id, **kwargs):
        """
        https://developer.github.com/v3/checks/runs/#list-check-run-annotations
        """
        headers = {'Accept': 'application/vnd.github.antiope-preview+json'}
        return self.get('/repos/{}/{}/check-runs/{}/annotations'.format(owner, repo, check_run_id), headers = headers, **kwargs)



