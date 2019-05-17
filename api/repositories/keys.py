from core.rest_client import RestClient


class Keys(RestClient):

    def List_deploy_keys(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/keys#list-deploy-keys
        """
        return self.get('/repos/{}/{}/keys'.format(owner, repo), **kwargs)

    def Get_deploy_key(self, owner, repo, key_id, **kwargs):
        """
        https://developer.github.com/v3/repos/keys#get-a-deploy-key
        :return:
        """
        return self.get('/repos/{}/{}/keys/{}'.format(owner, repo, key_id), **kwargs)

    def Add_deploy_key(self, owner, repo, **kwargs):
        """
        https://developer.github.com/v3/repos/keys#get-a-deploy-key
        """
        return self.post('/repos/{}/{}/keys'.format(owner, repo), **kwargs)

    def Edit_deploy_key(self):
        """
        https://developer.github.com/v3/repos/keys/#remove-a-deploy-key
        """
        print('Deploy keys are immutable. If you need to update a key, remove the key and create a new one instead.')

    def Remove_deploy_key(self, owner, repo, key_id, **kwargs):
        """
        https://developer.github.com/v3/repos/keys#remove-a-deploy-key
        """
        return self.delete('/repos/{}/{}/keys/{}'.format(owner, repo, key_id), **kwargs)
