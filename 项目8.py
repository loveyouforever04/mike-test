# -*- coding: UTF-8 -*-

# Filename : 05-if.py
# author by : （学员lisa)

# 目的:
# 掌握使用 if 语句
#导入random（随机数）模块
import random
print("\n----华丽分割线----")
a=float(input("输入三角形第一边长 a=: "))
b=float(input("输入三角形第二边长 b=: "))
c=float(input("输入三角形第三边长 c=: "))
if (a+b>c)and(a+c>b)and(b+c>a):
    if(abs(a-b)>c)or(abs(a-c)>b)or(abs(b-c)>a):
       pass
else：
    print("错误！某两边之差大于第三边，所以无法组成三角形.")
elif:
    if(a==b)or(b==c)or(a==c)
    print("正确，可以组成等边或等腰三角形")
else：
    print("正确，可以组成不等边三角形")
else：
    print("错误！某两边之和小于第三边，所以无法组成三角形")
