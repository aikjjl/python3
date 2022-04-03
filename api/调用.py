# -*- coding: utf-8 -*-
import requests
import time
import re

import requests
import json和dict转换

github_url = "http://appdev.open.oa.com"
data = json和dict转换.dumps({'name': 'test', 'no': '111'})
r = requests.post(github_url, data, auth=('user', '*****'),verify=False) #verify是ssl证书
r = requests.get(github_url, data, auth=('user', '*****'))
print(r.json)
r.content #返回内容
r.text #返回文本内容
r.encoding #编码
r.status_code #状态码
r.headers #请求头
