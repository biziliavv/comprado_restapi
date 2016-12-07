import requests
import unittest
import json
from random import choice

import time
from this import s

import rstr as rstr

DEFAULT_HEADER = 'application/json'

SUCCESS = 200
BADREQUEST = 400
ADDED = 201
UNAUTHORIZED = 401
UPGRADE_REQUIRED = 426
FORBIDDEN = 403
NOTFOUND = 404

TAN = 9999
FIRSTNAME = "Oleg"
LASTNAME = time.strftime("%d/%m/%Y"+"%H:%M:%S")
EMAIL = 'biziliavv@gmail.com'
PSW = "123456"
host = '54.93.81.169/api/v1'


def _login(headers=DEFAULT_HEADER, psw=PSW):
    s = requests.Session()
    url = 'http://{}/{}'.format(host, 'auth/signin')
    _headers = {'content-type': headers, 'accept': headers}

    response = s.post(url, data=_payload, headers=_headers)
    return s, response.status_code

# GET  /wallet/countries
class Test_001_ServerGetCountries(unittest.TestCase):

    def __init__(self, *a, **kw):
        super(Test_001_ServerGetCountries, self).__init__(*a, **kw)
        self.host = host
        self.command = 'wallet/countries'
        self.url = 'http://{}/{}'.format(self.host, self.command)

    def test_get_all_countries(self):
        status_code, text = self._test_get_countries()
        self.assertEqual(status_code, SUCCESS)

    def _test_get_countries(self):
        _response = requests.get(self.url)
        return _response.status_code, _response.json()

class Test_002_ServerGetDeiveID(unittest.TestCase):

    def __init__(self, *a, **kw):
        super(Test_002_ServerGetDeiveID, self).__init__(*a, **kw)
        self.host = host
        self.command = 'wallet/deviceid'
        self.url = 'http://{}/{}'.format(self.host, self.command)

    def test_get_deviceid(self):
        status_code, text = self._test_get_deviceid()
        self.assertEqual(status_code, SUCCESS)


    def _test_get_deviceid(self):
        _response = requests.get(self.url)
        return _response.status_code, _response.json()

class Test_003_ServerGetQuestions(unittest.TestCase):

    def __init__(self, *a, **kw):
        super(Test_003_ServerGetQuestions, self).__init__(*a, **kw)
        self.host = host
        self.command = 'wallet/questions'
        self.url = 'http://{}/{}'.format(self.host, self.command)

    def test_get_questions(self):
        status_code, text = self._test_get_questions()
        self.assertEqual(status_code, SUCCESS)

    def _test_get_questions(self):
        _response = requests.get(self.url)
        return _response.status_code, _response.json()

