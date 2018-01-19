'''

pickle.dump,load
标准库pickle，可以保存加载几乎任何Python数据对象，包括列表
Dump保存出数据，load恢复数据，必须以二进制访问模式打开这些文件。
'''

import pickle
# wb,rb，二进制模式
with open('file/man_data_dump.txt','wb') as mysavedata:
    pickle.dump([1, 2 ,'three'] , mysavedata,)

# dump 保存,数据
with open('file/man_data_dump.txt' , 'rb') as myrestoredata:
    a_list=pickle.load(myrestoredata)

# load恢复数据
print(a_list)
# 一旦数据恢复到程序中，就可以像其他对象一样处理

'''
不可变类型：Python中的一些数据类型，一旦赋值，不可改变。
腌制-------：将数据对象保存到一个持久存储的过程。（二进制方式保存，不可读）
解除腌制---:从持久存储中恢复一个已保存的数据对象的过程。
 
Strip()方法可以从字符串中去除不想要的空白符。
Print() BIF的file参数控制将数据发送/保存到哪里。
Finally总会执行，
向except组中传入一个异常对象，并使用as关键字赋至一个标识符。
Str() BIF可以用来访问任何数据对象（支持串转换）的串表示，
Locals() BIF返回当前作用域中的变量集合。
In 操作符用于检查成员关系
With语句会自动处理所有已打开文件的关闭工作，即使出现异常也不列外，使用as关键字。
Sys.stdout标准输出，
Pickle模块，高效地将Python数据对象保存到磁盘以及从磁盘恢复。
 
'''