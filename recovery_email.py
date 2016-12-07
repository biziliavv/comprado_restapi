import json
import requests
import unittest
from test import host, DEFAULT_HEADER, SUCCESS


class Test_004_ServerRecoverEmail(unittest.TestCase):


    def _login(headers=DEFAULT_HEADER):
        s = requests.Session()
        url = 'http://{}/{}'.format(host, 'auth/signin')

        _headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER}
        _userdata = json.dumps({"email": "biziliavv@gmail.com", "password": "12345678"})
        response2 = s.post(url, data=_userdata, headers=_headers)
        return s, response2.status_code

    def __init__(self, *a, **kw):
        super(Test_004_ServerRecoverEmail, self).__init__(*a, **kw)
        self.host = host
        self.command_signin = 'auth/signin'
        self.command_recoveryemail = 'auth/recovery'
        self.url_signin = 'http://{}/{}'.format(self.host, self.command_signin)
        self.url_recoveryemail = 'http://{}/{}'.format(self.host, self.command_recoveryemail)


    def test_01_recovered_successfully(self):
        # with open('USER_DATA.json') as data_file:
        #     data = json.load(data_file)
        #     for line in data:
        #         full_name= line["full_name"]
        #         email= line["email"]
        #         password = line["password"]
        #         have_car = line["have_car"]
        #         birthday = line["birthday"]

        s = requests.Session()
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER}
        userdata = json.dumps({"email": "tester@test.com", "password": "123456"})
        response = s.post(self.url_signin, data=userdata, headers=headers)
        self.assertEqual(response.status_code, SUCCESS)

        userdata1 = json.dumps({"email": "tester@test.com"})
        response2 = s.post(self.url_recoveryemail, data=userdata1, headers=headers)
        self.assertEqual(response2.status_code, SUCCESS)
