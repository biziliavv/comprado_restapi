import json
import requests
import unittest
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
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, }
        userdata = json.dumps({"email": "tester.vitalii@gmail.com"})
        response2 = s.post(self.url_signin, data=userdata, headers=headers)
        self.assertEqual(response2.status_code, SUCCESS)

if __name__ == '__main__':
    unittest.main()
