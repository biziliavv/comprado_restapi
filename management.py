import json
import requests
import unittest
import random
import string
from random import shuffle
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
WRONGID = 500
ACTION_IS_DONE = 204
DETACHED = 202


email_value = time.strftime("%d%m%Y" + "%H%M%S") + "@" + "test.com"
EMAIL = 'biziliavv@gmail.com'
PSW = "123456"
host = '54.93.81.169/api/v1'

class Test_004_business_Creation(unittest.TestCase):
    def __init__(self, *a, **kw):
        super(Test_004_business_Creation, self).__init__(*a, **kw)

    def test_01_business_created_correctly(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        time.sleep(5)
        token, index = test_authorization()
        time.sleep(5)
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': token}
        self.host = host
        self.command_business_create = 'management/businesses/create'

        self.url_business_create = 'http://{}/{}'.format(self.host, self.command_business_create)
        email_value = time.strftime("%d%m%Y" + "%H%M%S") + "@" + "test.com"
        userdata = json.dumps({"partner_id": 1, "email": email_value, "business_id_by_partner": "string", "address": "string", "geo_latitude": "48.92279", "geo_longitude": "22.4519749", "name": "string", "description": "string"})

        response2 = s.post(self.url_business_create, data=userdata, headers=headers)

        self.assertEqual(response2.status_code, SUCCESS)
    def test_01_business_not_created_because_empty_userdata(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER}
        self.host = host
        self.command_business_create = 'management/businesses/create'

        self.url_business_create = 'http://{}/{}'.format(self.host, self.command_business_create)
        userdata = json.dumps({})

        response2 = s.post(self.url_business_create, data=userdata, headers=headers)

        self.assertEqual(response2.status_code, UNAUTHORIZED)

class Test_004_business_Deleting(unittest.TestCase):
        def __init__(self, *a, **kw):
                super(Test_004_business_Deleting, self).__init__(*a, **kw)

        def test_01_business_deleted_correctly(self):
            with open('USER_DATA.json') as data_file:
                data = json.load(data_file)
            s = requests.Session()
            time.sleep(5)
            token, index = test_authorization()
            time.sleep(5)
            headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': token}
            self.host = host
            self.command_business_create = 'management/businesses/create'

            self.url_business_create = 'http://{}/{}'.format(self.host, self.command_business_create)
            email_value = time.strftime("%d%m%Y" + "%H%M%S") + "@" + "test.com"
            userdata = json.dumps({"partner_id": 1, "email": email_value, "business_id_by_partner": "string", "address": "string", "geo_latitude": "48.92279", "geo_longitude": "22.4519749", "name": "string", "description": "string"})

            response2 = s.post(self.url_business_create, data=userdata, headers=headers)
            cont = json.loads(response2.content)
            print cont
            identifier = cont['id']
            self.assertEqual(response2.status_code, SUCCESS)


            self.host = host
            self.command_business_update = 'management/businesses/update'
            self.url_business_update = 'http://{}/{}/{}'.format(self.host, self.command_business_update, identifier)
            userdata = json.dumps({"title": "newTitle"})
            response2 = s.patch(self.url_business_update, data=userdata, headers=headers)
            print response2
            self.assertEqual(response2.status_code, SUCCESS)

            self.host = host
            self.command_business_delete = 'management/businesses/delete'
            self.url_business_delete = 'http://{}/{}/{}'.format(self.host, self.command_business_delete, identifier)
            response2 = s.delete(self.url_business_delete, headers=headers)
            print response2
            self.assertEqual(response2.status_code, SUCCESS)

class Test_004_category_Creation(unittest.TestCase):
    def __init__(self, *a, **kw):
        super(Test_004_category_Creation, self).__init__(*a, **kw)

    def test_01_category_created_correctly(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        time.sleep(5)
        token, index = test_authorization()
        time.sleep(5)
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': token}
        self.host = host
        self.command_category_create = 'management/categories/create'


        self.url_category_create = 'http://{}/{}'.format(self.host, self.command_category_create)
        userdata = json.dumps({"parent_id": 3, "is_last": "false", "title": "string", "description": "string"})

        response2 = s.post(self.url_category_create, data=userdata, headers=headers)

        self.assertEqual(response2.status_code, SUCCESS)

class Test_004_category_Deleting(unittest.TestCase):
        def __init__(self, *a, **kw):
                super(Test_004_category_Deleting, self).__init__(*a, **kw)

        def test_01_category_deleted_correctly(self):
            with open('USER_DATA.json') as data_file:
                data = json.load(data_file)
            s = requests.Session()
            time.sleep(5)
            token, index = test_authorization()
            time.sleep(5)
            headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': token}
            self.host = host
            self.command_category_create = 'management/categories/create'

            self.url_category_create = 'http://{}/{}'.format(self.host, self.command_category_create)
            userdata = json.dumps({"parent_id": 2, "is_last": "false", "title": "string", "description": "string"})

            response2 = s.post(self.url_category_create, data=userdata, headers=headers)
            cont = json.loads(response2.content)
            identifier = cont['id']
            self.assertEqual(response2.status_code, SUCCESS)

            self.host = host
            self.command_category_update = 'management/categories/update'
            self.isocode = 'isocode1'
            self.isocode_value = 'en'
            self.url_category_update = 'http://{}/{}/{}?{}={}'.format(self.host, self.command_category_update, identifier, self.isocode, self.isocode_value)
            userdata = json.dumps({"title": "categoryTest"})
            response2 = s.patch(self.url_category_update, data=userdata, headers=headers)
            print response2
            self.assertEqual(response2.status_code, SUCCESS)

            self.host = host
            self.command_category_delete = 'management/categories/delete'

            self.url_category_delete = 'http://{}/{}/{}'.format(self.host, self.command_category_delete, identifier)
            response2 = s.delete(self.url_category_delete, headers=headers)
            print response2
            self.assertEqual(response2.status_code, SUCCESS)

        def test_01_not_deleted_because_of_alphabetical_id(self):
            with open('USER_DATA.json') as data_file:
                data = json.load(data_file)
            s = requests.Session()
            time.sleep(5)
            token, index = test_authorization()
            time.sleep(5)
            headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': token}


            self.host = host
            self.command_category_delete = 'management/categories/delete'
            index = 'b'
            self.url_category_delete = 'http://{}/{}/{}'.format(self.host, self.command_category_delete, index)
            response2 = s.delete(self.url_category_delete, headers=headers)
            print response2
            self.assertEqual(response2.status_code, WRONGID)

        def test_01_category_cant_be_deleted_because_id_doesnt_exist(self):
            with open('USER_DATA.json') as data_file:
                data = json.load(data_file)
            s = requests.Session()
            time.sleep(5)
            token, index = test_authorization()
            time.sleep(5)
            headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': token}


            self.host = host
            self.command_category_delete = 'management/categories/delete'
            index = 900
            self.url_category_delete = 'http://{}/{}/{}'.format(self.host, self.command_category_delete, index)
            response2 = s.delete(self.url_category_delete, headers=headers)
            print response2
            self.assertEqual(response2.status_code, BADDATA)

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
        newValue = random.choice(words)
        nameunique = "testuser" + time.strftime("%d%m%Y" + "%H%M%S") + "@" + random.choice(words) + ".com"
        print newValue
        email_value = time.strftime("%d%m%Y" + "%H%M%S") + "@" + "test.com"
        print email_value
        userdata = json.dumps({"full_name": newValue, "email": email_value, "password": "12345678", "password_confirmation": "12345678", "birthday": "1990-20-06", "gender": "male"})

        response2 = s.post(self.url_user_create, data=userdata, headers=headers)

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

        self.command_signup = 'auth/signup'

        self.url_signup = 'http://{}/{}'.format(host, self.command_signup)
        s = requests.Session()
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER}

        email_value = time.strftime("%d%m%Y" + "%H%M%S") + "@" + "test.com"

        userdata = json.dumps({"email": email_value, "full_name": "Test User"})
        response2 = s.post(self.url_signup, data=userdata, headers=headers)
        res = response2.headers
        print res
        auth_token = res['Authorization']
        cont = json.loads(response2.content)
        index = cont['id']
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': auth_token}


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
        words = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
        newValue = str(random.choice(words)) + str(random.choice(words)) + str(random.choice(words)) + str(random.choice(words))
        print newValue

        time.sleep(3)
        token, index = test_authorization()
        time.sleep(3)
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': token}
        userdata = json.dumps({"name": newValue})
        response2 = s.post(self.url_roles_create, data=userdata, headers=headers)
        res = json.loads(response2.content)
        print res
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
        words = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
        newValue = str(random.choice(words)) + str(random.choice(words)) + str(random.choice(words)) + str(
            random.choice(words))
        print newValue

        time.sleep(3)
        token, index = test_authorization()
        time.sleep(3)
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': token}
        userdata = json.dumps({"name": newValue})
        self.host = host
        self.command_roles_create = 'management/roles/create'

        self.url_roles_create = 'http://{}/{}'.format(self.host, self.command_roles_create)

        response2 = s.post(self.url_roles_create, data=userdata, headers=headers)
        print response2.content
        res = json.loads(response2.content)
        print res
        index = res['id']
        self.assertEqual(response2.status_code, SUCCESS)

        words = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
        newValue = str(random.choice(words)) + str(random.choice(words)) + str(random.choice(words)) + str(
            random.choice(words))
        print newValue
        userdata = json.dumps({"name": newValue})
        self.host = host
        self.command_roles_update = 'management/roles/update'

        self.url_roles_update = 'http://{}/{}/{}'.format(self.host, self.command_roles_update, index)

        response3 = s.patch(self.url_roles_update, data=userdata, headers=headers)
        self.assertEqual(response3.status_code, SUCCESS)

class Test_004_offer_Creation(unittest.TestCase):
    def __init__(self, *a, **kw):
        super(Test_004_offer_Creation, self).__init__(*a, **kw)

    def test_01_offer_created_correctly(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        time.sleep(3)
        token, index = test_authorization()
        time.sleep(3)
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': token}
        self.host = host

        self.command_category_create = 'management/categories/create'

        self.url_category_create = 'http://{}/{}'.format(self.host, self.command_category_create)
        userdata = json.dumps({"parent_id": 3, "is_last": "false", "title": "string", "description": "string"})

        response2 = s.post(self.url_category_create, data=userdata, headers=headers)
        self.assertEqual(response2.status_code, SUCCESS)
        res = json.loads(response2.content)
        identifier = res['id']

        self.command_business_create = 'management/businesses/create'

        self.url_business_create = 'http://{}/{}'.format(self.host, self.command_business_create)
        email_value = time.strftime("%d%m%Y" + "%H%M%S") + "@" + "test.com"
        userdata = json.dumps(
            {"partner_id": 1, "email": email_value, "business_id_by_partner": "string", "address": "string",
             "geo_latitude": "48.92279", "geo_longitude": "22.4519749", "name": "string", "description": "string"})

        response2 = s.post(self.url_business_create, data=userdata, headers=headers)
        self.assertEqual(response2.status_code, SUCCESS)
        res = json.loads(response2.content)
        index = res['id']

        self.command_offer_create = 'management/offers/create'

        self.url_offer_create = 'http://{}/{}'.format(self.host, self.command_offer_create)
        userdata = json.dumps({"title": "string1", "description": "string", "business_id": index, "main_category_id": identifier, "SKU": "string","offer_quantity": 0, "offer_id_by_partner": "string", "delivery_cost": 0, "vat": 0})

        response2 = s.post(self.url_offer_create, data=userdata, headers=headers)

        self.assertEqual(response2.status_code, SUCCESS)

class Test_004_offer_Approving(unittest.TestCase):
    def __init__(self, *a, **kw):
        super(Test_004_offer_Approving, self).__init__(*a, **kw)

    def test_01_offer_approved_correctly(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        time.sleep(3)
        token, index = test_authorization()
        time.sleep(3)
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': token}
        self.host = host

        self.command_offer_create = 'management/offers/create'
        self.command_offer_approve = 'management/offers/approve'
        self.command_offer_delete = 'management/offers/delete'

        self.command_category_create = 'management/categories/create'

        self.url_category_create = 'http://{}/{}'.format(self.host, self.command_category_create)
        userdata = json.dumps({"parent_id": 3, "is_last": "false", "title": "string", "description": "string"})

        response2 = s.post(self.url_category_create, data=userdata, headers=headers)
        self.assertEqual(response2.status_code, SUCCESS)
        res = json.loads(response2.content)
        identifier = res['id']

        self.command_business_create = 'management/businesses/create'

        self.url_business_create = 'http://{}/{}'.format(self.host, self.command_business_create)
        email_value = time.strftime("%d%m%Y" + "%H%M%S") + "@" + "test.com"
        userdata = json.dumps(
            {"partner_id": 1, "email": email_value, "business_id_by_partner": "string", "address": "string",
             "geo_latitude": "48.92279", "geo_longitude": "22.4519749", "name": "string", "description": "string"})

        response2 = s.post(self.url_business_create, data=userdata, headers=headers)
        self.assertEqual(response2.status_code, SUCCESS)
        res = json.loads(response2.content)
        index = res['id']

        self.command_offer_create = 'management/offers/create'

        self.url_offer_create = 'http://{}/{}'.format(self.host, self.command_offer_create)
        userdata = json.dumps(
            {"title": "string1", "description": "string", "business_id": index, "main_category_id": identifier,
             "SKU": "string", "offer_quantity": 0, "offer_id_by_partner": "string", "delivery_cost": 0, "vat": 0})
        response2 = s.post(self.url_offer_create, data=userdata, headers=headers)

        self.assertEqual(response2.status_code, SUCCESS)

        res = json.loads(response2.content)
        index = res['id']
        self.offer_ids = 'offer_ids'
        self.url_offer_approve = 'http://{}/{}?{}={}'.format(self.host, self.command_offer_approve, self.offer_ids, index)

        response2 = s.post(self.url_offer_approve, headers=headers)

        self.assertEqual(response2.status_code, SUCCESS)

        self.command_offer_delete = 'management/offers/delete'
        self.url_offer_delete = 'http://{}/{}/{}'.format(self.host, self.command_offer_delete, index)

        response2 = s.delete(self.url_offer_delete, headers=headers)
        print response2
        self.assertEqual(response2.status_code, SUCCESS)

class Test_004_offer_Disapproving(unittest.TestCase):
    def __init__(self, *a, **kw):
        super(Test_004_offer_Disapproving, self).__init__(*a, **kw)

    def test_01_offer_disapproved_correctly(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        time.sleep(3)
        token, index = test_authorization()
        time.sleep(3)
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': token}
        self.host = host
        self.command_offer_create = 'management/offers/create'
        self.command_offer_disapprove = 'management/offers/disapprove'
        self.command_offer_delete = 'management/offers/delete'

        self.url_offer_create = 'http://{}/{}'.format(self.host, self.command_offer_create)
        userdata = json.dumps({"title": "string1", "description": "string", "business_id": 115, "main_category_id": 97, "SKU": "string","offer_quantity": 0, "offer_id_by_partner": "string", "delivery_cost": 0, "vat": 0})

        response2 = s.post(self.url_offer_create, data=userdata, headers=headers)

        self.assertEqual(response2.status_code, SUCCESS)

        res = json.loads(response2.content)
        index = res['id']
        self.offer_ids = 'offer_ids'
        self.url_offer_disapprove = 'http://{}/{}?{}={}'.format(self.host, self.command_offer_disapprove, self.offer_ids, index)

        response2 = s.post(self.url_offer_disapprove, headers=headers)

        self.assertEqual(response2.status_code, SUCCESS)

        self.command_offer_delete = 'management/offers/delete'
        self.url_offer_delete = 'http://{}/{}/{}'.format(self.host, self.command_offer_delete, index)

        response2 = s.delete(self.url_offer_delete, headers=headers)
        print response2
        self.assertEqual(response2.status_code, SUCCESS)


class Test_004_offer_Publishing(unittest.TestCase):
    def __init__(self, *a, **kw):
        super(Test_004_offer_Publishing, self).__init__(*a, **kw)

    def test_01_offer_published_correctly(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        time.sleep(3)
        token, index = test_authorization()
        time.sleep(3)
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': token}
        self.host = host
        self.command_offer_create = 'management/offers/create'
        self.command_offer_publish = 'management/offers/publish'
        self.command_offer_delete = 'management/offers/delete'

        self.command_category_create = 'management/categories/create'

        self.url_category_create = 'http://{}/{}'.format(self.host, self.command_category_create)
        userdata = json.dumps({"parent_id": 3, "is_last": "false", "title": "string", "description": "string"})

        response2 = s.post(self.url_category_create, data=userdata, headers=headers)
        self.assertEqual(response2.status_code, SUCCESS)
        res = json.loads(response2.content)
        identifier = res['id']

        self.command_business_create = 'management/businesses/create'

        self.url_business_create = 'http://{}/{}'.format(self.host, self.command_business_create)
        email_value = time.strftime("%d%m%Y" + "%H%M%S") + "@" + "test.com"
        userdata = json.dumps(
            {"partner_id": 1, "email": email_value, "business_id_by_partner": "string", "address": "string",
             "geo_latitude": "48.92279", "geo_longitude": "22.4519749", "name": "string", "description": "string"})

        response2 = s.post(self.url_business_create, data=userdata, headers=headers)
        self.assertEqual(response2.status_code, SUCCESS)
        res = json.loads(response2.content)
        index = res['id']

        self.command_offer_create = 'management/offers/create'

        self.url_offer_create = 'http://{}/{}'.format(self.host, self.command_offer_create)
        userdata = json.dumps(
            {"title": "string1", "description": "string", "business_id": index, "main_category_id": identifier,
             "SKU": "string", "offer_quantity": 0, "offer_id_by_partner": "string", "delivery_cost": 0, "vat": 0})

        response2 = s.post(self.url_offer_create, data=userdata, headers=headers)

        self.assertEqual(response2.status_code, SUCCESS)

        res = json.loads(response2.content)
        index = res['id']
        self.offer_ids = 'offer_ids'
        self.url_offer_publish = 'http://{}/{}?{}={}'.format(self.host, self.command_offer_publish, self.offer_ids, index)

        response2 = s.post(self.url_offer_publish, headers=headers)

        self.assertEqual(response2.status_code, SUCCESS)

        self.command_offer_delete = 'management/offers/delete'
        self.url_offer_delete = 'http://{}/{}/{}'.format(self.host, self.command_offer_delete, index)

        response2 = s.delete(self.url_offer_delete, headers=headers)
        print response2
        self.assertEqual(response2.status_code, SUCCESS)


class Test_004_offer_Unpublishing(unittest.TestCase):
    def __init__(self, *a, **kw):
        super(Test_004_offer_Unpublishing, self).__init__(*a, **kw)

    def test_01_offer_unpublished_correctly(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        time.sleep(3)
        token, index = test_authorization()
        time.sleep(3)
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': token}
        self.host = host
        self.command_offer_create = 'management/offers/create'
        self.command_offer_unpublish = 'management/offers/unpublish'
        self.command_offer_delete = 'management/offers/delete'

        self.command_category_create = 'management/categories/create'

        self.url_category_create = 'http://{}/{}'.format(self.host, self.command_category_create)
        userdata = json.dumps({"parent_id": 3, "is_last": "false", "title": "string", "description": "string"})

        response2 = s.post(self.url_category_create, data=userdata, headers=headers)
        self.assertEqual(response2.status_code, SUCCESS)
        res = json.loads(response2.content)
        identifier = res['id']

        self.command_business_create = 'management/businesses/create'

        self.url_business_create = 'http://{}/{}'.format(self.host, self.command_business_create)
        email_value = time.strftime("%d%m%Y" + "%H%M%S") + "@" + "test.com"
        userdata = json.dumps(
            {"partner_id": 1, "email": email_value, "business_id_by_partner": "string", "address": "string",
             "geo_latitude": "48.92279", "geo_longitude": "22.4519749", "name": "string", "description": "string"})

        response2 = s.post(self.url_business_create, data=userdata, headers=headers)
        self.assertEqual(response2.status_code, SUCCESS)
        res = json.loads(response2.content)
        index = res['id']

        self.command_offer_create = 'management/offers/create'

        self.url_offer_create = 'http://{}/{}'.format(self.host, self.command_offer_create)
        userdata = json.dumps(
            {"title": "string1", "description": "string", "business_id": index, "main_category_id": identifier,
             "SKU": "string", "offer_quantity": 0, "offer_id_by_partner": "string", "delivery_cost": 0, "vat": 0})
        response2 = s.post(self.url_offer_create, data=userdata, headers=headers)

        self.assertEqual(response2.status_code, SUCCESS)

        res = json.loads(response2.content)
        index = res['id']
        self.offer_ids = 'offer_ids'
        self.url_offer_unpublish = 'http://{}/{}?{}={}'.format(self.host, self.command_offer_unpublish, self.offer_ids, index)

        response2 = s.post(self.url_offer_unpublish, headers=headers)

        self.assertEqual(response2.status_code, SUCCESS)

        self.command_offer_delete = 'management/offers/delete'
        self.url_offer_delete = 'http://{}/{}/{}'.format(self.host, self.command_offer_delete, index)

        response2 = s.delete(self.url_offer_delete, headers=headers)
        print response2
        self.assertEqual(response2.status_code, SUCCESS)


class Test_004_offer_Require_Categorization(unittest.TestCase):
    def __init__(self, *a, **kw):
        super(Test_004_offer_Require_Categorization, self).__init__(*a, **kw)

    def test_01_offer_require_categorization_set_correctly(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        time.sleep(3)
        token, index = test_authorization()
        time.sleep(3)
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': token}
        self.host = host
        self.command_offer_create = 'management/offers/create'
        self.command_offer_require_categorization = 'management/offers/require-categorization'
        self.command_offer_delete = 'management/offers/delete'

        self.command_category_create = 'management/categories/create'

        self.url_category_create = 'http://{}/{}'.format(self.host, self.command_category_create)
        userdata = json.dumps({"parent_id": 3, "is_last": "false", "title": "string", "description": "string"})

        response2 = s.post(self.url_category_create, data=userdata, headers=headers)
        self.assertEqual(response2.status_code, SUCCESS)
        res = json.loads(response2.content)
        identifier = res['id']

        self.command_business_create = 'management/businesses/create'

        self.url_business_create = 'http://{}/{}'.format(self.host, self.command_business_create)
        email_value = time.strftime("%d%m%Y" + "%H%M%S") + "@" + "test.com"
        userdata = json.dumps(
            {"partner_id": 1, "email": email_value, "business_id_by_partner": "string", "address": "string",
             "geo_latitude": "48.92279", "geo_longitude": "22.4519749", "name": "string", "description": "string"})

        response2 = s.post(self.url_business_create, data=userdata, headers=headers)
        self.assertEqual(response2.status_code, SUCCESS)
        res = json.loads(response2.content)
        index = res['id']

        self.command_offer_create = 'management/offers/create'

        self.url_offer_create = 'http://{}/{}'.format(self.host, self.command_offer_create)
        userdata = json.dumps(
            {"title": "string1", "description": "string", "business_id": index, "main_category_id": identifier,
             "SKU": "string", "offer_quantity": 0, "offer_id_by_partner": "string", "delivery_cost": 0, "vat": 0})
        response2 = s.post(self.url_offer_create, data=userdata, headers=headers)

        self.assertEqual(response2.status_code, SUCCESS)

        res = json.loads(response2.content)
        index = res['id']
        self.offer_ids = 'offer_ids'
        self.url_offer_require_categorization = 'http://{}/{}?{}={}'.format(self.host, self.command_offer_require_categorization, self.offer_ids, index)

        response2 = s.post(self.url_offer_require_categorization, headers=headers)

        self.assertEqual(response2.status_code, SUCCESS)

        self.command_offer_delete = 'management/offers/delete'
        self.url_offer_delete = 'http://{}/{}/{}'.format(self.host, self.command_offer_delete, index)

        response2 = s.delete(self.url_offer_delete, headers=headers)
        print response2
        self.assertEqual(response2.status_code, SUCCESS)


class Test_004_offer_Extra_Categories(unittest.TestCase):
    def __init__(self, *a, **kw):
        super(Test_004_offer_Extra_Categories, self).__init__(*a, **kw)

    def test_01_offer_added_and_removed_extra_categories_correctly(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        time.sleep(3)
        token, index = test_authorization()
        time.sleep(3)
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': token}
        self.host = host
        self.command_category_create = 'management/categories/create'

        self.url_category_create = 'http://{}/{}'.format(self.host, self.command_category_create)
        userdata = json.dumps({"parent_id": 2, "is_last": "false", "title": "string", "description": "string"})

        response2 = s.post(self.url_category_create, data=userdata, headers=headers)
        cont = json.loads(response2.content)
        identifier = cont['id']
        self.assertEqual(response2.status_code, SUCCESS)
        self.command_offer_create = 'management/offers/create'

        self.command_offer_attach_extra_category = 'management/offers/attach/extra-categories'
        self.command_offer_detach_extra_category = 'management/offers/detach/extra-categories'

        self.command_offer_delete = 'management/offers/delete'

        self.command_category_create = 'management/categories/create'

        self.url_category_create = 'http://{}/{}'.format(self.host, self.command_category_create)
        userdata = json.dumps({"parent_id": 3, "is_last": "false", "title": "string", "description": "string"})

        response2 = s.post(self.url_category_create, data=userdata, headers=headers)
        self.assertEqual(response2.status_code, SUCCESS)
        res = json.loads(response2.content)
        identifier = res['id']

        self.command_business_create = 'management/businesses/create'

        self.url_business_create = 'http://{}/{}'.format(self.host, self.command_business_create)
        email_value = time.strftime("%d%m%Y" + "%H%M%S") + "@" + "test.com"
        userdata = json.dumps(
            {"partner_id": 1, "email": email_value, "business_id_by_partner": "string", "address": "string",
             "geo_latitude": "48.92279", "geo_longitude": "22.4519749", "name": "string", "description": "string"})

        response2 = s.post(self.url_business_create, data=userdata, headers=headers)
        self.assertEqual(response2.status_code, SUCCESS)
        res = json.loads(response2.content)
        index = res['id']

        self.command_offer_create = 'management/offers/create'

        self.url_offer_create = 'http://{}/{}'.format(self.host, self.command_offer_create)
        userdata = json.dumps(
            {"title": "string1", "description": "string", "business_id": index, "main_category_id": identifier,
             "SKU": "string", "offer_quantity": 0, "offer_id_by_partner": "string", "delivery_cost": 0, "vat": 0})
        response2 = s.post(self.url_offer_create, data=userdata, headers=headers)

        self.assertEqual(response2.status_code, SUCCESS)

        res = json.loads(response2.content)
        index = res['id']
        self.offer_ids = 'offer_id'
        self.category_ids = 'category_ids'

        self.url_offer_attach_extra_categories = 'http://{}/{}?{}={}&{}={}'.format(self.host, self.command_offer_attach_extra_category, self.offer_ids, index, self.category_ids, identifier)

        response2 = s.post(self.url_offer_attach_extra_categories, headers=headers)

        self.assertEqual(response2.status_code, ACTION_IS_DONE)

        self.url_offer_detach_extra_categories = 'http://{}/{}?{}={}&{}={}'.format(self.host,
                                                                                   self.command_offer_detach_extra_category,
                                                                                   self.offer_ids, index,
                                                                                   self.category_ids, identifier)

        response2 = s.delete(self.url_offer_detach_extra_categories, headers=headers)

        self.assertEqual(response2.status_code, ACTION_IS_DONE)
        self.command_category_delete = 'management/categories/delete'

        self.url_category_delete = 'http://{}/{}/{}'.format(self.host, self.command_category_delete, identifier)
        response2 = s.delete(self.url_category_delete, headers=headers)
        print response2
        self.assertEqual(response2.status_code, SUCCESS)


        self.command_offer_delete = 'management/offers/delete'
        self.url_offer_delete = 'http://{}/{}/{}'.format(self.host, self.command_offer_delete, index)

        response2 = s.delete(self.url_offer_delete, headers=headers)
        print response2
        self.assertEqual(response2.status_code, SUCCESS)

class Test_004_offer_Deleting(unittest.TestCase):
        def __init__(self, *a, **kw):
                super(Test_004_offer_Deleting, self).__init__(*a, **kw)

        def test_01_offer_deleted_correctly(self):
            with open('USER_DATA.json') as data_file:
                data = json.load(data_file)
            s = requests.Session()
            time.sleep(3)
            token, index = test_authorization()
            time.sleep(3)
            headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': token}
            self.host = host
            self.command_offer_create = 'management/offers/create'

            self.command_category_create = 'management/categories/create'

            self.url_category_create = 'http://{}/{}'.format(self.host, self.command_category_create)
            userdata = json.dumps({"parent_id": 3, "is_last": "false", "title": "string", "description": "string"})

            response2 = s.post(self.url_category_create, data=userdata, headers=headers)
            self.assertEqual(response2.status_code, SUCCESS)
            res = json.loads(response2.content)
            identifier = res['id']

            self.command_business_create = 'management/businesses/create'

            self.url_business_create = 'http://{}/{}'.format(self.host, self.command_business_create)
            email_value = time.strftime("%d%m%Y" + "%H%M%S") + "@" + "test.com"
            userdata = json.dumps(
                {"partner_id": 1, "email": email_value, "business_id_by_partner": "string", "address": "string",
                 "geo_latitude": "48.92279", "geo_longitude": "22.4519749", "name": "string", "description": "string"})

            response2 = s.post(self.url_business_create, data=userdata, headers=headers)
            self.assertEqual(response2.status_code, SUCCESS)
            res = json.loads(response2.content)
            index = res['id']

            self.command_offer_create = 'management/offers/create'

            self.url_offer_create = 'http://{}/{}'.format(self.host, self.command_offer_create)
            userdata = json.dumps(
                {"title": "string1", "description": "string", "business_id": index, "main_category_id": identifier,
                 "SKU": "string", "offer_quantity": 0, "offer_id_by_partner": "string", "delivery_cost": 0, "vat": 0})
            response2 = s.post(self.url_offer_create, data=userdata, headers=headers)
            res = json.loads(response2.content)
            index = res['id']




            self.assertEqual(response2.status_code, SUCCESS)
            self.host = host
            self.command_offer_update = 'management/offers/update'
            self.url_offer_update = 'http://{}/{}/{}'.format(self.host, self.command_offer_update, index)
            userdata = json.dumps({"title": "stringebfherfberfeferferfrf"})

            response2 = s.patch(self.url_offer_update, data=userdata, headers=headers)
            print response2
            self.assertEqual(response2.status_code, SUCCESS)

            self.host = host
            self.command_offer_delete = 'management/offers/delete'
            self.url_offer_delete = 'http://{}/{}/{}'.format(self.host, self.command_offer_delete, index)

            response2 = s.delete(self.url_offer_delete, headers=headers)
            print response2
            self.assertEqual(response2.status_code, SUCCESS)




class Test_004_All_Partners(unittest.TestCase):

    def __init__(self, *a, **kw):
        super(Test_004_All_Partners, self).__init__(*a, **kw)
        self.host = host
        self.command_all_partners = 'management/partners'

        self.url_all_partners = 'http://{}/{}'.format(self.host, self.command_all_partners)


    def test_01_all_partners_opened(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        time.sleep(3)
        token, index = test_authorization()
        time.sleep(3)
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': token}
        response2 = s.get(self.url_all_partners, headers=headers)
        print response2
        self.assertEqual(response2.status_code, SUCCESS)

class Test_004_Partner_Show(unittest.TestCase):

    def __init__(self, *a, **kw):
        super(Test_004_Partner_Show, self).__init__(*a, **kw)



    def test_01_partner_page_showed_correctly(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        time.sleep(3)
        token, index = test_authorization()
        time.sleep(3)
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': token}
        self.host = host
        self.command_all_partners = 'manageement/partners'

        self.url_all_partners = 'http://{}/{}'.format(self.host, self.command_all_partners)
        partners = s.get(self.url_all_partners, headers=headers)

        index = 6
        print index
        self.host = host
        self.command_partner_show = 'management/partners/show'

        self.url_partner_show = 'http://{}/{}/{}'.format(self.host, self.command_partner_show, index)
        response2 = s.get(self.url_partner_show, headers=headers)
        print response2
        self.assertEqual(response2.status_code, SUCCESS)


# class Test_004_Partner_Creation(unittest.TestCase):
#     def __init__(self, *a, **kw):
#         super(Test_004_Partner_Creation, self).__init__(*a, **kw)
#
#     def test_01_partner_created_correctly(self):
#         with open('USER_DATA.json') as data_file:
#             data = json.load(data_file)
#         s = requests.Session()
#         headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER}
#         self.host = host
#         self.command_partner_create = 'management/partners/create'
#
#         self.url_partner_create = 'http://{}/{}'.format(self.host, self.command_partner_create)
#         words = ["python", "jumble", "easy", "difficult", "answer", "xylophone"]
#         newvalue = random.choice(words) + random.choice(words)
#         nameunique = "testuser" + random.choice(words) + random.choice(words)
#         userdata = json.dumps({"name": newvalue, "sync_period": nameunique})
#
#         response2 = s.post(self.url_partner_create, data=userdata, headers=headers)
#
#         self.assertEqual(response2.status_code, SUCCESS)
#
class Test_004_Partner_Updating(unittest.TestCase):
        def __init__(self, *a, **kw):
                super(Test_004_Partner_Updating, self).__init__(*a, **kw)

        def test_01_partner_updated_correctly(self):
            with open('USER_DATA.json') as data_file:
                data = json.load(data_file)
            s = requests.Session()
            time.sleep(3)
            token, index = test_authorization()
            time.sleep(3)
            headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': token}
            index = 6
            self.host = host
            self.command_partner_update = 'management/partners/update'
            self.url_partner_update = 'http://{}/{}/{}'.format(self.host, self.command_partner_update, index)
            userdata = json.dumps({"sync_period": "daily"})
            response2 = s.patch(self.url_partner_update, data=userdata, headers=headers)
            print response2
            self.assertEqual(response2.status_code, SUCCESS)


class Test_004_Role_Attaching(unittest.TestCase):
    def __init__(self, *a, **kw):
        super(Test_004_Role_Attaching, self).__init__(*a, **kw)

    def test_01_role_is_attached_successfully(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        time.sleep(3)
        token, user_id = test_authorization()
        time.sleep(3)
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': token}
        role_id = 11
        self.host = host
        self.command_role_attach = 'management/users/attach/role'
        self.userId = 'userId'
        self.role_id = 'role_id'
        self.url_role_attach = 'http://{}/{}?{}={}&{}={}'.format(self.host, self.command_role_attach,self.userId, user_id, self.role_id, role_id)
        response2 = s.post(self.url_role_attach, headers=headers)
        print response2
        self.assertEqual(response2.status_code, ACTION_IS_DONE)


class Test_004_Role_Detaching(unittest.TestCase):
    def __init__(self, *a, **kw):
        super(Test_004_Role_Detaching, self).__init__(*a, **kw)

    def test_01_role_is_detached_successfully(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        time.sleep(3)
        token, user_id = test_authorization()
        time.sleep(3)
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': token}
        role_id = 11
        self.host = host
        self.command_role_detach = 'management/users/detach/role'
        self.userId = 'userId'
        self.role_id = 'role_id'
        self.url_role_detach = 'http://{}/{}?{}={}&{}={}'.format(self.host, self.command_role_detach, self.userId,
                                                                 user_id, self.role_id, role_id)
        response2 = s.delete(self.url_role_detach, headers=headers)
        print response2
        self.assertEqual(response2.status_code, ACTION_IS_DONE)


class Test_004_Image_Attaching(unittest.TestCase):
    def __init__(self, *a, **kw):
        super(Test_004_Image_Attaching, self).__init__(*a, **kw)

    def test_01_image_is_attached_successfully(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        time.sleep(3)
        token, user_id = test_authorization()
        time.sleep(3)
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': token}
        self.partner_id = 'partner_id'
        partner_id = 6
        self.image_id = 'image_id'
        image_id = 612
        self.host = host
        self.command_image_attach = 'management/partners/image/attach'
        self.command_image_detach = 'management/partners/image/detach'


        self.url_image_attach = 'http://{}/{}?{}={}&{}={}'.format(self.host, self.command_image_attach, self.partner_id,
                                                                 partner_id, self.image_id, image_id)
        response2 = s.post(self.url_image_attach, headers=headers)
        print response2
        self.assertEqual(response2.status_code, ADDED)
        self.url_image_detach = 'http://{}/{}?{}={}&{}={}'.format(self.host, self.command_image_detach, self.partner_id,
                                                                 partner_id, self.image_id, image_id)
        response2 = s.delete(self.url_image_detach, headers=headers)
        self.assertEqual(response2.status_code, DETACHED)


class Test_004_attach_image_to_business(unittest.TestCase):
    def __init__(self, *a, **kw):
        super(Test_004_attach_image_to_business, self).__init__(*a, **kw)

    def test_01_image_is_attached_successfully(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        time.sleep(5)
        token, index = test_authorization()
        time.sleep(5)
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': token}
        self.host = host
        self.command_business_create = 'management/businesses/create'

        self.url_business_create = 'http://{}/{}'.format(self.host, self.command_business_create)
        email_value = time.strftime("%d%m%Y" + "%H%M%S") + "@" + "test.com"
        userdata = json.dumps \
            ({"partner_id": 1, "email": email_value, "business_id_by_partner": "string", "address": "string", "geo_latitude": "48.92279", "geo_longitude": "22.4519749", "name": "string", "description": "string"})

        response2 = s.post(self.url_business_create, data=userdata, headers=headers)
        self.assertEqual(response2.status_code, SUCCESS)
        res = json.loads(response2.content)
        print res
        identificator = res['id']

        self.command_businesses_image_attach = 'management/businesses/image/attach'
        self.command_businesses_image_detach = 'management/businesses/image/detach'

        self.business_id = 'business_id'
        self.image_id = 'image_id'
        image_id = 612
        self.url_businesses_image_attach = 'http://{}/{}?{}={}&{}={}'.format(self.host, self.command_businesses_image_attach, self.business_id,
                                                                  identificator, self.image_id, image_id)
        response2 = s.post(self.url_businesses_image_attach, headers=headers)
        print response2
        self.assertEqual(response2.status_code, ADDED)
        self.url_businesses_image_detach = 'http://{}/{}?{}={}&{}={}'.format(self.host,
                                                                             self.command_businesses_image_detach,
                                                                             self.business_id,
                                                                             identificator, self.image_id, image_id)
        response2 = s.delete(self.url_businesses_image_detach, headers=headers)
        self.assertEqual(response2.status_code, DETACHED)

        self.command_business_delete = 'management/businesses/delete'
        self.url_business_delete = 'http://{}/{}/{}'.format(self.host, self.command_business_delete, identificator)
        response2 = s.delete(self.url_business_delete, headers=headers)
        print response2
        self.assertEqual(response2.status_code, SUCCESS)


class Test_004_Image_Uploading(unittest.TestCase):
    def __init__(self, *a, **kw):
        super(Test_004_Image_Uploading, self).__init__(*a, **kw)

    def test_01_image_is_upload_successfully(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        time.sleep(3)
        token, user_id = test_authorization()
        time.sleep(3)
        headers = {'Authorization': token}
        self.partner_id = 'partner_id'
        partner_id = 6
        self.image_id = 'image_id'
        image_id = 612
        self.host = host
        self.command_image_upload = 'management/images/upload'
        self.command_image_delete = 'management/images/delete'


        self.url_image_upload = 'http://{}/{}'.format(self.host, self.command_image_upload)
        postdata = {}
        files = {'image': open('picture.jpg', 'rb')}

        response2 = s.post(self.url_image_upload, headers=headers, data=postdata, files=files )
        res = json.loads(response2.content)
        print res
        identificator = res['id']


        self.assertEqual(response2.status_code, SUCCESS)

        self.url_image_delete = 'http://{}/{}/{}'.format(self.host, self.command_image_delete, identificator)
        response2 = s.delete(self.url_image_delete, headers=headers)
        self.assertEqual(response2.status_code, SUCCESS)




if __name__ == '__main__':
    unittest.main()