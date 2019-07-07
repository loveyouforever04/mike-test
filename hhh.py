# -*- coding: UTF-8 -*-

# Filename : 05-if.py
# author by : （学员lisa)

# 目的:
# 掌握使用 if 语句
#导入random（随机数）模块
import random

#print("---开始出题目---")
#用'w'方式新建一个结果文件

file1 = "小学数学卷.txt"
f1 = open(file1, 'w')  # write 方式第一次写一行
text2write1 = "---开始出题目-无答案--\n"
f1.write(text2write1)
f1.close()
#用'a'方式打开文件，准备追加数学题
#filename = "小学数学卷.txt"

file2 = "小学数学卷答案.txt"
f2 = open(file2, 'w')  # write 方式第一次写一行
text2write2 = "---开始出题目-有答案--\n"
f2.write(text2write2)
f2.close()

#嘎嘎嘎嘎嘎
f1=open(file1,"a")
f2=open(file2,"a")
rows=20
columns=5
count=0
#最简单的for
for row in range(1,21):
     line1 = ''
     line2 = ""
     for col in range(1,6):
        count=count+1

        #随机生成2个0-99之间的整数
        a= random.randint(1, 100)
        b= random.randint(1, 100)

        #随机生成运算符
        op = random.randint(1,4)
        # debug


        #当op=1时加法
        if op == 1:
               line1 +=  "%d + %d=\t\t\t" % (a, b)
               answer=a+b
               line2 +=  "%d + %d=%d\t\t\t" % (a, b,answer)
        #print(line1)

        #当op=2时减法
        if op ==2:
            if a >=b:
                line1 +=  "%d-%d=\t\t\t" % (a, b)
                answer=a-b
                line2 += "%d - %d=%d\t\t\t" % (a, b,answer)
            else:
                line1 +=   "%d-%d=\t\t\t"%(b,a)
                answer=b-a
                line2 += "%d - %d=%d\t\t\t" % (b,a,answer)
        #print(line1)
        #当op=3时乘法

        if op ==3:
                line1 +=  "%d*%d=\t\t\t"%(a, b)
                answer=a*b
                line2 +=  "%d * %d=%d\t\t\t" % (a,b,answer)
        #print(line1)
        #当op=4时除法

        if op ==4:
            if a==0 and b!=0:
                line1=line1+"%d/%d=\t\t\t"%(a, b)
                answer=a/b
                line2 +="%d / %d=%0.2f\t\t\t" (a,b,answer)

            if a==0 and b==0:
                b=random.randint(1,99)
                line1=line1+"%d/%d=\t\t\t"%(a, b)
                answer=a/b
                line2 +="%d / %d=%0.2f \t\t\t" (a,b,answer)
        else:
                line1=line1+"%d/%d=\t\t\t"%(a, b)
                answer=a/b
                line2 +="%d / %d=%0.2f \t\t\t"% (a,b,answer)

        #print(line1)


     #print("第{0}行，第{1}列的第{2}道数学题\t\t\t".format(row,col,count))
     #print(line1)
     text2write1 = line1+'\n'
     f1.write(text2write1)

     #print("\n")
     text2write2 = line2+'\n'
     f2.write(text2write2)

#print("结束   （100）四则运算")
#print('---结束{0}道四则运算---'.format(count))
text2write1 = "---总共出了{0}道数学题---\n".format(count)
f1.write(text2write1)

text2write2 = "---结束---总共出了{0}道四则运算(含答案)---\n".format(count)
f2.write(text2write2)

f1.close()
f2.close()
