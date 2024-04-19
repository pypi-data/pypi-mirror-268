#! /usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import setuptools
import time
from rogue_tools import path_tool,file_tool
path_tool.del_('build')
path_tool.del_('dist')
path_tool.del_('rogue_tools.egg-info')
path_tool.copy(r'C:\Users\luohao\AppData\Local\Programs\Python\Python310\Lib\site-packages\rogue_tools',r'D:\project\test_tools\rogue_tools_for_pip\rogue_tools',is_cover=True)
lines = file_tool.read_simple_text2('version.txt').split('.')
now_version = f'{lines[0]}.{lines[1]}.{int(lines[2])+1}'
file_tool.write_str('version.txt',now_version,'w+')
time.sleep(1)


setup(
    name='rogue_tools',  # 包的名字
    author='luohao',  # 作者
    version=now_version,  # 版本号
    license='MIT',

    description='private tools',  # 描述
    long_description='''long description''',
    author_email='luohao@aobi.com',  # 你的邮箱**
    url='',  # 可以写github上的地址，或者其他地址
    # 包内需要引用的文件夹
    # packages=setuptools.find_packages(exclude=['url2io',]),
    packages=["rogue_tools"],
    # keywords='NLP,tokenizing,Chinese word segementation',
    # package_dir={'jieba':'jieba'},
    # package_data={'jieba':['*.*','finalseg/*','analyse/*','posseg/*']},

    # 依赖包
    install_requires=[
        'openpyxl >= 3.0.10',
        "requests >= 2.28.1",
        "matplotlib >= 3.7.0",
        "tqdm >= 4.64.1",
		"PyYaml >= 5.3",
		"lz4 >= 4.3.2",
    ],
    classifiers=[
        # 'Development Status :: 4 - Beta',
        'Operating System :: Microsoft',  # 你的操作系统  OS Independent      Microsoft
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        # 'License :: OSI Approved :: BSD License',  # BSD认证
        'Programming Language :: Python',  # 支持的语言
        'Programming Language :: Python :: 3',  # python版本 。。。
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries'
    ],
    zip_safe=True,
)