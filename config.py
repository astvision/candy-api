# -*- coding: utf-8 -

import os

PATH_ROOT = os.path.dirname(os.path.realpath(__file__))
PATH_LOG = os.path.join(PATH_ROOT, 'candy.log')

CANDY_API_HOST = 'api address'
CANDY_API_PORT = 8060
CANDY_API_USERNAME = 'api username'
CANDY_API_PASSWORD = 'api password'
CANDY_API_CERTFILE = os.path.join(PATH_ROOT, 'cert', 'candy_cert.pem')
CANDY_API_KEYFILE = os.path.join(PATH_ROOT, 'cert', 'candy_key_nopass.pem')