class Test_004_ServerRegistration(unittest.TestCase):

    def __init__(self, *a, **kw):
        super(Test_004_ServerRegistration, self).__init__(*a, **kw)
        self.host = host
        self.command_available = 'wallet/register/available'
        self.command_reserve = 'wallet/register/reserve'
        self.command_create = 'wallet/register/create'
        self.command_get_deviceid = 'wallet/deviceid'
        self.url_available = 'http://{}/{}'.format(self.host, self.command_available)
        self.url_reserve = 'http://{}/{}'.format(self.host, self.command_reserve)
        self.url_create = 'http://{}/{}'.format(self.host, self.command_create)
        self.url_getdevice = 'http://{}/{}'.format(self.host, self.command_get_deviceid)

    def test_01_register_successfully(self):
        s = requests.Session()
        headers = {'content-type': DEFAULT_HEADER, 'deviceId' : DEVICEID}
        payload = json.dumps({"phoneNumber": PHONE})
        response = s.post(self.url_available, data=payload, headers=headers)
        self.assertEqual(response.status_code, SUCCESS)
        #time.sleep(1)
        payload1 = json.dumps({"phoneNumber": PHONE, "tan": TAN})
        response1 = s.post(self.url_reserve, data=payload1, headers=headers)
        self.assertEqual(response1.status_code, SUCCESS)
        #time.sleep(1)
        payload2 = json.dumps({"firstName": FIRSTNAME, "lastName": LASTNAME, "email": EMAIL, "password":"123456", "phoneNumber":PHONE, "dateOfBirth": "06/01/1987", "qa":[{"q": 1, "a": "secret answer"}, {"q": 2, "a": "Kontrabas"}]})
        response2 = s.post(self.url_create, data=payload2, headers=headers)
        self.assertEqual(response2.status_code, SUCCESS)
        response3 = s.get(self.url_getdevice)
        self.assertEqual(response3.status_code, SUCCESS)

    def test_02_not_register_with_incorrect_TAN(self):
        s = requests.Session()
        headers = {'content-type': DEFAULT_HEADER, 'deviceId': DEVICEID}

        # time.sleep(1)
        payload1 = json.dumps({"phoneNumber": PHONE, "tan": '1414'})
        response1 = s.post(self.url_reserve, data=payload1, headers=headers)
        self.assertEqual(response1.status_code, UPGRADE_REQUIRED)

    def test_03_not_register_with_existing_phone(self):
        s = requests.Session()
        headers = {'content-type': DEFAULT_HEADER, 'deviceId': DEVICEID}
        payload = json.dumps({"phoneNumber": PHONE})
        response = s.post(self.url_available, data=payload, headers=headers)
        self.assertEqual(response.status_code, FORBIDDEN)




class Test_005_ServerLogin(unittest.TestCase):
    def __init__(self, *a, **kw):
        super(Test_005_ServerLogin, self).__init__(*a, **kw)
        self.host = host
        self.command_login = 'wallet/login'
        self.url_login = 'http://{}/{}'.format(self.host, self.command_login)

    def test_login_successfully(self):
        headers = {'content-type': DEFAULT_HEADER, 'deviceId': DEVICEID}
        _login(PHONE)


    def test_not_login_with_incorrect_password(self):
        headers = {'content-type': DEFAULT_HEADER, 'deviceId': DEVICEID}
        payload = json.dumps({"phoneNumber": PHONE, "password": "1234567"})
        response = requests.post(self.url_login, data=payload, headers=headers)
        self.assertEqual(response.status_code, UNAUTHORIZED)

    def test_not_login_with_incorrect_deviceid(self):
        headers = {'content-type': DEFAULT_HEADER, 'deviceId': '5454545454545454545'}
        payload = json.dumps({"phoneNumber": PHONE, "password": "123456"})
        response = requests.post(self.url_login, data=payload, headers=headers)
        self.assertEqual(response.status_code, UPGRADE_REQUIRED)

class Test_006_ServerLogout(unittest.TestCase):
    def __init__(self, *a, **kw):
        super(Test_006_ServerLogout, self).__init__(*a, **kw)
        self.host = host
        self.command_login = 'wallet/login'
        self.url_login = 'http://{}/{}'.format(self.host, self.command_login)
        self.command_logout = 'wallet/logout'
        self.url_logout = 'http://{}/{}'.format(self.host, self.command_logout)

    def test_logout(self):

        # Login
        current_session = _login(PHONE)
        self.assertEqual(current_session[1], SUCCESS)

        # Try logout
        response = current_session[0].get(self.url_logout)

        # Verify that logout successfully
        self.assertEqual(current_session[1], SUCCESS)

