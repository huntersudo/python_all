'''
转换列表(列表推导，list comprehension)
'''

mins = [1, 2, 3]
secs = [m * 6 for m in mins]
print(secs)

lower = ['i', 'little', 'hello']
feet = [s.upper() for s in lower]
print(feet)

'''
过程式，函数式，面向对象的开发代码方法，Python中都支持
'''
# 集合

distances = set()

# 分片： 从一个列表访问多个列表项
min2 = [1, 2, 3, 4, 5, 6]
print(min2[1:4]) #[2, 3, 4]
