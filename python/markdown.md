# 十进制转二进制（递归除以二的余数倒过来就是）
例如：14转二进制：1110
14/2=7余0
 7/2=3余1
 3/2=1余1
 1/2=0余1

二进制转十进制：逆向值乘以逆序的次方
例如:1110.转十进制:14
0*2的0次方等于0
1*2的1次方等于2
1*2的2次方等于4
1*2的3次方等于8
二进制1110等于十进制0+2+4+8就是14
---------------------------------------------------
换行\n
\表示转义 \'等于'
\\表示\
end = ''表示不换行
>>> print('I\'m ok.')
I'm ok.
>>> print('I\'m learning\nPython.')
I'm learning
Python.
>>> print('\\\n\\')
\
\
--------------------------------------------------
浮点数
1.23x109和12.3x108是完全相等的。浮点数可以用数学写法，如1.23，3.14，-9.01，等等。但是对于很大或很小的浮点数，就必须用科学计数法表示，把10用e替代，1.23x109就是1.23e9，或者12.3e8，0.000012可以写成1.2e-5，等等
--------------------------------------------------
布尔值可以用and、or和not运算。（逻辑运算）
and运算是与运算，只有所有都为True，and运算结果才是True：>>> 5 > 3 and 3 > 1	True
or运算是或运算，只要其中有一个为True，or运算结果就是True：>>> 5 > 3 or 1 > 3	True
not运算是非运算，它是一个单目运算符，把True变成False，False变成True：>>> not 1 > 2          True
变量：python是动态变量,      		java是静态变量
a=1;					int a =1;(定义a是整数类型)
a='abc'					a ='abc'(错误，不能把字符串赋值给整数类型a)
print(a)	abc	

a = 'ABC'	执行a = 'ABC'，解释器创建了字符串'ABC'和变量a，并把a指向'ABC'：
b = a		执行b = a，解释器创建了变量b，并把b指向a指向的字符串'ABC'：
a = 'XYZ'	执行a = 'XYZ'，解释器创建了字符串'XYZ'，并把a的指向改为'XYZ'，但b并没有更改：
print(b)	打印出了b=ABC
# string字符串  
例句：str_name = "hello word"
            方法                         #说明
长度        len(str_name)                #计算srt_name出现数量
计数        count("llo")                 #计算srt_value出现数量
位置        str_name.index("llo")        #计算llo索引位置,如果没有llo则报错
print(str_name.isdecimal)               #判断是否数字
print(str_name.startswith('hello'))     #判断开头
print(str_name.endswith('word'))        #判断结尾
print(str_name.replace('h','q'))        #替换

print(str_name.ljust(10))               #左对齐，数字表示空格+字符串数量
print(str_name.rjust())                 #右对齐
print(str_name.center())                #居中
print(format(str_name,'>'))             #格式化左右对齐和居中（> < ^）
---------------------------------------------------- 
函数
字符转整数编码 ord('A')等于65	整数编码转字符 chr(66)等于'A'
len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：
>>> len(b'ABC')
3
>>> len(b'\xe4\xb8\xad\xe6\x96\x87')
6
>>> len('中文'.encode('utf-8'))
6
# 格式化输出
1：format()方法
>>> print("hello {0},股票涨了 {1:.2f}%,你赚了{2} 万" .format('张三',203.124,30))
hello 张三,股票涨了 203.12%,你赚了30 万
2：占位符替换内容
%02d	整数
%.2f	浮点数
%s	字符串
%%	%
>>>print("hello %s,股票涨了 %.2f%%,你赚了%03d 万" %('张三',203.124,30))
hello 张三,股票涨了 203.12%,你赚了30 万
3：f-string
>>> name = '张三'
>>> f1 = 203.124
>>> int_1 = 30
>>> print(f'hello {name},股票涨了 {f1:.2f},你赚了 {int_1} 万')
hello 张三,股票涨了 203.12%,你赚了30 万
----------------------------------------------------------
# 使用list有序可重复集合
classmates = ['Sarah', 'Jack',4,True,'Adam']

