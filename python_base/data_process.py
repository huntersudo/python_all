'''

不同格式，编码，转换，高效处理
'''

# strip()方法可以从字符串中去除不想要的空白符。
print('=======strip=====')
import os

os.chdir('E:\PycharmProjects\python-all\python_base')
with open('file/data_p1.txt') as jaf:
    data = jaf.readline()
james = data.strip().split(',')  # 将数据转换为一个列表
print(james)
'''
data.strip().split(‘,’) 方法串链（method chaining）
strip应用到data中的数据行，去除字符串中所有不想要的空白字符。
Split创建一个列表，赋至标识符。

'''

# sort提供原地排序。

# sorted 支持复制排序
print("=======sort=====")
data = [6, 5, 4, 3, 2, 1]
data2 = sorted(data)
data.sort()
print(data)


data = [6, 5, 4, 3, 2, 1]
data2 = sorted(data)
print('data2 copy sort:'+str(data2))
print('data same:'+str(data))

'''
创建函数sanitize(),
这个函数处理字符串，找到所有的短横线或者冒号，替换为一个点号。
'''
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)
    (mins, secs) = time_string.split(splitter)
    return (mins + '.' + secs)

with open('file/data_p2.txt') as jaf:
    data3 = jaf.readline()
    print('=====sanitize===')
    print(sanitize(data3))