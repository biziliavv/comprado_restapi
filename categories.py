import json
import requests
import unittest

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



TAN = 9999
FIRSTNAME = "Oleg"
LASTNAME = time.strftime("%d/%m/%Y"+"%H:%M:%S")+"@"+"test.com"
EMAIL = 'biziliavv@gmail.com'
PSW = "123456"
host = '54.93.81.169/api/v1'

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
        self.isocode = 'isocode1'
        self.isocode_value = 'sv'
        self.parent_id = 'parent_id'
        self.parent_id_value = '2'
        self.page = 'page'
        self.page_number = '1'
        self.page_limit = 'limit'
        self.page_limit_value = '1000'


        self.url_all_categories = 'http://{}/{}?{}={}&{}={}&{}={}&{}={}'.format(self.host, self.command_all_categories, self.parent_id, self.parent_id_value, self.isocode, self.isocode_value, self.page, self.page_number, self.page_limit, self.page_limit_value)
        categories = s.get(self.url_all_categories, headers=headers)
        m = json.loads(categories.content)

        print m
        print m['data'][0]
        index = int(m['data'][0]['id'])
        print index
        self.host = host
        self.command_category_show = 'categories/show'

        self.url_category_show = 'http://{}/{}/{}'.format(self.host, self.command_category_show, index)
        response2 = s.get(self.url_category_show, headers=headers)
        print response2
        self.assertEqual(response2.status_code, SUCCESS)
    def test_01_category_page_short_version_showed_correctly(self):
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
        print m['data'][0]
        index = int(m['data'][0]['id'])
        print index
        self.host = host
        self.command_category_show = 'categories/show'

        self.url_category_show = 'http://{}/{}/{}'.format(self.host, self.command_category_show, index)
        response2 = s.get(self.url_category_show, headers=headers)
        print response2
        self.assertEqual(response2.status_code, SUCCESS)






if __name__ == '__main__':
    unittest.main()
