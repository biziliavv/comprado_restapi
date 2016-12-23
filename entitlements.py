import json


import requests
import unittest

import time


import random

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

TAN = 9999
FIRSTNAME = "Oleg"
LASTNAME = time.strftime("%d/%m/%Y"+"%H:%M:%S")+"@"+"test.com"
EMAIL = 'biziliavv@gmail.com'
PSW = "123456"
host = '54.93.81.169/api/v1'

class Test_004_ServerRoles(unittest.TestCase):

    def __init__(self, *a, **kw):
        super(Test_004_ServerRoles, self).__init__(*a, **kw)
        self.host = host
        self.command_roles = 'management/roles'

        self.url_all_roles = 'http://{}/{}'.format(self.host, self.command_roles)


    def test_01_all_roles_showed_successfully(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        time.sleep(3)
        token, index = test_authorization()
        time.sleep(3)
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': token}
        time.sleep(3)
        response2 = s.get(self.url_all_roles, headers=headers)
        self.assertEqual(response2.status_code, SUCCESS)


    def test_01_all_roles_showed_unsuccessfully(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        time.sleep(3)
        token, index = test_authorization()
        time.sleep(3)
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': token}
        response2 = s.get(self.url_all_roles, headers=headers)
        self.assertEqual(response2.status_code, SUCCESS)

class Test_004_ServerActions(unittest.TestCase):
    def __init__(self, *a, **kw):
        super(Test_004_ServerActions, self).__init__(*a, **kw)
        self.host = host
        self.command_actions = 'management/actions'

        self.url_all_actions = 'http://{}/{}'.format(self.host, self.command_actions)

    def test_01_all_actions_showed_successfully(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        time.sleep(3)
        token, index  = test_authorization()
        time.sleep(3)
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': token}
        response2 = s.get(self.url_all_actions, headers=headers)
        self.assertEqual(response2.status_code, SUCCESS)

class Test_004_ServerRolesCreate(unittest.TestCase):
    def __init__(self, *a, **kw):
        super(Test_004_ServerRolesCreate, self).__init__(*a, **kw)
        self.host = host
        self.command_roles_create = 'management/roles/create'

        self.url_roles_create = 'http://{}/{}'.format(self.host, self.command_roles_create)

    def test_01_roles_create_successfully(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        words = ["python", "jumble", "easy", "difficult", "answer", "xylophone"]
        newValue= random.choice(words)+random.choice(words)

        time.sleep(3)
        token, index = test_authorization()
        time.sleep(3)
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': token}
        userdata = json.dumps({"name": newValue})
        response2 = s.post(self.url_roles_create, data=userdata, headers=headers)
        res = json.loads(response2.content)
        index = res['id']
        self.assertEqual(response2.status_code, SUCCESS)
        self.host = host
        self.command_roles = 'management/roles'

        self.url_roles = 'http://{}/{}'.format(self.host, self.command_roles)
        roles = s.get(self.url_roles, headers=headers)


        print index

        self.host = host
        self.command_roles_delete = 'management/roles/delete'

        self.url_roles_delete = 'http://{}/{}/{}'.format(self.host, self.command_roles_delete, index)
        response3 = s.delete(self.url_roles_delete, headers=headers)
        self.assertEqual(response3.status_code, SUCCESS)

class Test_004_ServerShowRole(unittest.TestCase):
    def __init__(self, *a, **kw):
        super(Test_004_ServerShowRole, self).__init__(*a, **kw)
        self.host = host
        self.command_role_show = 'management/roles/show'

        self.url_role_show = 'http://{}/{}'.format(self.host, self.command_role_show)

    def test_01_roles_show_successfully(self):
        time.sleep(3)
        token, index = test_authorization()
        time.sleep(3)
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': token}
        s = requests.Session()
        self.host = host
        self.command_roles = 'roles'

        self.url_roles = 'http://{}/{}'.format(self.host, self.command_roles)
        roles = s.get(self.url_roles, headers=headers)
        m = json.loads(roles.content)

        index = 5
        print index

        self.host = host
        self.command_roles_show = 'management/roles/show'

        self.url_roles_show = 'http://{}/{}/{}'.format(self.host, self.command_roles_show, index)
        response3 = s.get(self.url_roles_show, headers=headers)
        self.assertEqual(response3.status_code, SUCCESS)

class Test_004_ServerUpdateRole(unittest.TestCase):
    def __init__(self, *a, **kw):
        super(Test_004_ServerUpdateRole, self).__init__(*a, **kw)
        self.host = host
        self.command_roles_update = 'management/roles/update'


    def test_01_roles_show_successfully(self):
        time.sleep(3)
        token, index = test_authorization()
        time.sleep(3)

        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': token}
        s = requests.Session()
        self.host = host
        self.command_roles = 'management/roles'

        self.url_roles = 'http://{}/{}'.format(self.host, self.command_roles)
        roles = s.get(self.url_roles, headers=headers)
        m = json.loads(roles.content)

        index = int(m['data'][2]['id'])
        print index
        words = ["python", "jumble", "easy", "difficult", "answer", "xylophone"]
        newValue = random.choice(words) + random.choice(words)

        time.sleep(3)
        token, index = test_authorization()
        time.sleep(3)
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': token}
        userdata = json.dumps({"name": newValue})
        self.host = host
        self.command_roles_create = 'management/roles/create'

        self.url_roles_create = 'http://{}/{}'.format(self.host, self.command_roles_create)

        response2 = s.post(self.url_roles_create, data=userdata, headers=headers)
        res = json.loads(response2.content)
        index = res['id']
        self.assertEqual(response2.status_code, SUCCESS)

        words = ["python", "jumble", "easy", "difficult", "answer", "xylophone"]

        newValue = random.choice(words)+ random.choice(words)
        userdata = json.dumps({"name": newValue})
        self.host = host
        self.command_roles_update = 'management/roles/update'

        self.url_roles_update = 'http://{}/{}/{}'.format(self.host, self.command_roles_update, index)

        response3 = s.patch(self.url_roles_update, data=userdata, headers=headers)
        self.assertEqual(response3.status_code, SUCCESS)

if __name__ == '__main__':
    unittest.main()


