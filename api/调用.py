# -*- coding: utf-8 -*-
import requests
import time
import re

import requests
import json

github_url = "http://appdev.open.oa.com"
data = json.dumps({'name': 'test', 'no': '111'})
r = requests.post(github_url, data, auth=('user', '*****'))
print(r.json)
