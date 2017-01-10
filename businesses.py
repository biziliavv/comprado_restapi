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

email_value = time.strftime("%d%m%Y" + "%H%M%S") + "@" + "test.com"
EMAIL = 'biziliavv@gmail.com'
PSW = "123456"
host = '54.93.81.169/api/v1'



class Test_004_All_businesses(unittest.TestCase):

    def __init__(self, *a, **kw):
        super(Test_004_All_businesses, self).__init__(*a, **kw)
        self.host = host
        self.command_all_businesses = 'businesses'

        self.url_all_businesses = 'http://{}/{}'.format(self.host, self.command_all_businesses)


    def test_01_all_businesses_opened(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()

        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER}
        response2 = s.get(self.url_all_businesses, headers=headers)
        print response2
        self.assertEqual(response2.status_code, SUCCESS)

class Test_004_business_Show(unittest.TestCase):

    def __init__(self, *a, **kw):
        super(Test_004_business_Show, self).__init__(*a, **kw)



    def test_01_business_page_showed_correctly(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER}
        self.host = host
        self.command_all_businesses = 'businesses'

        self.url_all_businesses = 'http://{}/{}'.format(self.host, self.command_all_businesses)
        businesses = s.get(self.url_all_businesses, headers=headers)
        m = json.loads(businesses.content)

        print m
        print m['data'][0]
        index = int(m['data'][0]['id'])
        print index
        self.host = host
        self.command_business_show = 'businesses/show'

        self.url_business_show = 'http://{}/{}/{}'.format(self.host, self.command_business_show, index)
        response2 = s.get(self.url_business_show, headers=headers)
        print response2
        self.assertEqual(response2.status_code, SUCCESS)





if __name__ == '__main__':
    unittest.main()
