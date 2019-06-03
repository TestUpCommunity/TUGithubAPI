import requests
import json as json_parser


class RestClient():
    def __init__(self, api_root_url, username=None, password=None, token=None):
        self.api_root_url = api_root_url
        self.session = requests.session()
        if username and password:
            self.session.auth = (username, password)
        elif token:
            self.session.headers["Authorization"] = "token {}".format(token)

    def get(self, url, **kwargs):
        return self.request(url, "get", **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        return self.request(url, "post", data, json, **kwargs)

    def options(self, url, **kwargs):
        return self.request(url, "potions", **kwargs)

    def head(self, url, **kwargs):
        return self.request(url, "head", **kwargs)

    def put(self, url, data=None, **kwargs):
        return self.request(url, "put", data, **kwargs)

    def patch(self, url, data=None, **kwargs):
        return self.request(url, "patch", data, **kwargs)

    def delete(self, url, **kwargs):
        return self.request(url, "delete", **kwargs)

    def request(self, url, method_name, data=None, json=None, **kwargs):
        url = self.api_root_url + url
        if method_name == "get":
            return self.session.get(url, **kwargs)
        if method_name == "post":
            return self.session.post(url, data, json, **kwargs)
        if method_name == "options":
            return self.session.options(url, **kwargs)
        if method_name == "head":
            return self.session.head(url, **kwargs)
        if method_name == "put":
            return self.session.put(url, data, **kwargs)
        if method_name == "patch":
            if json:
                data = json_parser.dumps(json)
            return self.session.patch(url, data, **kwargs)
        if method_name == "delete":
            return self.session.delete(url, **kwargs)

