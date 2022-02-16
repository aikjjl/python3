# -*- coding: utf-8 -*-
import json

import json和dict转换
import requests

post请求参数一部分在url里面，另一部分在body里

1，第一种application / json和dict转换, 传json参数
{"i":"xxx","i2":"xxxx","i3":"true"}

2,第二种 application/x-www-form-urlencodeed，传data参数
i=xxx&i2=xxx&i3=fales

3,第三种 multipart、form-data：这是一种表单格式的
文件上传，图片上传等混合式

4，第四种 text/xml



post传json参数
1，传json参数，自动转json
d={"a":1, "b":"c"}
requests.post(url=url, json=d)

2,传data参数
requests.post(url=url,data=json.dumps(d))


