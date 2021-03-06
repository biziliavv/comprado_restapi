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


if __name__ == '__main__':
    unittest.main()