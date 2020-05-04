# -*- coding: UTF-8 -*-
# 用for循环实现1~100求和
# sum = 0
# for x in range(101):
#     sum += x
# print(sum)

# 用for循环实现1~100之间的偶数求和
# 方法一
# sum = 0
# for x in range(2, 101, 2):
#     sum += x
# print(sum)

# 方法二
# sum = 0
# for x in range(1, 101):
#     if x % 2 == 0:
#         sum += x
# print(sum)

# 计算机出一个1到100之间的随机数，
# 玩家输入自己猜的数字，
# 计算机给出对应的提示信息(大一点、小一点或猜对了)，
# 如果玩家猜中了数字，
# 计算机提示用户一共猜了多少次，
# 游戏结束，否则游戏继续。
# import random
# answer = random.randint(1, 100)
# counter = 0
# while True:
#   counter += 1
#   number = int(input('请输入: ')) 
#   if number < answer:
#      print('大一点') 
#   elif number > answer:
#      print('小一点') 
#   else:
#      print('恭喜你猜对了!') 
#      break
# print('你总共猜了%d次' % counter) 
# if counter > 7:
#      print('你的智商余额明显不足')

# 通过嵌套的循环来输出一个九九乘法表。
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('%d*%d=%d' % (i, j, i * j), end = '\t')
#     print()

# 练习1:输入一个正整数判断是不是素数。
# number = int(input('请输入一个正整数: '))
# a =int
# a!= 1
# a!= number
# if (number % a) == 0:
#     print('{}不是素数'.format(number))
# else:
#     print('{}是素数'.format(number))

# from math import sqrt
# num = int(input('请输入一个正整数: ')) 
# end = int(sqrt(num))
# # sqrt() 方法返回数字x的平方根。 
# is_prime = True
# # 程序用变量isprime来表示一个数是否为素数。
# for x in range(2, end + 1):
#     if num % x == 0:
#         is_prime = False
#         break
# if is_prime and num != 1:
#     print('%d是素数' % num) 
# else:
#     print('%d不是素数' % num)


# 练习2:输入两个正整数，计算它们的最大公约数和最小公倍数。
# 12和18的公倍数有：36，72，….其中36是12和18的最小公倍数，记作[12，18]=36。
# 12和18的公约数有：1，2，3，6.其中6是12和18的最大公约数，记作（12，18）=6。

# a = int(input('请输入一个正整数: ')) 
# b = int(input('请再输入一个正整数: ')) 
# for x in range(a):
#     if a % x == 0 and b % x == 0:


x = int(input('x = '))
y = int(input('y = '))
# 如果x大于y就交换x和y的值 
if x > y:
# 通过下面的操作将y的值赋给x, 将x的值赋给y
   x, y = y, x
# 从两个数中较的数开始做递减的循环 
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0: 
       print('%d和%d的最大公约数是%d' % (x, y, factor)) 
       print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor)) 
    break




# 练习3:打印如下所示的三角形图案。
# row = int(input('请输入行数: ')) 
# for i in range(row):
#     for _ in range(i + 1):
#         print('*', end='')
#     print()

# for i in range(row):
#     for j in range(row):
#         if j < row - i - 1:
#             print(' ', end='')
#         else:
#             print('*', end='')
#     print()

# for i in range(row):
#     for _ in range(row - i - 1):
#         print(' ', end='')
#     for _ in range(2 * i + 1):
#         print('*', end='')
#     print()
