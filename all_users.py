import json
from random import choice

import requests
import unittest

import time

from test import host, DEFAULT_HEADER, SUCCESS, BADDATA


class Test_004_ServerRegister(unittest.TestCase):

    def __init__(self, *a, **kw):
        super(Test_004_ServerRegister, self).__init__(*a, **kw)
        self.host = host
        self.command_users = 'users'

        self.url_all_users = 'http://{}/{}'.format(self.host, self.command_users)


    def test_01_all_users_showed_successfully(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER}
        response2 = s.get(self.url_all_users, headers=headers)
        self.assertEqual(response2.status_code, SUCCESS)

    def _get_accounts(self, identificator=None):
        _url = self.url_all_users
        if identificator:
            _url = "{}/{}".format(self.url_all_users, identificator)
        _response = requests.get(_url)
        return _response.status_code, _response.json()

    def _get_list_of(self, key):
        _, data = self._get_accounts()
        return map(lambda x: x.get(key), data.get('full_name'))

    def _delete_account(self, identificator):
        _response = requests.delete("{}/{}".format(self.url_all_users, identificator))
        return _response.status_code, _response.json()