len()函数可以获得list元素的个数:len(classmates)	>>5
访问list中每一个位置的元素:classmates[0]		>>Adam
追加元素到末尾：classmates.append('Adam')
元素插入到指定索引位置:classmates.insert(1, 'Jack')
元素替换成别的元素,直接赋值给对应的索引位置:classmates[0] = 'Sarah'
删除list末尾/指定索引的元素:classmates.pop()	classmates.pop(1)
删除指定key：classmates.remove（Adam）
拼接二个list列表：classmates.extend（classmates_2）

要拿到'php'可以写p[1]或者s[2][1]，因此s可以看成是一个二维数组，类似的还有三维、四维……数组，不过很少用到。
注意赋值顺序
p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']
列表功能：     关键字函数方法                    说明
增加         list.insert(索引，数据)     指定位置插入
            list.append(数据)          末尾插入 
            list.extend（list2）       列表2插入列表
修改         list[索引] = 数据          修改指定索引数据      
删除         del list[索引]             删除指定索引数据
            list.remove(数据)          删除第一个出现的指定数据
            list.pop                  删除末尾数据
            list.clear ()               清空列表
统计         len(list)                 列表长度
排序         list.sort()                升序排列
            list.sort(reverse=True)   降序排列
            list.reverse()             逆序/反转
查           list[索引]                 查询
-----------------------------------------------------------

# tuple元组
请问以下变量哪些是tuple类型：
 a = ()
 b = (1)
 c = [2]
 d = (3,)
 e = (4,5,6)
 答案：a,d,e

 可变的”tuple：
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
>>('a', 'b', ['X', 'Y'])
------------------------------------------------------------
# 条件判断if elif else

#if else语句
example2:
age = int(input("请输入年龄:"))
if age >= 18:
	print("已成年，可以上网嗨皮！")
else:
	print("未成年，回家写作业吧！")
print("这句代码什么时候输出？")

example2
根据身高体重计算bmi肥胖值：
height = float(input("身高"))

weight = float(input("体重:"))

bmi = weight/(height*height)

if bmi < 18.5:

    print("bmi: %f 低于18.5：过轻" % bmi)

elif bmi >= 18.5 and bmi <=25:

    print("bmi: %f 18.5-25：正常" % bmi)

elif bmi > 25 and bmi <=28:

    print("bmi: %f 25-28：过重" % bmi)

elif bmi > 28 and bmi <=32:

    print("bmi: %f 28-32：肥胖" % bmi)

else:

    print("bmi: %f 高于32：严重肥胖" % bmi)

循环:计算100内奇数、奇数和
案例1：
n=[]
for i in range(1,100):
    if i%2==1:
        n.append(i)
print (n)
print (sum(n))
案例2：奇数和或者偶数和
n = 0
for i in range(1,100): #可换成 [1,2,3,4,5,6,7,8,9,10-100],(1,100,2)可以求偶数/(1,100,1)可以求偶数
    n = n + i
print(n)
案例3:奇数和
n = 0 
i = 100
while i > 0:
    n = n + i
    i = i -1    #i -2 可以计算偶数和
print(n)
break用法
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')#打印出1~10后，紧接着打印END，程序结束
continue用法1:打印奇数和偶数
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)

continue用法2
i = 0
while i < 10:
    if i == 2:
        i += 1    #代表跳过的数字再加上此数字再继续执行
        continue
    print(i)
    i += 1
print('中止')
>>013456789
while用法1:打印0-9
i = 0 
while i < 10:
    print(i)
    i = i+1
print('中止')
>>0123456789

while用法2:计算1+2+3+...+100:
s = 0 
n = 1
while n <= 100:
    s = s + name
    n = n + 1
print(s)

while用法3:计算1*2*3*...*100的积:
s = 1
n = 1
while n <= 100
    s = s * name
    n = n + 1
print(s)

案例1：打印99乘法表，二个while循环，需要定义变量和计数器
row = 1
while row <= 9:
    col = 1
    while col <= row:
        result = col * row
        print("%s * % s = %s  " % (col,row,result),end = '')
        col += 1
    print("")
    row += 1
案例2：打印99乘法表,for循环+while循环
for row in range(1,10): 
    col = 1
    while col <= row:
        result = col * row
        print("%s * % s = %s  " % (col,row,result),end = '')
        col += 1
    print("")
案例2：打印99乘法表
for row in range(1, 10):
    for col in range(1, i+1):
        print('{}x{}={}'.format(j, i, i*j), end='\t')
    print()
