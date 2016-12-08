import json
import requests
import unittest

import time

from test import host, DEFAULT_HEADER, SUCCESS, BADDATA

class Test_004_All_categories(unittest.TestCase):

    def __init__(self, *a, **kw):
        super(Test_004_All_categories, self).__init__(*a, **kw)
        self.host = host
        self.command_all_categories = 'categories'

        self.url_all_categories = 'http://{}/{}'.format(self.host, self.command_all_categories)


    def test_01_all_categories_opened(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER}
        response2 = s.get(self.url_all_categories, headers=headers)
        print response2
        self.assertEqual(response2.status_code, SUCCESS)

class Test_004_category_Show(unittest.TestCase):

    def __init__(self, *a, **kw):
        super(Test_004_category_Show, self).__init__(*a, **kw)



    def test_01_category_page_showed_correctly(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER}
        self.host = host
        self.command_all_categories = 'categories'

        self.url_all_categories = 'http://{}/{}'.format(self.host, self.command_all_categories)
        categories = s.get(self.url_all_categories, headers=headers)
        m = json.loads(categories.content)

        print m
        print m['data'][172]
        index = int(m['data'][172]['id'])
        print index
        self.host = host
        self.command_category_show = 'categories/show'

        self.url_category_show = 'http://{}/{}/{}'.format(self.host, self.command_category_show, index)
        response2 = s.get(self.url_category_show, headers=headers)
        print response2
        self.assertEqual(response2.status_code, SUCCESS)


class Test_004_category_Creation(unittest.TestCase):
    def __init__(self, *a, **kw):
        super(Test_004_category_Creation, self).__init__(*a, **kw)

    def test_01_category_created_correctly(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER}
        self.host = host
        self.command_category_create = 'categories/create'

        self.url_category_create = 'http://{}/{}'.format(self.host, self.command_category_create)
        userdata = json.dumps({"parent_id": 0, "is_last": "false", "title": "string", "description": "string"})

        response2 = s.post(self.url_category_create, data=userdata, headers=headers)

        self.assertEqual(response2.status_code, SUCCESS)

class Test_004_category_Deleting(unittest.TestCase):
        def __init__(self, *a, **kw):
                super(Test_004_category_Deleting, self).__init__(*a, **kw)

        def test_01_category_deleted_correctly(self):
            with open('USER_DATA.json') as data_file:
                data = json.load(data_file)
            s = requests.Session()
            headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER}
            self.host = host
            self.command_all_categories = 'categories'

            self.url_all_categories = 'http://{}/{}'.format(self.host, self.command_all_categories)
            categories = s.get(self.url_all_categories, headers=headers)
            m = json.loads(categories.content)

            print m
            print m['data'][172]
            index = int(m['data'][172]['id'])
            print index

            self.host = host
            self.command_category_update = 'categories/update'
            self.url_category_update = 'http://{}/{}/{}'.format(self.host, self.command_category_update, index)
            userdata = json.dumps({"title": "categoryTest"})
            response2 = s.patch(self.url_category_update, data=userdata, headers=headers)
            print response2
            self.assertEqual(response2.status_code, SUCCESS)

            self.host = host
            self.command_category_delete = 'categories/delete'
            self.url_category_delete = 'http://{}/{}/{}'.format(self.host, self.command_category_delete, index)
            response2 = s.delete(self.url_category_delete, headers=headers)
            print response2
            self.assertEqual(response2.status_code, SUCCESS)