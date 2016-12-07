import json
import requests
import unittest
from test import host, DEFAULT_HEADER, SUCCESS


class Test_004_ServerResetPassword(unittest.TestCase):

    def __init__(self, *a, **kw):
        super(Test_004_ServerResetPassword, self).__init__(*a, **kw)
        self.host = host
        self.command_resetpassword = 'auth/reset'

        self.url_resetpassword = 'http://{}/{}'.format(self.host, self.command_resetpassword)


    def test_01_resetpassword_successfully(self):
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
        userdata = json.dumps({"email": "tester@test.com"})
        response2 = s.post(self.url_resetpassword, data=userdata, headers=headers)
        self.assertEqual(response2.status_code, SUCCESS)