-------------------------------------------
# dict字典（key是唯一索引只能是字符串数字和元祖，value是数据，可重覆）无序对象集合，
dict = {'张三':60,'李四':85,'王五':95}
print(dict['张三'])
>>60    #打印Key，value自动出来
print( dict.get('张三'))
>>60    #打印Key，value自动出来

dict['张三'] = 70
print(dict['张三'])
>>70   #key不可变，value可变，可直接赋值

print('赵六' in dict)   
>>false                 #判断key'是否存在false/None/指定输出
print(dict.get('赵六'))
>>None                  #判断key'是否存在false/None/指定输出
print(dict.get('赵六','没有value'))
>>没有value             #判断key'是否存在false/None/指定输出
dict.pop('王五')
print(dict)
>>{'张三':60,'李四':85}  #删除dict
                    字典                        描述
查询            dict_name['key']
                dict_name.get['key']
插入            dict_name['key'] = value
修改            dict_name['key'] = value
删除            del dict_name
                del dict_name['key']           删除指定key
                dict_name.pop['key']
                dict_name.clear()              清空
拼接             dict_name.update(dict_name2)   拼接字典
遍历            for result in dict_name:
    print(result +':'+ str(dict_name[x]),end='')

## 遍历字典的key,value案例：
dict_name = {'x':'1','y':'2','z':'3'}
for k in dict_name:
    print(k)

for v in dict_name.values():

    print(v)

for k,v in dict_name.items():
    print(k,end='\t')
    print(v)
print(' ')
-----------------------------------------
<font size=10>函数</font>

## 函数百度访问经典例子：
def test1(a):
    a = input('输入访问内容:')
    if a == '百度':
        print('--进入百度')
        test2(2)
def test2(b):
    b = input("输入访问内容:")
    if b == '文库':
        print('--进入文库')
        test3(3)
def test3(c):
    c = input('请输入内容：')
    if c =='诗句':
        print('将进酒诗句')
    elif c == '关闭窗口':
        print('返回百度首页',test1(1))
    
test1(1)
## 案例：测试函数调用，打印字符串次数
def test(char,times):
    row = 0
    while row < 5:
        print(char * times)
        row += 1
test('-',50)
# 函数1：函数可以赋值给变量
def func1(a,b):
    c= a + b
    return (c)      #return告诉调用函数结果
    e = 3           #return下面的代码不会执行并呈现灰色
    
result = func1(2,2) #函数结果需要赋值给一个变量再打印
print(result)
函数2：#定义并调用求绝对值的函数，功能类似abs()
def my_abs(x):
    if x > 0:
        return x
    else:
        return -x
print(my_abs(-2))
函数3：
import math
def my_abs(x):
    if not isinstance(x, (int, float)):   #isinstance函数判断，用法:isinstance（对象或变量,(数据类型)）
        raise TypeError('bad operand 111')#raise+异常名称+（异常原因）
    if x >= 0:
        return x
    else:
        return -x
my_abs(3)
# 函数参数：（二个参数）计算平方，输入一个参数是默认2次方
## 必选参数在前，默认参数在后
def power(x, n=2):  #n=2相当于设置了默认参数,是必选参数在前，默认参数在后，否则Python的解释器会报错
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(3,3))
默认函数参数:这样，大多数学生注册时不需要提供年龄和城市，只提供必须的两个参数：
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
enroll('Sarah', 'F')
name: Sarah
gender: F
age: 6
city: Beijing
默认参数尽量提供给不可变变量防止值错误变化，或者用str，None这个不变对象来实现
由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。
我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。
def add_end(L=[]):
    L.append('END')
    return L
add_end()
['END', 'END']
add_end()
['END', 'END', 'END']
或者用str，None这个不变对象来实现：
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
## 不可变参数案例：不可变参数计算a2 + b2 + c2 + ……。
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
#但是调用的时候，需要先组装出一个list或tuple：
>>> calc([1, 2, 3])
14
>>> calc((1, 3, 5, 7))
84
## 可变参数*args案例：可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个list或tuple
可变参数计算a2 + b2 + c2 + ……。

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
>>> calc(1, 2,4,6,)#实际测试记得用变量接受函数再打印
57
>>> calc()
0
#也可把列表参数加个*号变成可变列表传进去
>>> nums = [1, 2, 3]
>>> calc(nums[0], nums[1], nums[2])#繁琐方法
14
>>> nums = [1, 2, 3]                #简单方法
>>> calc(*nums) 
14

               可变参数*args               关键字参数**kw    
