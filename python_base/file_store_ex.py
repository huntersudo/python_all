'''
数据保存到文件
'''

man = ['abc', 'cde']
other = ['abc', 'cde']

try:
    data = open('file/sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()  # strip方法从字符串中去除空白符
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':  # elif  代表elseif
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The datafile is missing!')

print(man)
print(other)

print('#########read done#######################')

'''
写模式打开文件
Open()打开磁盘文件，指定访问模式，默认r模式，读，
访问模式：
w: 打开指定的文件，如果已经存在，将会被清空内容。
a: 追加到一个文件。
w+：打开，一个文件来完成写和读（不清除）。
若文件不存在，会自动创建。

读文件时，还好，异常，但是数据仍然在文件中，问题不大。
写文件时，麻烦了
'''

try:
    man_file = open('file/man_data.txt', 'a')
    other_file = open('file/other_data.txt', 'a')
    # 写模式，打开，赋至一个文件对象
    print(man, file=man_file)
    print(other, file=other_file)
# print将指定的列表保存到指定的磁盘文件
except IOError:
    print('File error.')

finally:
    if 'man_file' in locals():  # 数据文件对象并未创建，这样就不可能在数据对象上调用close方法
        man_file.close()
    if 'other_file' in locals():
        other_file.close()

print('##############write done##################')



'''
Python中的字符串是不可变的。
元组：不可变的列表
另外，所有数值类型都是不可变得

locals( )  BIF会返回当前作用域中定义的所有名的集合。
这里会在locals（）BIF 返回的集合中搜索字符串data,如果找到，可以认为文件已经成功打开。
'''


# print exception
try:
    data = open('missing.txt')
    print(data.readline(), end='')
except IOError as err:
    print('File error ：' + str(err))  # str 把异常对象转换为字符串
    # print('File error ：' + err)
finally:
    if 'data' in locals():
        data.close()

print('######### print exception #############')

'''
Try/except/finally模式常用，所以Python提供了一个语句来抽象出相关的一些细节
对文件使用with语句时，大大减少代码量。不需要使用finally组来处理文件的关闭
With会完成关闭文件的任务 ,类似java 7的 try()
With语句使用了一种名为上下文关系协议（context management protocol）的Python技术
'''
try:
    with open('file/man_data1.txt', 'w') as man_file, open('file/other_data2.txt', 'w') as other_file:
        # 两个with语句合并到一起
        print(man, file=man_file)
        print(other, file=other_file)
except IOError as err:
    print('File error: ' + str(err))

print('######### with ###################')

'''
标准输出：sys.stdout
向print_lol函数增加第四个参数，标识把数据写入到哪个位置，缺省sys.stdout

Q

'''
import sys

def print_lol(the_list, indent=False, level=0, fh=sys.stdout):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level+1, fh)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t", end='', file=fh)


try:
    with open('file/man_data1.txt', 'w') as man_file, open('file/other_data2.txt', 'w') as other_file:
        # 两个with语句合并到一起
        print_lol(man, fh=man_file)
        print_lol(other, fh=other_file)
except IOError as err:
    print('File error: ' + str(err))