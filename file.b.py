# -*- coding: UTF-8 -*-

# Filename : 04-file.py
# author by : （学员ID)

# 目的:
# 掌握文件的打开、写入、读取

import os

# 指定要读的文件名
filename = "test.txt"

# 读文件
f = open(filename, 'r') # readonly 方式读文件

print("第一个文件内容如下：")
text4read = f.read()
print(text4read)

f.close()