传参个数          0-n个                      0-n个含参数名的参数
传参类型          list/tuple                 dict

## 关键字参数**kw案例：关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
person('Michael', 30)
>>name: Michael age: 30 other: {}
也可以传入任意个数的关键字参数：
person('Bob', 35, city='Beijing',job='Engineer')
>name: Bob age: 35 other: {'city': 'Beijing',job='Engineer'}

关键字参数案例：用户注册功能：要求person函数里接收到name和age这两个必选参数，除了用户名和年龄是必填项外，其他都是可选项
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
user = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])#简化写法person('Jack', 24, **extra)
>>name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}

命名关键字参数限制关键字参数案例：只能输入city和job
def person(name, age, *, city, job):#跟在*后面,或者可变参数*args后面
    print(name, age,*, city, job)
person('Jack', 24, 'xx',city='beijing',job='Engineer')
>Jack 24 'xx' Beijing Engineer

命名关键字参数city具有默认值，缺省值，调用时，可不传入city参数：
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)
person('Jack', 24, job='Engineer')
>Jack 24 Beijing Engineer
## Python中定义函数，可以按顺序用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用,对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的,但不要同时使用太多的组合，否则函数接口的可理解性很差。
比如定义一个函数，包含上述若干种参数：

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
在函数调用的时候，Python解释器自动按照参数位置和参数名把对应的参数传进去。

>>> f1(1, 2)
a = 1 b = 2 c = 0 args = () kw = {}
>>> f1(1, 2, c=3)
a = 1 b = 2 c = 3 args = () kw = {}
>>> f1(1, 2, 3, 'a', 'b')
a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
>>> f1(1, 2, 3, 'a', 'b', x=99)
a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
>>> f2(1, 2, d=99, ext=None)
a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}
最神奇的是通过一个tuple和dict，你也可以调用上述函数：

>>> args = (1, 2, 3, 4)
>>> kw = {'d': 99, 'x': '#'}
>>> f1(*args, **kw)
a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
>>> args = (1, 2, 3)
>>> kw = {'d': 88, 'x': '#'}
>>> f2(*args, **kw)
a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}

可变参数案例1：函数可以接收多个数计算两个数的乘积
def mul(x, *y):
    if y:
        pass 
    else:
        return x
    return x * mul(*y)
可变参数案例2：函数可以接收多个数计算两个数的乘积
def mul(*y):
    r=1
    if len(y)==0:
        raise TypeError
    else:
        for n in y:
            r=r*n
    return r
#测试
print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('测试失败!')
elif mul(5, 6) != 30:
    print('测试失败!')
elif mul(5, 6, 7) != 210:
    print('测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        mul()
        print('测试失败!')
    except TypeError:
        print('测试成功!')
        
  # 递归函数
  案例：计算阶乘n! = 1 x 2 x 3 x ... x n
  def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)#调用一次生成一次栈帧，函数返回就减少一次栈帧，n最高到997会堆栈溢出

    如果我们计算fact(5)，可以根据函数定义看到计算过程如下：
    ===> fact(5)
===> 5 * fact(4)
===> 5 * (4 * fact(3))
===> 5 * (4 * (3 * fact(2)))
===> 5 * (4 * (3 * (2 * fact(1))))
===> 5 * (4 * (3 * (2 * 1)))
===> 5 * (4 * (3 * 2))
===> 5 * (4 * 6)
===> 5 * 24
===> 120
  ## 递归函数优化(防止栈帧溢出)  
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
-------------------------------------------------------------
<font size=10>高级特性</font>

# 列表、元祖和字典高级特性
## 切片
取列表和元祖的指定元素
#常规
L = ['x', 'y', 'z','a']
[L[0], L[1], L[2]]
>>['x', 'y', 'z','a']
#切片
L[0:3]
>>['x', 'y', 'z','a']

