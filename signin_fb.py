import json
import requests
import unittest
from test import host, DEFAULT_HEADER, SUCCESS


class Test_004_ServerLoginByFacebook(unittest.TestCase):

    def __init__(self, *a, **kw):
        super(Test_004_ServerLoginByFacebook, self).__init__(*a, **kw)
        self.host = host
        self.command_signinbyfb = 'auth/signin/fb'

        self.url_signinbyfb = 'http://{}/{}'.format(self.host, self.command_signinbyfb)


    def test_01_register_successfully(self):
        # with open('USER_DATA.json') as data_file:
        #     data = json.load(data_file)
        #     for line in data:
        #         full_name= line["full_name"]
        #         email= line["email"]
        #         password = line["password"]
        #         have_car = line["have_car"]
        #         birthday = line["birthday"]

        s = requests.Session()
        headers = {'content-type': DEFAULT_HEADER, 'accept': DEFAULT_HEADER}
        userdata = json.dumps({"access_token": "EAACEdEose0cBAJdMjLCpu8xL5YKErHzgTh3nFSeeOabR9NLXe3pzOJx0DrIZCrdSfmpvUYEDgt7xnO9EPs0M01vcFoZAZAMLhfG94prHXNqcOpKOKZASN0dCIfnPlWjiOMHKtnjwvuyVFZA9kNwwdz9uBW7NE1YubJykiZATOnawZDZD"})
        response2 = s.post(self.url_signinbyfb, data=userdata, headers=headers)
        self.assertEqual(response2.status_code, SUCCESS)
