import json
import requests
import unittest

import time

from test import host, DEFAULT_HEADER, SUCCESS, BADDATA

EMAIL = time.strftime("%d%m%Y"+"%H%M%S")+"@"+"test.com"
class Test_004_ServerRegister(unittest.TestCase):

    def __init__(self, *a, **kw):
        super(Test_004_ServerRegister, self).__init__(*a, **kw)
        self.host = host
        self.command_createUser = 'users/create'

        self.url_createUser = 'http://{}/{}'.format(self.host, self.command_createUser)


    def test_01_user_created_successfully(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER}
        userdata = json.dumps({"email": EMAIL, "full_name": "FullName"})
        response2 = s.post(self.url_createUser, data=userdata, headers=headers)

        self.assertEqual(response2.status_code, SUCCESS)

