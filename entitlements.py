import json


import requests
import unittest

import time

from test import host, DEFAULT_HEADER, SUCCESS, BADDATA
import random

class Test_004_ServerRoles(unittest.TestCase):

    def __init__(self, *a, **kw):
        super(Test_004_ServerRoles, self).__init__(*a, **kw)
        self.host = host
        self.command_roles = 'roles'

        self.url_all_roles = 'http://{}/{}'.format(self.host, self.command_roles)


    def test_01_all_roles_showed_successfully(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER}
        response2 = s.get(self.url_all_roles, headers=headers)
        self.assertEqual(response2.status_code, SUCCESS)

class Test_004_ServerActions(unittest.TestCase):
    def __init__(self, *a, **kw):
        super(Test_004_ServerActions, self).__init__(*a, **kw)
        self.host = host
        self.command_actions = 'actions'

        self.url_all_actions = 'http://{}/{}'.format(self.host, self.command_actions)

    def test_01_all_actions_showed_successfully(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER}
        response2 = s.get(self.url_all_actions, headers=headers)
        self.assertEqual(response2.status_code, SUCCESS)

class Test_004_ServerRolesCreate(unittest.TestCase):
    def __init__(self, *a, **kw):
        super(Test_004_ServerRolesCreate, self).__init__(*a, **kw)
        self.host = host
        self.command_roles_create = 'roles/create'

        self.url_roles_create = 'http://{}/{}'.format(self.host, self.command_roles_create)

    def test_01_roles_create_successfully(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        words = ["python", "jumble", "easy", "difficult", "answer", "xylophone"]
        newValue= random.choice(words)+random.choice(words)


        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER}
        userdata = json.dumps({"name": newValue})
        response2 = s.post(self.url_roles_create, data=userdata, headers=headers)
        self.assertEqual(response2.status_code, SUCCESS)
        self.host = host
        self.command_roles = 'roles'

        self.url_roles = 'http://{}/{}'.format(self.host, self.command_roles)
        roles = s.get(self.url_roles, headers=headers)
        m = json.loads(roles.content)

        print m
        print m['data'][7]
        index = int(m['data'][7]['id'])
        print index
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER}
        self.host = host
        self.command_roles_delete = 'roles/delete'

        self.url_roles_delete = 'http://{}/{}/{}'.format(self.host, self.command_roles_delete, index)
        response3 = s.delete(self.url_roles_delete, headers=headers)
        self.assertEqual(response3.status_code, SUCCESS)

class Test_004_ServerShowRole(unittest.TestCase):
    def __init__(self, *a, **kw):
        super(Test_004_ServerShowRole, self).__init__(*a, **kw)
        self.host = host
        self.command_role_show = 'roles/show'

        self.url_role_show = 'http://{}/{}'.format(self.host, self.command_role_show)

    def test_01_roles_show_successfully(self):
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER}
        s = requests.Session()
        self.host = host
        self.command_roles = 'roles'

        self.url_roles = 'http://{}/{}'.format(self.host, self.command_roles)
        roles = s.get(self.url_roles, headers=headers)
        m = json.loads(roles.content)

        index = int(m['data'][7]['id'])
        print index
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER}
        self.host = host
        self.command_roles_show = 'roles/show'

        self.url_roles_show = 'http://{}/{}/{}'.format(self.host, self.command_roles_show, index)
        response3 = s.get(self.url_roles_show, headers=headers)
        self.assertEqual(response3.status_code, SUCCESS)

class Test_004_ServerUpdateRole(unittest.TestCase):
    def __init__(self, *a, **kw):
        super(Test_004_ServerUpdateRole, self).__init__(*a, **kw)
        self.host = host
        self.command_roles_update = 'roles/update'


    def test_01_roles_show_successfully(self):
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER}
        s = requests.Session()
        self.host = host
        self.command_roles = 'roles'

        self.url_roles = 'http://{}/{}'.format(self.host, self.command_roles)
        roles = s.get(self.url_roles, headers=headers)
        m = json.loads(roles.content)

        index = int(m['data'][7]['id'])
        print index
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER}
        userdata = json.dumps({"name": "changedValue"})
        self.host = host
        self.command_roles_update = 'roles/update'

        self.url_roles_update = 'http://{}/{}/{}'.format(self.host, self.command_roles_update, index)

        response3 = s.patch(self.url_roles_update, data=userdata, headers=headers)
        self.assertEqual(response3.status_code, SUCCESS)


