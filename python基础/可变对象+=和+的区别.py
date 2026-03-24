a = [1,2,3]
b = a
c = a[:]

print(id(a) == id(b))    #True   调用 __iadd__，原地修改原对象内容
print(id(a) == id(c))    #False   调用 __iadd__，原地修改原对象内容

a += [4,5]    #原地加法，不改变

print(id(a) == id(b))


a = a + [1]
print(id(a) == id(b))   #Fasle     调用 __add__，新建对象并赋值给 a