import json
import requests
import unittest
import random

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
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER}
        self.host = host
        self.command_signup = 'auth/signup'

        self.url_signup = 'http://{}/{}'.format(self.host, self.command_signup)
        words = ["python", "jumble", "easy", "difficult", "answer", "xylophone"]

        newValue = random.choice(words)
        email_value = time.strftime("%d%m%Y" + "%H%M%S") + "@" + "test.com"
        self.host = host
        self.command_user_create = 'management/users/create'

        self.url_user_create = 'http://{}/{}'.format(self.host, self.command_user_create)
        words = ["python", "jumble", "easy", "difficult", "answer", "xylophone"]
        newvalue = random.choice(words) + random.choice(words)
        nameunique = "testuser" + random.choice(words) + random.choice(words) + "@" + random.choice(words) + ".com"
        userdata = json.dumps(
            {"full_name": email_value, "email": email_value, "password": "12345678", "password_confirmation": "12345678",
             "birthday": "1990-06-12"})

        response2 = s.post(self.url_user_create, data=userdata, headers=headers)

        cont = response2.content
        res = response2.headers
        print res
        lost = res['Authorization']
        identificator  = cont['id']

        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': lost}

        response2 = s.get(self.url_profile_view, headers=headers)
        print response2
        self.assertEqual(response2.status_code, SUCCESS)

        self.host = host
        self.command_user_delete = 'management/users/delete'
        self.url_user_delete = 'http://{}/{}/{}'.format(self.host, self.command_user_delete, identificator)
        response2 = s.delete(self.url_user_delete, headers=headers)
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
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER}
        self.host = host
        self.command_signup = 'auth/signup'

        self.url_signup = 'http://{}/{}'.format(self.host, self.command_signup)
        words = ["python", "jumble", "easy", "difficult", "answer", "xylophone"]

        newValue = random.choice(words)
        email_value = time.strftime("%d%m%Y" + "%H%M%S") + "@" + "test.com"
        print email_value
        userdata = json.dumps({"email": email_value, "full_name": "FullName"})
        response2 = s.post(self.url_signup, data=userdata, headers=headers)

        res = response2.headers
        lost = res['Authorization']
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': lost}
        userdata = json.dumps({"name": "TestVtuier"})

        response2 = s.patch(self.url_profile_edit, data=userdata, headers=headers)

        self.assertEqual(response2.status_code, SUCCESS)


if __name__ == '__main__':
    unittest.main()
