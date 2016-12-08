import json
import requests
import unittest
from test import host, DEFAULT_HEADER, SUCCESS, BADDATA,  BADREQUEST, UNAUTHORIZED


class Test_004_ServerLogin(unittest.TestCase):



    def __init__(self, *a, **kw):
        super(Test_004_ServerLogin, self).__init__(*a, **kw)
        self.host = host
        self.command_signin = 'auth/signin'

        self.url_signin = 'http://{}/{}'.format(self.host, self.command_signin)


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
        userdata = json.dumps({"email": "biziliavv@gmail.com", "password": "12345678"})
        response2 = s.post(self.url_signin, data=userdata, headers=headers)
        self.assertEqual(response2.status_code, SUCCESS)

    def test_01_register_incorrect_email(self):
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
        userdata = json.dumps({"email": "focus@gmail.com", "password": "12345678"})
        response2 = s.post(self.url_signin, data=userdata, headers=headers)
        self.assertEqual(response2.status_code, UNAUTHORIZED)

    def test_01_register_incorrect_password(self):
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
        userdata = json.dumps({"email": "biziliavv@gmail.com", "password": "262621"})
        response2 = s.post(self.url_signin, data=userdata, headers=headers)
        self.assertEqual(response2.status_code, UNAUTHORIZED)

    def test_01_register_empty_fields(self):
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
        userdata = json.dumps({"email": "     ", "password": "     "})
        response2 = s.post(self.url_signin, data=userdata, headers=headers)
        self.assertEqual(response2.status_code, BADDATA)