class Test_007_ServerChangePassword(unittest.TestCase):
    def __init__(self, *a, **kw):
        super(Test_007_ServerChangePassword, self).__init__(*a, **kw)
        self.host = host
        self.command_login = 'wallet/login'
        self.url_login = 'http://{}/{}'.format(self.host, self.command_login)
        self.command_logout = 'wallet/user/changePassword'
        self.url_change_password = 'http://{}/{}'.format(self.host, self.command_logout)
        self.headers = {'content-type': DEFAULT_HEADER, 'deviceId': DEVICEID}

    def test_01_change_password_negative_test(self):

        #Login
        current_session = _login(PHONE)
        self.assertEqual(current_session[1], SUCCESS)

        #Try set incorrect oldPassword
        payload1 = json.dumps({"newPassword": "12345678", "oldPassword": "1234567"})
        response1 = current_session[0].patch(self.url_change_password, data=payload1, headers=self.headers)
        self.assertEqual(response1.status_code, UNAUTHORIZED)

    def test_02_change_password(self):

        # Login
        current_session = _login(PHONE)
        self.assertEqual(current_session[1], SUCCESS)

        # Try change password
        payload2 = json.dumps({"newPassword": "12345678", "oldPassword": "123456"})
        response2 = current_session[0].patch(self.url_change_password, data=payload2, headers=self.headers)
        self.assertEqual(response2.status_code, SUCCESS)

        # Login again
        current_session = _login(PHONE,psw='12345678')
        self.assertEqual(current_session[1], SUCCESS)

        # Change to previuosly password
        payload2 = json.dumps({"newPassword": "123456", "oldPassword": "12345678"})
        response2 = current_session[0].patch(self.url_change_password, data=payload2, headers=self.headers)
        self.assertEqual(response2.status_code, SUCCESS)

class Test_008_ServerChangeEmail(unittest.TestCase):
    def __init__(self, *a, **kw):
        super(Test_008_ServerChangeEmail, self).__init__(*a, **kw)
        self.host = host
        self.command_login = 'wallet/login'
        self.url_login = 'http://{}/{}'.format(self.host, self.command_login)
        self.command_change_email = 'wallet/user/email/change'
        self.url_change_email = 'http://{}/{}'.format(self.host, self.command_change_email)
        self.headers = {'content-type': DEFAULT_HEADER, 'deviceId': DEVICEID}

    def test_01_change_email_to_not_valid(self):

        # Login
        current_session = _login(PHONE)
        self.assertEqual(current_session[1], SUCCESS)

        # Try set invalid email
        payload1 = json.dumps({"email": "testttt"})
        response1 = current_session[0].post(self.url_change_email, data=payload1, headers=self.headers)

        # Verify that appears error
        self.assertEqual(response1.status_code, BADREQUEST)

    def test_02_change_email_to_valid(self):

        # Login
        current_session = _login(PHONE)
        self.assertEqual(current_session[1], SUCCESS)

        # Try set valid email
        payload1 = json.dumps({"email": "test@test.com"})
        response1 = current_session[0].post(self.url_change_email, data=payload1, headers=self.headers)
        self.assertEqual(response1.status_code, SUCCESS)

        # Verify that email was changed successufully in your profile
        self._verify_email('test@test.com',current_session)

        # Login again
        current_session = _login(PHONE)

        # Set previously email address
        payload3 = json.dumps({"email": EMAIL})
        response3 = current_session[0].post(self.url_change_email, data=payload3, headers=self.headers)
        self.assertEqual(response3.status_code, SUCCESS)

        # Verify that email was changed successufully in your profile
        self._verify_email(Email=EMAIL, current_session=current_session)

    def _verify_email(self, Email, current_session):
        resp = current_session[0].get('http://{}/{}'.format(self.host, 'wallet/user/profile'))
        email = (resp.content).find(Email)
        self.assertNotEqual(email, "-1")

