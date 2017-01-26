import json
import requests
import unittest
import random

import time

from authorization import test_authorization

DEFAULT_HEADER = 'application/json'

SUCCESS = 200
BADREQUEST = 400
ADDED = 201
UNAUTHORIZED = 401
UPGRADE_REQUIRED = 426
FORBIDDEN = 403
NOTFOUND = 404
BADDATA = 422
MAIL_SENT = 202


TAN = 9999
FIRSTNAME = "Oleg"

EMAIL = 'biziliavv@gmail.com'
PSW = "123456"
host = '54.93.81.169/api/v1'


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
        words = ["python", "jumble", "easy", "difficult", "answer", "xylophone"]

        newValue = random.choice(words)
        email_value = time.strftime("%d%m%Y" + "%H%M%S") + "@" + "test.com"
        userdata = json.dumps({"email": email_value, "full_name": "FullName"})
        response2 = s.post(self.url_signup, data=userdata, headers=headers)
        self.assertEqual(response2.status_code, SUCCESS)

    def test_02_register_empty_values(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER}
        userdata = json.dumps({"email": "", "full_name": ""})
        response2 = s.post(self.url_signup, data=userdata, headers=headers)
        self.assertEqual(response2.status_code, BADDATA)

    def test_03_register_wrong_email_format(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER}
        userdata = json.dumps({"email": "test", "full_name": "test"})
        response2 = s.post(self.url_signup, data=userdata, headers=headers)
        self.assertEqual(response2.status_code, BADDATA)

    def test_04_register_already_registered_email(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER}
        userdata = json.dumps({"email": "testing2301@mailinator.com", "full_name": "test"})
        response2 = s.post(self.url_signup, data=userdata, headers=headers)
        self.assertEqual(response2.status_code, BADDATA)

class Test_004_ServerLogin(unittest.TestCase):



    def __init__(self, *a, **kw):
        super(Test_004_ServerLogin, self).__init__(*a, **kw)
        self.host = host
        self.command_signin = 'auth/signin'

        self.url_signin = 'http://{}/{}'.format(self.host, self.command_signin)


    def test_01_signed_in_successfully(self):
        # with open('USER_DATA.json') as data_file:
        #     data = json.load(data_file)
        #     for line in data:
        #         full_name= line["full_name"]
        #         email= line["email"]
        #         password = line["password"]
        #         have_car = line["have_car"]
        #         birthday = line["birthday"]

        s = requests.Session()
        email_value = time.strftime("%d%m%Y" + "%H%M%S") + "@" + "test.com"
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER}
        userdata = json.dumps({"email": "testing23011@mailinator.com", "password": "13021139"})
        response2 = s.post(self.url_signin, data=userdata, headers=headers)
        self.assertEqual(response2.status_code, SUCCESS)




class Test_004_ServerLoginByFacebook(unittest.TestCase):

    def __init__(self, *a, **kw):
        super(Test_004_ServerLoginByFacebook, self).__init__(*a, **kw)
        self.host = host
        self.command_signinbyfb = 'auth/signin/fb'

        self.url_signinbyfb = 'http://{}/{}'.format(self.host, self.command_signinbyfb)


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
        userdata = json.dumps({"access_token": "EAAJgkA7ZBGS0BAL6pZCJ2W53aRPnnMuL3cqmKzoFmKYG0ZCDGKUL1fhcOowhoJwLSoAZBseuAaaIfWRIVzVEf0XwIQI2SsDSzXXgCn7GiuMkX8LRajRSJy4wHSItmGgBRpPXbqkr3kweuExvxLdTCrZBKyxCv8XUZD"})
        response2 = s.post(self.url_signinbyfb, data=userdata, headers=headers)

        self.assertEqual(response2.status_code, SUCCESS)

class Test_Recovery_Password(unittest.TestCase):

    def __init__(self, *a, **kw):
        super(Test_Recovery_Password, self).__init__(*a, **kw)
        self.host = host
        self.command_recovery_password = 'auth/recovery'


        self.url_recovery_password = 'http://{}/{}'.format(self.host, self.command_recovery_password)


    def test_01_recovered_password_successfully(self):
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
        userdata = json.dumps({"email": "testing2301@mailinator.com"})
        response2 = s.post(self.url_recovery_password, data=userdata, headers=headers)
        res = response2.headers
        reset_token = res['reset_token']
        print reset_token

        self.assertEqual(response2.status_code, MAIL_SENT)
        self.command_reset_password = 'auth/reset'
        self.url_reset_password = 'http://{}/{}'.format(self.host, self.command_reset_password)
        userdata = json.dumps({"token": reset_token, "password": "string", "password_confirmation": "string"})
        response2 = s.post(self.url_reset_password, data=userdata, headers=headers)
        self.assertEqual(response2.status_code, SUCCESS)


class Test_Refresh_Token(unittest.TestCase):

    def __init__(self, *a, **kw):
        super(Test_Refresh_Token, self).__init__(*a, **kw)
        self.host = host
        self.command_refresh_token = 'auth/refresh'
        self.url_refresh_token = 'http://{}/{}'.format(self.host, self.command_refresh_token)

    def test_01_refreshed_token_successfully(self):
        s = requests.Session()
        token, index = test_authorization()
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': token}
        response2 = s.get(self.url_refresh_token, headers=headers)
        res = response2.headers
        newToken = res['Authorization']
        self.assertNotEqual(token, newToken)
        self.assertEqual(response2.status_code, MAIL_SENT)
if __name__ == '__main__':
    unittest.main()