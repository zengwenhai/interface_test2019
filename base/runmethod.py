import requests
import json


class RunMethod(object):

    def get_main(self, url, params, header=None):
        res = None
        if header != None:
            res = requests.get(url=url, params=params, header=header)
        else:
            res = requests.get(url=url, params=params)
        return res

    def post_main(self, url, data, header=None):
        res = None
        if header != None:
            res = requests.post(url=url, data=data, header=header, verify=False)
        else:
            res = requests.post(url=url, data=data, verify=False)
        return res

    def run_main(self, method, url, params=None, data=None, header=None):
        res = None
        if method == 'post':
            res = self.post_main(url, data, header)
        else:
            res = self.get_main(url, params, header)
        # return json.dumps(res, ensure_ascii=False, sort_keys=False)
        return res


if __name__ == '__main__':
    method = 'post'
    url = 'http://127.0.0.1:5000/login'
    data = {'username': 'zengwenhai', 'password': 123456}
    r = RunMethod().run_main(url=url, data=data, method=method)
    print(r.text)