class Test_009_ServerProfile(unittest.TestCase):
    def __init__(self, *a, **kw):
        super(Test_009_ServerProfile, self).__init__(*a, **kw)
        self.host = host
        self.command_login = 'wallet/login'
        self.url_login = 'http://{}/{}'.format(self.host, self.command_login)
        self.command_get_profile = 'wallet/user/profile'
        self.url_get_profile = 'http://{}/{}'.format(self.host, self.command_get_profile)
        self.command_update_profile = 'wallet/user/profile'
        self.url_update_profile = 'http://{}/{}'.format(self.host, self.command_update_profile)
        self.headers = {'content-type': DEFAULT_HEADER, 'deviceId': DEVICEID}

    def test_01_try_update_email_and_phone_into_profile(self):

        # Login
        current_session = _login(PHONE)
        self.assertEqual(current_session[1], SUCCESS)

        # Try change_email
        payload1 = json.dumps({"email": "testttt@test.com"})
        response1 = current_session[0].patch(self.url_update_profile, data=payload1, headers=self.headers)

        # Verify that appears error
        self.assertEqual(response1.status_code, BADREQUEST)

        # Try change_phone
        payload2 = json.dumps({"phoneNumber": "09585844844"})
        response2 = current_session[0].patch(self.url_update_profile, data=payload2, headers=self.headers)

        # Verify that appears error
        self.assertEqual(response2.status_code, BADREQUEST)

    def test_02_change_profile_with_valid_data(self):

        # Login
        current_session = _login(PHONE)
        self.assertEqual(current_session[1], SUCCESS)

        # Try set valid email
        payload1 = json.dumps({"email": "test@test.com", "firstName":"TestName", "lastName":"TestLastName", "dateOfBirth":"06/01/1989"})
        response1 = current_session[0].patch(self.url_update_profile, data=payload1, headers=self.headers)
        self.assertEqual(response1.status_code, SUCCESS)

        # Verify that email was changed successufully in your profile
        self._verify_profile('test@test.com','TestName', 'TestLastName', '06/01/1989', current_session)

        # Login again
        current_session = _login(PHONE)

        # Set previously profile_information
        payload3 = json.dumps({"email": EMAIL, "firstName": FIRSTNAME, "lastName": LASTNAME, "dateOfBirth":"06/01/1987"})
        response3 = current_session[0].patch(self.url_update_profile, data=payload3, headers=self.headers)
        self.assertEqual(response3.status_code, SUCCESS)

        # Verify that email was changed successufully in your profile
        self._verify_profile(EMAIL, FIRSTNAME, LASTNAME, '06/01/1989', current_session)

    def _verify_profile(self, Email, firstName, lastName, birthday, current_session):
        resp = current_session[0].get('http://{}/{}'.format(self.host, 'wallet/user/profile'))
        email = (resp.content).find(Email)
        firstname = (resp.content).find(firstName)
        lastname = (resp.content).find(lastName)
        bDay = (resp.content).find(birthday)
        self.assertNotEqual(email, "-1")
        self.assertNotEqual(firstname, "-1")
        self.assertNotEqual(lastname, "-1")
        self.assertNotEqual(bDay, "-1")

