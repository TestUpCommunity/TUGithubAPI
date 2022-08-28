from core.rest_client import RestClient


class Permission(RestClient):
    def list_ssh_for_current_user(self, **kwargs):
        """
        https://docs.github.com/en/rest/users/keys#list-public-ssh-keys-for-the-authenticated-user
        :param kwargs:
        :return:
        """
        headers = {'Accept': 'application/vnd.github+json'}
        return self.get("/user/keys", headers=headers, **kwargs)

    def create_ssh_for_current_user(self, **kwargs):
        """
        https://docs.github.com/en/rest/users/keys#create-a-public-ssh-key-for-the-authenticated-user
        :param kwargs:
        :return:
        """
        headers = {'Accept': 'application/vnd.github+json'}
        return self.post("/user/keys", headers=headers, **kwargs)

    def get_a_ssh_for_current_user(self, key_id, **kwargs):
        """
        https://docs.github.com/en/rest/users/keys#get-a-public-ssh-key-for-the-authenticated-user
        :param key_id: SSH key id
        :param kwargs:
        :return:
        """
        headers = {'Accept': 'application/vnd.github+json'}
        return self.get("/user/keys/{}".format(key_id), headers=headers, **kwargs)

    def delete_a_ssh_for_current_user(self, key_id, **kwargs):
        """
        https://docs.github.com/en/rest/users/keys#delete-a-public-ssh-key-for-the-authenticated-user
        :param key_id: SSH key id
        :param kwargs:
        :return:
        """
        headers = {'Accept': 'application/vnd.github+json'}
        return self.delete("/user/keys/{}".format(key_id), headers=headers, **kwargs)
