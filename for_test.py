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
FINISHED = 202


email_value = time.strftime("%d%m%Y" + "%H%M%S") + "@" + "test.com"
EMAIL = 'biziliavv@gmail.com'
PSW = "123456"
host = '54.93.81.169/api/v1'


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

        response2 = s.post(self.url_offer_dislike, headers=headers)
        self.assertEqual(response2.status_code, FINISHED)
        response2 = s.post(self.url_offer_like, headers=headers)
        self.assertEqual(response2.status_code, FINISHED)
        self.url_offer_dislike = 'http://{}/{}?{}={}'.format(self.host, self.command_offer_dislike, self.offer_id,
                                                             identificator)

        response2 = s.post(self.url_offer_dislike, headers=headers)
        self.assertEqual(response2.status_code, FINISHED)
        response2 = s.post(self.url_offer_like, headers=headers)
        self.assertEqual(response2.status_code, FINISHED)
        self.url_offer_dislike = 'http://{}/{}?{}={}'.format(self.host, self.command_offer_dislike, self.offer_id,
                                                             identificator)

        response2 = s.post(self.url_offer_dislike, headers=headers)
        self.assertEqual(response2.status_code, FINISHED)
        response2 = s.post(self.url_offer_like, headers=headers)
        self.assertEqual(response2.status_code, FINISHED)
        self.url_offer_dislike = 'http://{}/{}?{}={}'.format(self.host, self.command_offer_dislike, self.offer_id,
                                                             identificator)

        response2 = s.post(self.url_offer_dislike, headers=headers)
        self.assertEqual(response2.status_code, FINISHED)

        self.command_offer_delete = 'management/offers/delete'
        self.url_offer_delete = 'http://{}/{}/{}'.format(self.host, self.command_offer_delete, identificator)

        response2 = s.delete(self.url_offer_delete, headers=headers)
        print response2
        self.assertEqual(response2.status_code, SUCCESS)


if __name__ == '__main__':
    unittest.main()