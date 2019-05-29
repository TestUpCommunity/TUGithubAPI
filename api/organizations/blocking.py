from core.rest_client import RestClient


class Blocking(RestClient):
    # 435
    def list_blocked_users(self, org, **kwargs):
        """
        https://developer.github.com/v3/orgs/blocking#list-blocked-users
        """
        return self.get('/orgs/{}/blocks'.format(org), **kwargs)


if __name__ == "__main__":
    r = Blocking("https://github.com/")
    t = r.list_blocked_users("")
    print(t.text)


