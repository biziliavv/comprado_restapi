import json
import requests
import unittest

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
LASTNAME = time.strftime("%d/%m/%Y"+"%H:%M:%S")+"@"+"test.com"
EMAIL = 'biziliavv@gmail.com'
PSW = "123456"
host = '54.93.81.169/api/v1'

class Test_004_All_offers(unittest.TestCase):

    def __init__(self, *a, **kw):
        super(Test_004_All_offers, self).__init__(*a, **kw)
        self.host = host
        self.command_all_offers = 'offers'

        self.url_all_offers = 'http://{}/{}'.format(self.host, self.command_all_offers)


    def test_01_all_offers_opened(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER}
        response2 = s.get(self.url_all_offers, headers=headers)
        print response2
        self.assertEqual(response2.status_code, SUCCESS)

class Test_004_offer_Show(unittest.TestCase):

    def __init__(self, *a, **kw):
        super(Test_004_offer_Show, self).__init__(*a, **kw)



    def test_01_offer_page_showed_correctly(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER}
        self.host = host
        self.command_all_offers = 'offers'

        self.url_all_offers = 'http://{}/{}'.format(self.host, self.command_all_offers)
        offers = s.get(self.url_all_offers, headers=headers)
        m = json.loads(offers.content)

        print m
        print m['data'][1]
        index = int(m['data'][1]['id'])
        print index
        self.host = host
        self.command_offer_show = 'offers/show'

        self.url_offer_show = 'http://{}/{}/{}'.format(self.host, self.command_offer_show, index)
        response2 = s.get(self.url_offer_show, headers=headers)
        print response2
        self.assertEqual(response2.status_code, SUCCESS)


class Test_004_offer_Creation(unittest.TestCase):
    def __init__(self, *a, **kw):
        super(Test_004_offer_Creation, self).__init__(*a, **kw)

    def test_01_offer_created_correctly(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER}
        self.host = host
        self.command_offer_create = 'offers/create'

        self.url_offer_create = 'http://{}/{}'.format(self.host, self.command_offer_create)
        userdata = json.dumps({"title": "string1", "description": "string", "business_id": 0, "category_id": 0, "SKU": "string","offer_quantity": 0, "offer_id_by_partner": "string", "delivery_cost": 0, "vat": 0})

        response2 = s.post(self.url_offer_create, data=userdata, headers=headers)

        self.assertEqual(response2.status_code, SUCCESS)

class Test_004_offer_Deleting(unittest.TestCase):
        def __init__(self, *a, **kw):
                super(Test_004_offer_Deleting, self).__init__(*a, **kw)

        def test_01_offer_deleted_correctly(self):
            with open('USER_DATA.json') as data_file:
                data = json.load(data_file)
            s = requests.Session()
            headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER}
            self.host = host
            self.command_all_offers = 'offers'

            self.url_all_offers = 'http://{}/{}'.format(self.host, self.command_all_offers)
            offers = s.get(self.url_all_offers, headers=headers)
            m = json.loads(offers.content)

            print m
            print m['data'][1]
            index = int(m['data'][1]['id'])
            print index

            self.host = host
            self.command_offer_update = 'offers/update'
            self.url_offer_update = 'http://{}/{}/{}'.format(self.host, self.command_offer_update, index)
            userdata = json.dumps({"title": "newtitle", "category_id": "1"})
            response2 = s.patch(self.url_offer_update, data=userdata, headers=headers)
            print response2
            self.assertEqual(response2.status_code, SUCCESS)

            self.host = host
            self.command_offer_delete = 'offers/delete'
            self.url_offer_delete = 'http://{}/{}/{}'.format(self.host, self.command_offer_delete, index)
            response2 = s.delete(self.url_offer_delete, headers=headers)
            print response2
            self.assertEqual(response2.status_code, SUCCESS)

if __name__ == '__main__':
    unittest.main()