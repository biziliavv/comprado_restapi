import json
import requests
import unittest
from authorization import test_authorization
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
FINISHED = 202

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
        self.isocode = 'isocode1'
        self.isocode_value = 'sv'
        self.latitude = 'latitude'
        latitude_value = 59.3258414
        self.longitude = 'longitude'
        longitude_value = 17.7073729
        self.url_all_offers = 'http://{}/{}?{}={}&{}={}&{}={}'.format(self.host, self.command_all_offers, self.isocode, self.isocode_value, self.latitude, latitude_value, self.longitude, longitude_value)



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
        self.isocode = 'isocode1'
        self.isocode_value = 'sv'
        self.latitude = 'latitude'
        latitude_value  = 59.3258414
        self.longitude = 'longitude'
        longitude_value = 17.7073729

        self.url_all_offers = 'http://{}/{}?{}={}&{}={}&{}={}'.format(self.host, self.command_all_offers, self.isocode, self.isocode_value, self.latitude, latitude_value, self.longitude, longitude_value)
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


class Test_004_bestOffers(unittest.TestCase):
    def __init__(self, *a, **kw):
        super(Test_004_bestOffers, self).__init__(*a, **kw)

    def test_01_best_offers_showed_correctly(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER}
        self.host = host
        self.command_best_offers = 'offers/best'
        self.isocode = 'isocode1'
        self.isocode_value = 'en'
        self.category_ids_title = 'category_ids'
        self.category_ids_numbers = '85%2C86%2C87'
        self.url_best_offers = 'http://{}/{}?{}={}&{}={}'.format(self.host, self.command_best_offers,
                                                                  self.isocode, self.isocode_value, self.category_ids_title, self.category_ids_numbers)
        response2 = s.get(self.url_best_offers, headers=headers)
        print response2
        self.assertEqual(response2.status_code, SUCCESS)

class Test_004_offer_liking_disliking(unittest.TestCase):
    def __init__(self, *a, **kw):
        super(Test_004_offer_liking_disliking, self).__init__(*a, **kw)

    def test_01_offer_liked_and_disliked_correctly(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        time.sleep(3)
        token, index = test_authorization()
        time.sleep(3)
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': token}
        self.host = host
        self.command_offer_create = 'management/offers/create'

        self.url_offer_create = 'http://{}/{}'.format(self.host, self.command_offer_create)
        userdata = json.dumps({"title": "string1", "description": "string", "business_id": 115, "main_category_id": 97, "SKU": "string","offer_quantity": 0, "offer_id_by_partner": "string", "delivery_cost": 0, "vat": 0})

        response2 = s.post(self.url_offer_create, data=userdata, headers=headers)

        self.assertEqual(response2.status_code, SUCCESS)
        res = json.loads(response2.content)
        print res
        identificator = res['id']
        self.command_offer_like = 'offers/like'
        self.command_offer_dislike = 'offers/dislike'

        self.offer_id = 'offer_id'

        self.url_offer_like = 'http://{}/{}?{}={}'.format(self.host, self.command_offer_like, self.offer_id, identificator)

        response2 = s.post(self.url_offer_like, headers=headers)
        self.assertEqual(response2.status_code, FINISHED)
        self.url_offer_dislike = 'http://{}/{}?{}={}'.format(self.host, self.command_offer_dislike, self.offer_id,
                                                          identificator)

        response2 = s.delete(self.url_offer_dislike, headers=headers)
        self.assertEqual(response2.status_code, FINISHED)

        self.command_offer_delete = 'management/offers/delete'
        self.url_offer_delete = 'http://{}/{}/{}'.format(self.host, self.command_offer_delete, identificator)

        response2 = s.delete(self.url_offer_delete, headers=headers)
        print response2
        self.assertEqual(response2.status_code, SUCCESS)


if __name__ == '__main__':
    unittest.main()
