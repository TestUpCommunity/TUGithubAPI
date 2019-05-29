from core.rest_client import RestClient


class Orgs(RestClient):
    # 428
    def list_your_organizations(self, **kwargs):
        """
        https://developer.github.com/v3/orgs#list-your-organizations
        """
        return self.get("/user/orgs", **kwargs)

    # 429
    def list_all_organizations(self, **kwargs):
        """
            https://developer.github.com/v3/orgs#list-all-organizations
        """
        return self.get("/organizations", **kwargs)

    # 430
    def list_user_organizations(self, username, **kwargs):
        """
            https://developer.github.com/v3/orgs#list-user-organizations
        """
        return self.get("/users/{}/orgs".format(username), **kwargs)

    # 431
    def get_an_organization(self, org, **kwargs):
        """
            https://developer.github.com/v3/orgs/#get-an-organization
        """
        return self.get("/orgs/{}".format(org), **kwargs)

    # 432
    def edit_an_organization(self, org, **kwargs):
        """
            https://developer.github.com/v3/orgs/#edit-an-organization
        """
        return self.patch("/orgs/{}".format(org), **kwargs)

    # 433
    def list_credential_authorization_for_an_organization(self, org, **kwargs):
        """
            https://developer.github.com/v3/orgs/#list-credential-authorizations-for-an-organization
        """
        return self.get("/orgs/{}/credential-authorizations".format(org), **kwargs)
