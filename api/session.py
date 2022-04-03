# -*- coding: utf-8 -*-
import requests

保存在服务端，一般放在内存中
客户端和服务端通过 SessionID来沟通，一般是较长的随机字符串32或48字节

保持高效会话

s = requests.Session()  #保持会话
