ip_dic = {"192.168.88.101:8083": "x86_1",
          "192.168.88.102:8083": "x86_2",
          "localhost:8002": "x86_1",
          "192.168.88.202:8083": "x86_1"}

key_li = ip_dic.keys()
print(key_li)
va_li = ip_dic.values()
print(va_li)
x = zip(va_li,key_li)
print(dict(x))

print(type({1,2}))