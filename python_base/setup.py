
'''
 (2) 在文件夹中新建一个setup.py文件
包含有关发布的元数据。如下：
从python发布工具中导入setup这个函数
Python_modules 将模块的元数据与setup函数的参数关联

'''

from distutils.core import setup
setup(
    name='nest',
    version='1.0.0',
    py_modules=['nest'],
    author='jqm',
    author_email='jqm2009@gmail.com',
    url='http://www.headfirstlabs.com',
    description='A simple printer of nested lists',

)