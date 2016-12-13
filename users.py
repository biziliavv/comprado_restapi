import json

import now as now
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
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER}
        self.host = host
        self.command_user_create = 'users/create'

        self.url_user_create = 'http://{}/{}'.format(self.host, self.command_user_create)
        words = ["python", "jumble", "easy", "difficult", "answer", "xylophone"]
        newvalue = random.choice(words) + random.choice(words)
        nameunique = "testuser" + random.choice(words)+ random.choice(words) + "@" + random.choice(words) + ".com"
        userdata = json.dumps({"full_name": newvalue, "email": nameunique, "password": "12345678", "password_confirmation": "12345678"})

        response2 = s.post(self.url_user_create, data=userdata, headers=headers)

        self.assertEqual(response2.status_code, SUCCESS)

class Test_004_All_users(unittest.TestCase):

    def __init__(self, *a, **kw):
        super(Test_004_All_users, self).__init__(*a, **kw)
        self.host = host
        self.command_all_users = 'users'

        self.url_all_users = 'http://{}/{}'.format(self.host, self.command_all_users)


    def test_01_all_users_opened(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER}
        response2 = s.get(self.url_all_users, headers=headers)
        print response2
        self.assertEqual(response2.status_code, SUCCESS)

class Test_004_user_Show(unittest.TestCase):

    def __init__(self, *a, **kw):
        super(Test_004_user_Show, self).__init__(*a, **kw)



    def test_01_user_page_showed_correctly(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER}
        self.host = host
        self.command_all_users = 'users'

        self.url_all_users = 'http://{}/{}'.format(self.host, self.command_all_users)
        users = s.get(self.url_all_users, headers=headers)
        m = json.loads(users.content)

        print m
        print m['data'][1]
        index = int(m['data'][1]['id'])
        print index
        self.host = host
        self.command_user_show = 'users/show'

        self.url_user_show = 'http://{}/{}/{}'.format(self.host, self.command_user_show, index)
        response2 = s.get(self.url_user_show, headers=headers)
        print response2
        self.assertEqual(response2.status_code, SUCCESS)




class Test_004_user_Deleting(unittest.TestCase):
        def __init__(self, *a, **kw):
                super(Test_004_user_Deleting, self).__init__(*a, **kw)

        def test_01_user_deleted_correctly(self):
            with open('USER_DATA.json') as data_file:
                data = json.load(data_file)
            s = requests.Session()
            headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER}
            self.host = host
            self.command_all_users = 'users'

            self.url_all_users = 'http://{}/{}'.format(self.host, self.command_all_users)
            users = s.get(self.url_all_users, headers=headers)
            m = json.loads(users.content)

            print m
            print m['data'][1]
            index = int(m['data'][1]['id'])
            print index

#            self.host = host
#            self.command_user_update = 'users/update'
#            self.url_user_update = 'http://{}/{}/{}'.format(self.host, self.command_user_update, index)
#            words = ["python", "jumble", "easy", "difficult", "answer", "xylophone"]
#            newvalue = random.choice(words) + random.choice(words)
#            nameunique = "testuser" + random.choice(words) + "@" + "test.com"
#            userdata = json.dumps({"full_name": newvalue, "email": nameunique})
#            response2 = s.patch(self.url_user_update, data=userdata, headers=headers)
#            print response2
#            self.assertEqual(response2.status_code, SUCCESS)

            self.host = host
            self.command_user_delete = 'users/delete'
            self.url_user_delete = 'http://{}/{}/{}'.format(self.host, self.command_user_delete, index)
            response2 = s.delete(self.url_user_delete, headers=headers)
            print response2
            self.assertEqual(response2.status_code, SUCCESS)

if __name__ == '__main__':
    unittest.main()