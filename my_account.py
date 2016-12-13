import json
import requests
import unittest

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

TAN = 9999
FIRSTNAME = "Oleg"
LASTNAME = time.strftime("%d/%m/%Y"+"%H:%M:%S")+"@"+"test.com"
EMAIL = 'biziliavv@gmail.com'
PSW = "123456"
host = '54.93.81.169/api/v1'
token = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjMsImlzcyI6Imh0dHA6XC9cLzU0LjkzLjgxLjE2OVwvYXBpXC92MVwvYXV0aFwvc2lnbmluXC9mYiIsImlhdCI6MTQ4MTYxNDA3NCwiZXhwIjoxNDgxNjE3Njc0LCJuYmYiOjE0ODE2MTQwNzQsImp0aSI6IjAxNTA2MzUyNzlhMzY4YzIyNjA2YTNkODA2MzI1MjYzIn0.-HpkRI0f4d467iepzIhy3-oE0zcuyoRgj0BZpdQPkak"
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
        self.assertEqual(response2.status_code, BADREQUEST)

    def test_03_user_profile_not_opened_because_wrong_token(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        token = "dfgetgergergergerg"
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': token}

        response2 = s.get(self.url_profile_view, headers=headers)
        print response2
        self.assertEqual(response2.status_code, BADREQUEST)


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

        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': token}
        userdata = json.dumps({"name": "TestVtuier"})

        response2 = s.patch(self.url_profile_edit, data=userdata, headers=headers)

        self.assertEqual(response2.status_code, SUCCESS)


if __name__ == '__main__':
    unittest.main()
