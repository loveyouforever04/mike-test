import random
List1 = ['张飞','赵云','马超','吕布']
tup1  = ('刘备','曹操','孙权')

pos = 0
value = List1[pos]
print("取出列表的第%d个值,它是%s"%(pos,value))
print('输出列表中所有元素')
pos = 0
for v in List1:
    print("取出列表的%d个值，它是%s"%(pos , v))
    pos = pos+1
print('\n---cutting line4---')
newvalue = '关羽'
List1[0] = newvalue
print("---输出更新后的列表中所有元素")
pos = 0
for v in List1:
    print("取出列表的%d个值，它是%s"%(pos , v))
    pos = pos+1
print('\n---cutting line5---')
newvalue = '关羽'
tup1[0] = newvalue
print("---输出更新后的列表中所有元素")
pos = 0
for v in tup1:
    print("取出列表的%d个值，它是%s"%(pos , v))
    pos = pos+1
print('\n---cutting line6---')
for i in range(1,5):
    #fbb
    s = random,choice(List1)
    print(s
    #fbe
