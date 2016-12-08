import json
import requests
import unittest

import time

from test import host, DEFAULT_HEADER, SUCCESS, BADDATA

class Test_004_My_Profile_View(unittest.TestCase):

    def __init__(self, *a, **kw):
        super(Test_004_My_Profile_View, self).__init__(*a, **kw)
        self.host = host
        self.command_profile_view = 'me'

        self.url_profile_view = 'http://{}/{}'.format(self.host, self.command_profile_view)


    def test_01_user_profile_opened(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': "Bearer :eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjIsImlzcyI6Imh0dHA6XC9cLzU0LjkzLjgxLjE2OVwvYXBpXC92MVwvYXV0aFwvc2lnbmluXC9mYiIsImlhdCI6MTQ4MTE4MjQwNSwiZXhwIjoxNDgxMTg2MDA1LCJuYmYiOjE0ODExODI0MDUsImp0aSI6IjExZjg0ODBkMDQ2YTk0MjVkOThlYjEzMWEwZDZjNTk5In0.xmr8sf8rAywB-6x75gtpJA3TL1hrDpooYHLnf-KldsU"}

        response2 = s.get(self.url_profile_view, headers=headers)
        print response2
        self.assertEqual(response2.status_code, SUCCESS)


class Test_004_My_Profile_Edit(unittest.TestCase):

    def __init__(self, *a, **kw):
        super(Test_004_My_Profile_Edit, self).__init__(*a, **kw)
        self.host = host
        self.command_profile_edit = 'me/update'

        self.url_profile_edit = 'http://{}/{}'.format(self.host, self.command_profile_edit)


    def test_01_user_profile_edited(self):
        with open('USER_DATA.json') as data_file:
            data = json.load(data_file)
        s = requests.Session()
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': "Bearer :eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjIsImlzcyI6Imh0dHA6XC9cLzU0LjkzLjgxLjE2OVwvYXBpXC92MVwvYXV0aFwvc2lnbmluXC9mYiIsImlhdCI6MTQ4MTE4MjQwNSwiZXhwIjoxNDgxMTg2MDA1LCJuYmYiOjE0ODExODI0MDUsImp0aSI6IjExZjg0ODBkMDQ2YTk0MjVkOThlYjEzMWEwZDZjNTk5In0.xmr8sf8rAywB-6x75gtpJA3TL1hrDpooYHLnf-KldsU"}
        userdata = json.dumps({"name": "VitaliyBizilia"})

        response2 = s.post(self.url_profile_edit, data=userdata, headers=headers)

        self.assertEqual(response2.status_code, SUCCESS)
