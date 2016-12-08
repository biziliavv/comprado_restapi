import json
import requests
import unittest
from test import host, DEFAULT_HEADER, SUCCESS, BADDATA


class Test_004_ServerRegister(unittest.TestCase):

    def __init__(self, *a, **kw):
        super(Test_004_ServerRegister, self).__init__(*a, **kw)
        self.host = host
        self.command_signup = 'auth/signup'

        self.url_signup = 'http://{}/{}'.format(self.host, self.command_signup)


    def test_01_register_successfully(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER}
        userdata = json.dumps({"email": "tester@test.com", "full_name": "FullName"})
        response2 = s.post(self.url_signup, data=userdata, headers=headers)
        self.assertEqual(response2.status_code, SUCCESS)

    def test_01_register_inc(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER}
        userdata = json.dumps({"email": "tester@test.com", "full_name": "Full Name"})
        response2 = s.post(self.url_signup, data=userdata, headers=headers)
        self.assertEqual(response2.status_code, BADDATA)