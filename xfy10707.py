import random
print('\n---cutting line1---')
for i in range(1,3):
    #fbb
    password = random.randint(0,9999)
    print('Password is : %04d'%(password))
    #fbe
print('\n---cutting line2---')
nums = ('0','1','2','3','4','5','6','7','8','9')
password = []
for i in range(1,5):
    #fbb
    password.append(random.choice(nums))
    # DEBUG
    print('debug - Password list changing : %s'%(password))
    #fbe
# DEBUG
print('debug - list of password = %s'%(password))
#顺序取出所有数字组成最终密码
print('Password is :',end='')
for item in password:
    print('%s'%(item),end='')




char1 = ['0','1','2','3','4','5','6','7','8','9']
char2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
char3 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
char4 = ['~','!','@','#','$','%','^','&','*','(',')','_','+','-','=','{','}','[',']',':','"',';','<','>','?',',','.','/']
#合并到
charA11 = char1  + char2 + char3 + char4
## DEBUG:
print('\ndebug-All usable chars :%s' % (charA11))
#定义密码长度
pwdLen = 8
 #初始化
password  = []
for i in range(1,pwdLen ):
    #fbb
    password.append(random.choice(charA11))
    ## DEBUG:
    print('debug -Password list changing : %s'%(password))
    #fbe
# DEBUG
print('debug - list of password = %s'%(password))

#顺序取出所有数字组成最终密码
print('Password is :',end='')
for item in password:
    print('%s'%(item),end='')
