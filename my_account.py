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
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': "Bearer :eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjE0LCJpc3MiOiJodHRwOlwvXC81NC45My44MS4xNjlcL2FwaVwvdjFcL2F1dGhcL3NpZ25pblwvZmIiLCJpYXQiOjE0ODEyNzIyNTgsImV4cCI6MTQ4MTI3NTg1OCwibmJmIjoxNDgxMjcyMjU4LCJqdGkiOiI0MTI1NzAyMTUzMjA4ZDA0ZTJhZWYxNTE0NGEyNzNjZiJ9.xpmewGTBdY7HlGoYII-v0gAe8yf8VhC6bga8uKi3RPk"}

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
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER, 'Authorization': "Bearer :eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjE0LCJpc3MiOiJodHRwOlwvXC81NC45My44MS4xNjlcL2FwaVwvdjFcL2F1dGhcL3NpZ25pblwvZmIiLCJpYXQiOjE0ODEyNzIyNTgsImV4cCI6MTQ4MTI3NTg1OCwibmJmIjoxNDgxMjcyMjU4LCJqdGkiOiI0MTI1NzAyMTUzMjA4ZDA0ZTJhZWYxNTE0NGEyNzNjZiJ9.xpmewGTBdY7HlGoYII-v0gAe8yf8VhC6bga8uKi3RPk"}
        userdata = json.dumps({"name": "VitaliyBizilia"})

        response2 = s.post(self.url_profile_edit, data=userdata, headers=headers)

        self.assertEqual(response2.status_code, SUCCESS)
