"""
模块就是一个包含Python代码的文本文件
三重引号建立多行注释
分号“;”用于把多行代码放在一行中,不过最好不要这么做
“#” 开始到这一行结束：都是注释
"""

"""
List()          工厂函数，创建一个新列表
Range()        返回一个迭代器，根据需要生成一个指定范围的数字列表，
Enumerate()      创建成对数据的一个编号列表，从0开始，
Int()           将一个字符串或一个数，转换为一个整数（如果可行)
Id()           返回一个python对象的唯一标识
Next()        返回一个可迭代数据结构（如列表中）的下一项 
 """

# for num in range(4):
#     print(num)

# 修改nest.py 让嵌套列表缩进指定数目的制表符

def print_lol(a_list, level = 0):
    for each_item in a_list:
        if isinstance(each_item, list):
            print_lol(each_item, level+1)
        else:
            for tab_stop in range(level):
                print("\t", end='')
            print(each_item)

# 这个提供了可选参数：level=0
# def print_lol(a_list, level=0)
# 这样支持不同的签名

# 需要缩进时，true，否则false
def print_lol2(a_list, indent=False, level=0):
    for each_item in a_list:
        if isinstance(each_item, list):
            print_lol2(each_item, indent, level + 1)
        else:
            if indent:
                for l in range(level):
                    print("\t", end='')
            print(each_item)


movies = ["hello", 1975, ["tom", 1988, "hello"], "apache", 1988]
print_lol(movies)
print_lol(movies,4)
print_lol2(movies)
print_lol2(movies,True)

""" 
使用三重引号字符串""" """可以在代码中加入一个多行注释。
Python内存中的名字就存放在”命名空间“中，
Python的主命名空间名为_main_

模块是一个包含Python代码的文本文件。
发布工具允许将模块转换为可共享的包。
Setup.py程序提供了模块的元数据，用来构建/安装/上传打包的发布。
#单行注释。
From module import function 形式可以从一个模块将函数专门导入到当前命名空间，
内置函数（built-in-functions,BIF）有自己的命名空间，__builtins__，自动包含在每一个Python程序中。
Range()BIF与for结合使用，从而可以迭代固定次数。
包含end=’’作为print语句的一个参数会关闭默认行为(即在输入中自动包含换行)
为函数参数提供一个缺省值，这个参数就是可选的。
"""