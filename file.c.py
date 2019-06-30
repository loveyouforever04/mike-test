# -*- coding: UTF-8 -*-

# Filename : 04-file.py
# author by : （学员ID)

# 目的:
# 掌握文件的打开、写入、读取

import os

# 指定要读的文件名
filename = "test.txt"

# 向文件追加内容
f = open(filename, 'a') # append 方式读文件

text2write = "这是追加的内容，看到我了吧！\n"
f.write(text2write)

f.close()
