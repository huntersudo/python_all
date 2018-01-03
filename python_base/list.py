
# python的变量标识符没有类型
#  标识符只是名字，可以指示某个数据类型的数据对象
#

"""
cast = ['cheese', 'plain', 'jones', 'Idle']
print(len(cast))
print(cast[1])
cast.append("Gilliam")
print('after append')
print(cast)
# cast.remove("hello")
cast.remove("Gilliam")
print("after remove")
print(cast)
# (location,item)
cast.insert(0,"hello")
print('after insert:')
print(cast)
cast.extend(["Gilliam", "hello"])
print('after extend')
print(cast)
"""

#
# 在列表中混合不同的数据类型

"""
movies = ["hello", 1, "world", 2, "apache", 3]
# tab 缩进
# for each_item in movies:
#     print(each_item)

# while
count = 0
while count < len(movies):
    print(movies[count])
    count = count+1

"""

"""
列表能做的事情要比数组多很多
列表支持伸缩，如果访问一个并不存在的数据项,会提示Index error，表示“越界”
单引号，双引号都可以表示字符串
Python区分大小写：msg和MSG代表不同的名字
"""

# 在列表中存储列表

movies = ["hello", 1975, ["tom", 1988, "hello"], "apache", 1988]

# print(movies[2][0])
"""
# For循环只打印外列表的各个数据项
for each in movies:
    print(each)
"""

# 显示嵌套列表

"""
for each in movies:
    if isinstance(each, list):
        for each2 in each:
            print(each2)
    else:
        print(each)
"""

"""
isinstance 检查某个标识符是否包含某个特定类型的数据
Python3中大约70多个BIF
键入 dir(__builtins__)   （前后分别两个下划线）可以看到Python提供的内置方法列表
关于某个内置BIF是干什么的，比如print,是输入help(print)
大量的BIF意味着可以少些代码,还有丰富的第三方库
"""


print(isinstance(movies, list))

"""
如果有三层嵌套是甚至更多
解决之道：递归
Python3默认递归深度不能超过100，可以修改深度上限
"""

def print_lol(the_list):
    for each1 in the_list:
        if isinstance(each1, list):
            print_lol(each1)
        else:
            print(each1)
# use function
print_lol(movies)

# Python使用缩进将 语句 归组在一起
