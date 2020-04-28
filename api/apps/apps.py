from TUGithubAPI.core.rest_client import RestClient


class Apps(RestClient):
    def get_a_single_GitHub_App(self,app_slug,**kwargs):
        return self.get('/apps/{}'.format(app_slug),**kwargs)

    def get_the_authenticated_GitHub_App(self, **kwargs):
        return self.get('/app', **kwargs)

    def list_installations(self, **kwargs):
        return self.get('/app/installations', **kwargs)

    def get_an_installation(self, installation_id, **kwargs):
        return self.get('/app/installations/{}'.format(installation_id), **kwargs)

    def delete_an_installation(self, installation_id, **kwargs):
        return self.delete('/app/installations/{}'.format(installation_id), **kwargs)

    def create_a_new_installation_token(self, installation_id, **kwargs):
        return self.post('/app/installations/{}/access_tokens'.format(installation_id), **kwargs)

    def get_an_organization_installation(self, org, **kwargs):
        return self.get('/orgs/{}/installation'.format(org), **kwargs)

    def get_a_repository_installation(self, owner, repo, **kwargs):
        return self.get('/repos/{}/{}/installation'.format(owner, repo), **kwargs)

    def get_a_user_installation(self, username, **kwargs):
        return self.get('/users/{}/installation'.format(username), **kwargs)

    def create_a_GitHub_App_from_a_manifest(self, code, **kwargs):
        return self.post(' /app-manifests/{}/conversions'.format(code), **kwargs)


