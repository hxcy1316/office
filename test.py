d = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5}
if 2 in d:
    print("value")
if 'two' in d:
    print("key")
if ('two', 2) in d:
    print("kv")
# 成员检测检测的是key内容
print(d)
print(d['one'])
del(d['one'])
print(d)
#dict字典遍历，按key值访问
d = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5}
for k in d:
    print(k, d[k])
print('*' * 50)
for k in d.keys():
    print(k, d[k])
print('*' * 50)
for v in d.values():
    print(v)
print('*' * 50)
for k,v in d.items():
    print(k, '---', v)
print('*' * 50)
#dict字典生成式
d = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5}
dd = {k:v for k,v in d.items()}
print(dd)
print('*' * 50)
#加限制条件生成式
ddd = {k:v for k,v in d.items() if v % 2 == 0}
print(ddd)
print('*' * 50)
#dict字典相关函数
#通用函数 len(),max(),mini(),dict()
#str(字典) 返回字典的字符串格式
print(str(d))
print('*' * 50)
# clear: 清空字典
# item: 返回字典的键值对组成的元祖格式
i = d.items()
print(type(i))
print(i)
# keys: 返回字典的键组成的一个结构
k = d.keys()
print(type(k))
print(k)
# values: 返回字典的值组成的一个可迭代的结构
v = d.values()
print(type(v))
print(v)
# get: 根据指定键返回相应的字典值，好处是：可以设置默认值
print(d.get("on333"))
# fromkeys: 使用指定的序列作为键，使用一个值作为字典的所有键的值
l = ['1', '2', '3', '4']
d1 = dict.fromkeys(l, "nihao")
print(d1)