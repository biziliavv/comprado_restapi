import json
import requests
import unittest
from test import host, DEFAULT_HEADER, SUCCESS


class Test_004_ServerRegistration(unittest.TestCase):

    def __init__(self, *a, **kw):
        super(Test_004_ServerRegistration, self).__init__(*a, **kw)
        self.host = host
        self.command_signup = 'auth/signup'

        self.url_signup = 'http://{}/{}'.format(self.host, self.command_signup)


    def test_01_register_successfully(self):
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
        userdata = json.dumps({"full_name": "vvfdveve", "email": "vfvv@etst.com", "password": "123456", "have_car": "true"})
        response2 = s.post(self.url_signup, data=userdata, headers=headers)
        self.assertEqual(response2.status_code, SUCCESS)
