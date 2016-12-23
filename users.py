import json

import now as now
import requests
import unittest
import random
import time
from authorization import test_authorization


email_value = time.strftime("%d%m%Y"+"%H%M%S")+"@"+"test.com"

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

class Test_004_user_Creation(unittest.TestCase):
    def __init__(self, *a, **kw):
        super(Test_004_user_Creation, self).__init__(*a, **kw)

    def test_01_user_created_correctly(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        time.sleep(3)
        token, index = test_authorization()
        time.sleep(3)
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': token}
        self.host = host
        self.command_user_create = 'management/users/create'

        self.url_user_create = 'http://{}/{}'.format(self.host, self.command_user_create)
        words = ["python", "jumble", "easy", "difficult", "answer", "xylophone"]
        newvalue = random.choice(words) + random.choice(words)
        nameunique = "testuser" + random.choice(words)+ random.choice(words) + "@" + random.choice(words) + ".com"
        userdata = json.dumps({"full_name": newvalue, "email": email_value, "password": "12345678", "password_confirmation": "12345678", "birthday": "1990-20-06"})

        response2 = s.post(self.url_user_create, data=userdata, headers=headers)

        print response2.content
        res = json.loads(response2.content)

        self.host = host
        self.command_user_delete = 'management/users/delete'
        self.url_user_delete = 'http://{}/{}/{}'.format(self.host, self.command_user_delete, index)
        response2 = s.delete(self.url_user_delete, headers=headers)

        self.assertEqual(response2.status_code, SUCCESS)




    def test_02_user_not_created_empty_values(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        time.sleep(3)
        token, index = test_authorization()
        time.sleep(3)
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': token}
        self.host = host
        self.command_user_create = 'management/users/create'

        self.url_user_create = 'http://{}/{}'.format(self.host, self.command_user_create)
        words = ["python", "jumble", "easy", "difficult", "answer", "xylophone"]
        newvalue = random.choice(words) + random.choice(words)
        nameunique = "testuser" + random.choice(words)+ random.choice(words) + "@" + random.choice(words) + ".com"
        userdata = json.dumps({"full_name": "", "email": "", "password": "", "password_confirmation": "", "birthday": ""})

        response2 = s.post(self.url_user_create, data=userdata, headers=headers)

        self.assertEqual(response2.status_code, BADDATA)

    def test_03_user_not_created_wrong_email_format(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        time.sleep(3)
        token, index = test_authorization()
        time.sleep(3)
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': token}
        self.host = host
        self.command_user_create = 'management/users/create'

        self.url_user_create = 'http://{}/{}'.format(self.host, self.command_user_create)
        words = ["python", "jumble", "easy", "difficult", "answer", "xylophone"]
        newvalue = random.choice(words) + random.choice(words)
        nameunique = "testuser" + random.choice(words)+ random.choice(words) + "@" + random.choice(words) + ".com"
        userdata = json.dumps({"full_name": newvalue, "email": "test", "password": "12345678", "password_confirmation": "12345678", "birthday": "1990-20-06"})

        response2 = s.post(self.url_user_create, data=userdata, headers=headers)



        self.assertEqual(response2.status_code, BADDATA)

class Test_004_All_users(unittest.TestCase):


    def __init__(self, *a, **kw):
        super(Test_004_All_users, self).__init__(*a, **kw)
        self.host = host
        self.command_all_users = 'management/users'

        self.url_all_users = 'http://{}/{}'.format(self.host, self.command_all_users)


    def test_01_all_users_opened(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        time.sleep(3)
        token, index = test_authorization()
        time.sleep(3)
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': token}
        response2 = s.get(self.url_all_users, headers=headers)
        print response2.content
        self.assertEqual(response2.status_code, SUCCESS)

class Test_004_user_Show(unittest.TestCase):

    def __init__(self, *a, **kw):
        super(Test_004_user_Show, self).__init__(*a, **kw)



    def test_01_user_page_showed_correctly(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        time.sleep(3)
        token, index = test_authorization()
        time.sleep(3)
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': token}
        self.host = host
        self.command_all_users = 'management/users'

        self.url_all_users = 'http://{}/{}'.format(self.host, self.command_all_users)
        users = s.get(self.url_all_users, headers=headers)

        self.command_user_show = 'management/users/show'

        self.url_user_show = 'http://{}/{}/{}'.format(self.host, self.command_user_show, index)
        response2 = s.get(self.url_user_show, headers=headers)
        print response2
        self.assertEqual(response2.status_code, SUCCESS)


class Test_004_user_Deleting(unittest.TestCase):
    def __init__(self, *a, **kw):
        super(Test_004_user_Deleting, self).__init__(*a, **kw)

    def authorize_with_id(self):
        self.command_signup = 'auth/signup'

        self.url_signup = 'http://{}/{}'.format(host, self.command_signup)
        s = requests.Session()
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER}

        email_value = time.strftime("%d%m%Y" + "%H%M%S") + "@" + "test.com"

        userdata = json.dumps({"email": email_value, "full_name": "FullName"})
        response2 = s.post(self.url_signup, data=userdata, headers=headers)
        res = response2.headers
        auth_token = res['Authorization']
        index = json.loads(response2.content)
        print index
        return (auth_token, index)

    def test_01_user_deleted_correctly(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        token, index = test_authorization()
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': token}


        print index

        self.host = host
        self.command_user_update = 'management/users/update'
        self.url_user_update = 'http://{}/{}/{}'.format(self.host, self.command_user_update, index)
        words = ["python", "jumble", "easy", "difficult", "answer", "xylophone"]

        newvalue = random.choice(words) + random.choice(words)

        userdata = json.dumps({"full_name": newvalue, "birthday": "1990-05-30"})
        response2 = s.patch(self.url_user_update, data=userdata, headers=headers)


        self.host = host
        self.command_user_delete = 'management/users/delete'


        self.url_user_delete = 'http://{}/{}/{}'.format(self.host, self.command_user_delete, index)
        response2 = s.delete(self.url_user_delete, headers=headers)
        print response2
        self.assertEqual(response2.status_code, SUCCESS)

if __name__ == '__main__':
    unittest.main()
