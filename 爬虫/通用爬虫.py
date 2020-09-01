print('遵守robots协议')

print("urllib2")
import urllib.request

#构造请求对象
#response = urllib.request.Request("https://www.baidu.com")

#向指定url地址发送请求，返回服务器的类文件对象
response = urllib.request.urlopen("https://www.baidu.com")


html = response.read()

#返回http响应码
print(response.getcode())

#返回实际数据的url，防止重定向问题
print(response.geturl())



print(html)