class Test_010_ServerPassword(unittest.TestCase):
    def __init__(self, *a, **kw):
        super(Test_010_ServerPassword, self).__init__(*a, **kw)

        self.host = host
        self.command_login = 'wallet/login'
        self.url_login = 'http://{}/{}'.format(self.host, self.command_login)

        self.command_resetPassword_available = 'wallet/resetPassword/available'
        self.url_resetPassword_available = 'http://{}/{}'.format(self.host, self.command_resetPassword_available)

        self.command_resetPassword_verify = 'wallet/resetPassword/verify'
        self.url_resetPassword_verify = 'http://{}/{}'.format(self.host, self.command_resetPassword_verify)

        self.command_resetPassword_confirm = 'wallet/resetPassword/confirm'
        self.url_resetPassword_confirm = 'http://{}/{}'.format(self.host, self.command_resetPassword_confirm)

        self.command_resetPassword_reset = 'wallet/resetPassword/reset'
        self.url_resetPassword_reset = 'http://{}/{}'.format(self.host, self.command_resetPassword_reset)

        self.headers = {'content-type': DEFAULT_HEADER, 'deviceId': DEVICEID}

    def test_01_try_change_password_with_invalid_answers_for_question(self):

        # Login
        current_session = _login(PHONE)
        self.assertEqual(current_session[1], SUCCESS)

        # Verify_valid_phone_number
        payload = json.dumps({"phoneNumber": PHONE})
        response = current_session[0].post(self.url_resetPassword_available, data=payload, headers=self.headers)
        self.assertEqual(response.status_code, SUCCESS)

        # Try set valid email
        payload1 = json.dumps({"tan": 9999})
        response1 = current_session[0].post(self.url_resetPassword_verify, data=payload1, headers=self.headers)

        # Verify TAN
        self.assertEqual(response1.status_code, SUCCESS)

        #Confirm
        payload2 = json.dumps({"qa": [{"q": 1, "a": "secret answe"}, {"q": 2, "a": "Kontraba"}]})
        response2 = current_session[0].post(self.url_resetPassword_verify, data=payload2, headers=self.headers)
        # Verify confrim response
        self.assertEqual(response2.status_code, BADREQUEST)

    def test_02_try_change_password_with_valid_answers_for_question(self):
        # Login
        current_session = _login(PHONE)
        self.assertEqual(current_session[1], SUCCESS)

        # Verify_valid_phone_number
        payload = json.dumps({"phoneNumber": PHONE})
        response = current_session[0].post(self.url_resetPassword_available, data=payload, headers=self.headers)
        self.assertEqual(response.status_code, SUCCESS)

        # Try set valid email
        payload1 = json.dumps({"tan": 9999})
        response1 = current_session[0].post(self.url_resetPassword_verify, data=payload1, headers=self.headers)

        # Verify TAN
        self.assertEqual(response1.status_code, SUCCESS)

        # Confirm
        payload2 = json.dumps({"qa": [{"q": 1, "a": "secret answer"}, {"q": 2, "a": "Kontrabas"}]})
        response2 = current_session[0].post(self.url_resetPassword_confirm, data=payload2, headers=self.headers)
        # Verify confrim response
        self.assertEqual(response2.status_code, SUCCESS)

        # Reset password
        payload3 = json.dumps({"password":"123456789"})
        response3 = current_session[0].post(self.url_resetPassword_reset, data=payload3, headers=self.headers)

        # Verify confrim response
        self.assertEqual(response3.status_code, SUCCESS)

        #Try login with old password
        current_session = _login(PHONE)
        self.assertEqual(current_session[1], UNAUTHORIZED)

        # Try login with new password
        current_session = _login(PHONE, psw="123456789")
        self.assertEqual(current_session[1], SUCCESS)

    def test_03_try_back_password(self):
        # Login
        current_session = _login(PHONE, psw="123456789")
        self.assertEqual(current_session[1], SUCCESS)

        # Verify_valid_phone_number
        payload = json.dumps({"phoneNumber": PHONE})
        response = current_session[0].post(self.url_resetPassword_available, data=payload, headers=self.headers)
        self.assertEqual(response.status_code, SUCCESS)

        # Try set valid email
        payload1 = json.dumps({"tan": 9999})
        response1 = current_session[0].post(self.url_resetPassword_verify, data=payload1, headers=self.headers)

        # Verify TAN
        self.assertEqual(response1.status_code, SUCCESS)

        # Confirm
        payload2 = json.dumps({"qa": [{"q": 1, "a": "secret answer"}, {"q": 2, "a": "Kontrabas"}]})
        response2 = current_session[0].post(self.url_resetPassword_confirm, data=payload2, headers=self.headers)
        # Verify confrim response
        self.assertEqual(response2.status_code, SUCCESS)

        # Reset password
        payload3 = json.dumps({"password": "123456"})
        response3 = current_session[0].post(self.url_resetPassword_reset, data=payload3, headers=self.headers)

        # Verify confrim response
        self.assertEqual(response3.status_code, SUCCESS)

        # Try login with old password
        current_session = _login(PHONE, psw="123456789")
        self.assertEqual(current_session[1], UNAUTHORIZED)

        # Try login with new password
        current_session = _login(PHONE)
        self.assertEqual(current_session[1], SUCCESS)






if __name__ == '__main__':
    unittest.main(verbosity=2)