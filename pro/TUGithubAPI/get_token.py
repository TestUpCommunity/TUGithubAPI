import requests,json

url="https://github.com/login"
headers={'Content-Type':'application/json;charset=UTF-8'}
request_param={
    "username":"cassie01",
    "password":"xd19941225"
}
response=requests.post(url,data=json.dumps(request_param), headers=headers)
print(response.text)
print(response.json()['data']['token'])


import requests
def login():
    url = "http://test.xxxxxxx.com/api/common/login/login"
    data = {
        "username": "cassie01",
        "password": "xd19941225"
    }
    h = {
        "User-Agent": "Android/H60-L01/8.1.0/"

    }
    res = requests.post(url, data=data, headers=h)
    print(res.json())
 login()