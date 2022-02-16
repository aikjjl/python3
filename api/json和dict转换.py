# -*- coding: utf-8 -*-
import json
字典是无序的
#字典转json
d={}
d={"a":1,"b":"c"}
js = json.dumps(d)
print(js)
print(type(js))

#json转dict
print(json.loads(js))
print(type(js))

json解析
r=r.content #字节输出，str类型
r=r.json() #解析json，dict类型


url编码
import urllib
a="哈哈"
print(urllib.quote(a))
requests自动将url里的中文转码

解码
print(urllib.unquote(a))
