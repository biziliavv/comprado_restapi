import json
import requests
import unittest
import random
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

        userdata = json.dumps({"email": "tester" + newValue + newValue + "@test.com", "full_name": "FullName"})
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
        userdata = json.dumps({"email": "a.storozhenko@live.com", "full_name": "test"})
        response2 = s.post(self.url_signup, data=userdata, headers=headers)
        self.assertEqual(response2.status_code, BADDATA)

if __name__ == '__main__':
    unittest.main()