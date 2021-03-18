from core.rest_client import RestClient

class Deployments(RestClient):

    def list_deployments(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/deployments/#list-deployments
        """
        headers = {'Accept':'application/vnd.github.ant-man-preview+json'}
        return self.get("/repos/{}/{}/deployments".format(owner, repo), headers = headers, **kwargs)

    def get_a_single_deployment(self, owner, repo, deployment_id):
        """
        https://developer.github.com/v3/repos/deployments/#get-a-single-deployment
        """
        headers = {'Accept':'application/vnd.github.machine-man-preview'}
        return self.get("/repos/{}/{}/deployments/{}".format(owner, repo, deployment_id), headers=headers)

    def create_deployment(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/deployments/#create-a-deployment
        """
        headers = {'Accept':'application/vnd.github.ant-man-preview+json'}
        return self.post("/repos/{}/{}/deployments".format(owner, repo),headers=headers, **kwargs)

    def list_deployment_statuses(self, owner, repo, deployment_id):
        """
        https://developer.github.com/v3/repos/deployments/#list-deployment-statuses
        """
        headers = {'Accept':'application/vnd.github.ant-man-preview+json,application/vnd.github.flash-preview+json'}
        return self.get("/repos/{}/{}/deployments/{}/statuses".format(owner, repo, deployment_id),headers=headers)

    def get_a_single_deployment_status(self, owner, repo, deployment_id, status_id):
        """
        https://developer.github.com/v3/repos/deployments/#get-a-single-deployment-status
        """
        headers = {'Accept':'application/vnd.github.machine-man-preview,'
                            'application/vnd.github.flash-preview+json,'
                            'application/vnd.github.ant-man-preview+json'}
        return self.get("/repos/{}/{}/deployments/{}/statuses/{}",format(owner, repo, deployment_id, status_id),headers=headers)

    def create_a_deployment_status(self, owner, repo, deployment_id, **kwargs):
        """
        https://developer.github.com/v3/repos/deployments/#create-a-deployment-status
        """
        headers = {'Accept':'application/vnd.github.flash-preview+json,'
                            'application/vnd.github.ant-man-preview+json'}
        return self.post("/repos/{}/{}/deployments/{}/statuses".format(owner, repo, deployment_id), headers=headers, **kwargs)

