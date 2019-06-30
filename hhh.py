# -*- coding: UTF-8 -*-

# Filename : 05-if.py
# author by : （学员lisa)

# 目的:
# 掌握使用 if 语句
#导入random（随机数）模块
import random

#print("---开始出题目---")
#用'w'方式新建一个结果文件
filename = "小学数学卷.txt"
f = open(filename, 'w')  # write 方式第一次写一行

text2write = "---开始出题目-888--\n"
f.write(text2write)
f.close()
#用'a'方式打开文件，准备追加数学题
#filename = "小学数学卷.txt"

f = open(filename, 'a')  # append 方式读文件
text2write = "888888\n"
f.write(text2write)
#嘎嘎嘎嘎嘎

count=0
#最简单的for
for row in range(1,21):
     line1 = ''
     for col in range(1,6):
        count=count+1

        #随机生成2个0-99之间的整数
        a= random.randint(0, 99)
        b= random.randint(0, 99)

        #随机生成运算符
        op = random.randint(1,4)
        #当op=1时加法
        if op == 1:
            line1 = line1 + "%d + %d=\t" % (a, b)

        #print(line1)
        #当op=2时减法
        if op ==2:
            line1=line1+"%d-%d=\t"%(a, b)
        #print(line1)
        #当op=3时乘法
        if op ==3:
            line1=line1+"%d*%d=\t"%(a, b)
        #print(line1)
        #当op=4时除法
        if op ==4:
            line1=line1+"%d/%d=\t"%(a, b)
        #print(line1)


     #print("第{0}行，第{1}列的第{2}道数学题\t\t\t".format(row,col,count))
     #print(line1)
     text2write = line1+'\n'
     f.write(text2write)
     #print("\n")

#print("结束   （100）四则运算")
#print('---结束{0}道四则运算---'.format(count))
text2write = "---总共出了{0}道数学题---\n".format(count)
f.write(text2write)

f.close()
