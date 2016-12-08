import json
import requests
import unittest

import time

from test import host, DEFAULT_HEADER, SUCCESS, BADDATA

class Test_004_All_Partners(unittest.TestCase):

    def __init__(self, *a, **kw):
        super(Test_004_All_Partners, self).__init__(*a, **kw)
        self.host = host
        self.command_all_partners = 'partners'

        self.url_all_partners = 'http://{}/{}'.format(self.host, self.command_all_partners)


    def test_01_all_partners_opened(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER}
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
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER}
        self.host = host
        self.command_all_partners = 'partners'

        self.url_all_partners = 'http://{}/{}'.format(self.host, self.command_all_partners)
        partners = s.get(self.url_all_partners, headers=headers)
        m = json.loads(partners.content)

        print m
        print m['data'][2]
        index = int(m['data'][2]['id'])
        print index
        self.host = host
        self.command_partner_show = 'partners/show'

        self.url_partner_show = 'http://{}/{}/{}'.format(self.host, self.command_partner_show, index)
        response2 = s.get(self.url_partner_show, headers=headers)
        print response2
        self.assertEqual(response2.status_code, SUCCESS)


class Test_004_Partner_Creation(unittest.TestCase):
    def __init__(self, *a, **kw):
        super(Test_004_Partner_Creation, self).__init__(*a, **kw)

    def test_01_partner_created_correctly(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER}
        self.host = host
        self.command_partner_create = 'partners/create'

        self.url_partner_create = 'http://{}/{}'.format(self.host, self.command_partner_create)
        userdata = json.dumps({"name": "testPartner", "sync_period": "testPartner"})

        response2 = s.post(self.url_partner_create, data=userdata, headers=headers)

        self.assertEqual(response2.status_code, SUCCESS)

class Test_004_Partner_Deleting(unittest.TestCase):
        def __init__(self, *a, **kw):
                super(Test_004_Partner_Deleting, self).__init__(*a, **kw)

        def test_01_partner_deleted_correctly(self):
            with open('USER_DATA.json') as data_file:
                data = json.load(data_file)
            s = requests.Session()
            headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER}
            self.host = host
            self.command_all_partners = 'partners'

            self.url_all_partners = 'http://{}/{}'.format(self.host, self.command_all_partners)
            partners = s.get(self.url_all_partners, headers=headers)
            m = json.loads(partners.content)

            print m
            print m['data'][3]
            index = int(m['data'][3]['id'])
            print index

            self.host = host
            self.command_partner_update = 'partners/update'
            self.url_partner_update = 'http://{}/{}/{}'.format(self.host, self.command_partner_update, index)
            userdata = json.dumps({"name": "partnerTest"})
            response2 = s.patch(self.url_partner_update, data=userdata, headers=headers)
            print response2
            self.assertEqual(response2.status_code, SUCCESS)

            self.host = host
            self.command_partner_delete = 'partners/delete'
            self.url_partner_delete = 'http://{}/{}/{}'.format(self.host, self.command_partner_delete, index)
            response2 = s.delete(self.url_partner_delete, headers=headers)
            print response2
            self.assertEqual(response2.status_code, SUCCESS)