L[-1::-1]
['Michael', 'Sarah', 'Tracy']
>>['a', 'z', 'y','x']
## 迭代
### 判断是否可迭代
>>> from collections.abc import Iterable
>>> isinstance('abc', Iterable) # str是否可迭代
True
>>> isinstance([1,2,3], Iterable) # list是否可迭代
True
>>> isinstance(123, Iterable) # 整数是否可迭代
False
### enumerate内置函数打印索引下标和元素值
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
>>
0 A
1 B
2 C
###  enumerate内置函数打印索引下标和元素值，列表内值个数不受限制
a = (['A', 1，11], ['B', '2'，22], ['C', 3，33])
for x, y in enumerate(a):
    print(x, y)
>
0 ['A', 1，11]
1 ['B', '2'，22]
2 ['C', 3，33]
### 可以遍历二个k,v（元祖放进列表）
for x, y in [(1, "x"), (2, 4), (3, 9)]:
    print(x, y)
>
1 x
2 4
3 9
## 字典不能用这个迭代
## 遍历字典的key,value案例：
dict_name = {'x':'1','y':'2','z':'3'}
for k in dict_name:
    print(k)

for v in dict_name.values():

    print(v)

for k,v in dict_name.items():
    print(k,end='\t')
    print(v)
print(' ')

# map求积，reduce求和、整数； reduce+map高阶函数 写出str转int的函数，filter过滤序列求基数、去空格、求素数、求回数（12321）； sorted排序算法求列表字符串字典正反顺序
from functools import reduce
#  map高阶函数，（第一个参数f是函数本身（需1个参数），第二个参数是要遍历的值）
def f(x):
    return x * x
## map（）函数方法遍历
r = map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))
## 传统方法遍历
L = []
for n in [1,2,3,4,5,6,7,8,9]:
    L.append(f(n))
print(L)
## 把这个list所有数字转为字符串：
list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

# 高阶函数
## reduce高阶函数（第一个参数f是函数本身（需2个参数），第二个参数是要遍历的值）
## 序列求和，就可以用reduce实现：
def add(x,y):
    return x + y 
print(reduce(add,[1,3,5,7]))
## reduce高阶函数把列表转整数
def f(x, y):
    return x * 10 + y
reduce(f, [1, 3, 5, 7, 9])
>> 13579

## reduce+map高阶函数 写出str转int的函数
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))
## 还可以用lambda函数进一步简化成：
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

# filter()函数用于过滤序列。
##求基数
def is_odd(n):
    return n % 2 == 1
list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
>>  [1, 5, 9, 15]
##求删除空字符串
def not_empty(s):
    return s and s.strip()
list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
>> ['A', 'B', 'C']
##filter()筛选出回数：
def f1(n):
    str_1 = str(n)
    str_2 = str_1[::-1]
    return str_1 == str_2
r = filter(f1,range(1,10))
if list(filter(f1,range(1,10))) == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print("测试成功")
else:
    print('测试失败')
# sorted排序算法
##求顺序
sorted([36, 5, -12, 9, -21])
>>[-21, -12, 5, 9, 36]
##求绝对值顺序
sorted([36, 5, -12, 9, -21],key=abs)
>>[5, 9, -12, -21, 36]
##求字符串正反排序
sorted(['bob', 'about', 'Zoo', 'Credit'])
>>['Credit', 'Zoo', 'about', 'bob']#以大写为大
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
>>['about', 'bob', 'Credit', 'Zoo']#正序
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
>>['Zoo', 'Credit', 'bob', 'about']#反序
##求按名字排序和按分数排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
def by_score(t):
    return -t[1]
L2 = sorted(L,key=by_name)
print(L2)
L2 = sorted(L,key=by_score,reverse=True)
print(L2)

# 面系对象编程
## 访问限制（__开头）
class student():
    #__开头方法私有且不可访问修改
    def __init__(self,name,score) -> None:
        self.__name = name
        self.__score = score
    #获取私有属性
    def get(self):
        return self.__name
    def get2(self):
        return self.__score
    #修改私有属性
    def set_score(self,name,score):
        self.__name = name
        if 0<= score <=100:
            self.__score =score
        else:
            raise ValueError('bad score')
#实例化对象调用         
bat = student("zs",50)
print(bat.get())
print(bat.get2())
print(bat.set_score("zs",60))
print(bat.get())
print(bat.get2())

# 获取对象数据类型