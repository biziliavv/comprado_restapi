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


email_value = time.strftime("%d%m%Y" + "%H%M%S") + "@" + "test.com"
EMAIL = 'biziliavv@gmail.com'
PSW = "123456"
host = '54.93.81.169/api/v1'





if __name__ == '__main__':
    unittest.main()