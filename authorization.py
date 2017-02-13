import unittest

import requests
import random
import json

import time

host = '54.93.81.169/api/v1'

DEFAULT_HEADER = 'application/json'
SUCCESS = 200
BADREQUEST = 400
ADDED = 201
UNAUTHORIZED = 401
UPGRADE_REQUIRED = 426
FORBIDDEN = 403
NOTFOUND = 404
BADDATA = 422


def test_authorization():

        command_signin = 'auth/signin'

        url_signin = 'http://{}/{}'.format(host, command_signin)
        s = requests.Session()
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER}


        email_value = time.strftime("%d%m%Y" + "%H%M%S") + "@" + "test.com"

        userdata = json.dumps({ "email": "tester.bizilia@gmail.com", "password": "NIHMjk53LalOz3Bj"})
        response2 = s.post(url_signin, data=userdata, headers=headers)
        res = response2.headers
        print res
        time.sleep(10)
        auth_token = res['Authorization']
        cont = json.loads(response2.content)
        index = cont['id']

        print auth_token
        return (auth_token, index)




if __name__ == '__main__':
    unittest.main()

