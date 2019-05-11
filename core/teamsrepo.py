import requests, json

class Teamsrepo():
    def __init__(self, api_root_url, username=None, password=None, token=None):
        self.api_root_url = api_root_url
        self.session = requests.session()
        if username and password and token != None:
            self.session.auth = (username, password)
        elif username and password:
            self.session.auth = (username, password)
        else:
            self.session.headers['Authorization'] = 'token %s' %(token)

    def get(self, url, **kwargs):
        return self.request(url, 'get', **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        return self.request(url, 'post', data, json, **kwargs)

    def patch(self, url, data=None, **kwargs):
        return self.request(url, 'patch', data, **kwargs)

    def delete(self, url, **kwargs):
        return self.request(url, 'delete', **kwargs)

    def put(self, url, data=None, **kwargs):
        return self.request(url, data, **kwargs)

    def request(self, url, name, data=None, json=None, **kwargs):
        url = self.api_root_url + url
        if name == 'get':
            return self.session.get(url, **kwargs)
        if name == 'post':
            return self.session.post(url, data, json, **kwargs)
        if name == 'patch':
            return self.session.patch(url, data, **kwargs)
        if name == 'delete':
            return self.session.delete(url, **kwargs)
        if name == 'put':
            return self.request(url, data, **kwargs)

if __name__== '__main__':
    r = Teamsrepo('http://httpbin.org')
    x = r.post('/post', json={'a':'b'})
    print(x.text)