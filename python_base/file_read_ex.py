'''
  Python中的基本输入机制是基于行的，从个文本文件向程序读入数据时，一次会到达一个数据行。
'''
import os

print()
print()
print(os.getcwd())
# os.chdir('../python3/')
# print(os.getcwd())

data = open('test.txt')
'''
print(data.readline(),end='')
data.seek(0) # 回到文件起始位置
print(data.readline(),end='')
'''

# for each_line in data:
# 	print(each_line,end='')
#
#
# data.close()   # 处理完一定要关闭

# split()
'''
for each_line in data:
    # (role,line_spoken)=each_line.split(":") #不符合则报错
    (role, line_spoken) = each_line.split(":", 1) #只分解2部分

    print(role,end='')
    print('---said---: ',end='')
    print(line_spoken,end='')
    
'''

# method help
# print(help(each_line.split))

# 查找字串find()
# Find()查找一个字符串的子串，并返回索引位置，找不到就返回-1.
each_line = "hello:world"
# print(each_line.find(':'))

'''
for each_line in data:
    if not each_line.find(':') == -1:   # not关键字取反
        (role, line_spoken) = each_line.split(':', 1)
        print(role, end='')
        print('----said---- ', end='')
        print(line_spoken, end='')

'''

'''
  exception 
  放过错误：pass（空语句，或null）
'''

if os.path.exists('test1.txt'):  # exists

    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            print(role, end='')
            print(' said: ', end='')
            print(line_spoken, end='')
        except:
            # pass
            print(each_line)
    data.close()
else:
    print('The data file is missing!')


# catch exception指定异常

try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':')
            print(role, end='')
            print(' said ', end='')
            print(line_spoken, end='')
        except ValueError:
            pass
    data.close()
except IOError:
    print('The datafile is missing!')

'''
Open() BIF 打开一个磁盘文件，创建一个迭代器从文件读取数据，一次一行。
readline()方法从一个打开的文件中读取一行数据。
seek()方法可以用来将文件“退回“到起始位置。
close()关闭一个之前打开的文件。
split()将一个字符串分解为一个子串列表。
Python中不可改变的常量列表：元组（tuple）。
ValueError：数据不符合期望的格式出现时的错误类型。
IOError：数据无法正常访问时出现的错误类型。
help()BIF
find() 方法会在一个字符串中查找一个特定子串。
not关键字将一个条件取反。
try/except语句提供了一个异常处理机制，从而保护可能导致运行时错误的某些代码行。
pass语句就是Python的空语句或null语句，什么都不做。
'''