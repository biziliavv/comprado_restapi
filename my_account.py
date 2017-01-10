import json
import requests
import unittest
import random
from authorization import test_authorization



import time

DEFAULT_HEADER = 'application/json'

SUCCESS = 200
BADREQUEST = 400
ADDED = 201
UNAUTHORIZED = 401
UPGRADE_REQUIRED = 426
FORBIDDEN = 403
NOTFOUND = 404
BADDATA = 422
EXPIRED_TOKEN = 419

TAN = 9999
FIRSTNAME = "Oleg"
email_value = time.strftime("%d%m%Y"+"%H%M%S")+"@"+"test.com"
EMAIL = 'biziliavv@gmail.com'
PSW = "123456"
host = '54.93.81.169/api/v1'






class Test_004_My_Profile_View(unittest.TestCase):

    def __init__(self, *a, **kw):
        super(Test_004_My_Profile_View, self).__init__(*a, **kw)
        self.host = host
        self.command_profile_view = 'me'

        self.url_profile_view = 'http://{}/{}'.format(self.host, self.command_profile_view)


    def test_01_user_profile_opened(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()



        time.sleep(5)
        token, index = test_authorization()
        time.sleep(5)
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': token}

        response2 = s.get(self.url_profile_view, headers=headers)
        print response2
        self.assertEqual(response2.status_code, SUCCESS)





    def test_02_user_profile_not_opened_because_empty_token(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()

        token = ""
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': token}

        response2 = s.get(self.url_profile_view, headers=headers)
        print response2
        self.assertEqual(response2.status_code, UNAUTHORIZED)

    def test_03_user_profile_not_opened_because_wrong_token(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        token = "dfgetgergergergerg"
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': token}

        response2 = s.get(self.url_profile_view, headers=headers)
        print response2
        self.assertEqual(response2.status_code, UNAUTHORIZED)

    def test_04_user_profile_not_opened_because_expired_token(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        token = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjE0MiwiaXNzIjoiaHR0cDpcL1wvNTQuOTMuODEuMTY5XC9hcGlcL3YxXC9hdXRoXC9zaWdudXAiLCJpYXQiOjE0ODM0NTQ0NzcsImV4cCI6MTQ4MzQ1ODA3NywibmJmIjoxNDgzNDU0NDc3LCJqdGkiOiJkZTAwMWQ5YmUxMGNhYjA1M2QzODE1YjhhNTMyNmYwMyJ9.Zrv6bt85tvKXvMLiB57poGbQvCJ7K1ghF0pjrG-EyfU"
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': token}

        response2 = s.get(self.url_profile_view, headers=headers)
        print response2
        self.assertEqual(response2.status_code, EXPIRED_TOKEN)



class Test_004_My_Profile_Edit(unittest.TestCase):

    def __init__(self, *a, **kw):
        super(Test_004_My_Profile_Edit, self).__init__(*a, **kw)
        self.host = host
        self.command_profile_edit = 'me/update'

        self.url_profile_edit = 'http://{}/{}'.format(self.host, self.command_profile_edit)


    def test_01_user_profile_edited(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        time.sleep(5)
        token, index = test_authorization()
        time.sleep(5)
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': token}
        userdata = json.dumps({"name": "TestVtuier"})

        response2 = s.patch(self.url_profile_edit, data=userdata, headers=headers)

        self.assertEqual(response2.status_code, SUCCESS)


if __name__ == '__main__':
    unittest.main()
