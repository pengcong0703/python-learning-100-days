# -*- coding:utf-8 -*-
# 任务1：读取文件中的第一列，找出其中的完美数，参考例子1

f = open('data_day05.txt', 'r')  # open file
lines = f.readlines()

for line in lines:
    line = line.strip('\n')  # 删除换行符
    line = line.split('\t')  # 打开文件可以看到每一行有两个数字，数字之间使用tab键隔开的，程序里面用'\t'表示
    num0 = line[0]  # 按照'\t'分割之后， line[0]表示第1个数字，加上int,将原来字符串类型转换成int
    num0 = int(num0)
    # print(num0)  # 取消注释可以查看数值
    # print(type(num0))  # 取消注释可以数据类型
    # exit(0)  # 取消注释，程序读取一行数字推出，适合在循环语句中调试
    # 判断第一个数字是否为水仙花数字，是的话print出来
    # 在下面写上你的代码，参考经典例子1
    low = num0 % 10
    mid = num0 // 10 % 10
    high = num0 // 100
    if num0 == low ** 3 + mid ** 3 + high ** 3:
       print(num0)

# -*- coding:utf-8 -*-
# 任务2：读取文件中的第2列，反转数字，参考例子1

f = open('data_day05.txt')  # open file
lines = f.readlines()

for line in lines:
    line = line.strip('\n').split('\t')  # 删除换行符，按照'\t'分割，可以连着写
    num1 = int(line[1])  # 按照'\t'分割之后， line[1]表示第2个数字，加上int,将原来字符串类型转换成int
    # 将数字num1进行反转，并print出来，参考例子1
    # 在下面写上你的代码
    # print(num1)
    # print(type(num1))

    # reversed_num = 0
    # while num1 > 0:
    #     reversed_num = reversed_num * 10 + num1 % 10
    #     num1 //= 10
    # print(reversed_num)

    # i+=1  等于i=i+1

    low = num1 % 10
    mid = num1 // 10 % 10
    high = num1 // 100
    # print(low)
    n = "{}{}{}".format(low,mid,high)
    print(int(n))
    
   
   # -*- coding:utf-8 -*-
# 任务3：找出第一个数字和第二个数字和为1065的数字

f = open('data_day05.txt')  # open file
lines = f.readlines()

for line in lines:
    line = line.strip('\n').split('\t')  # 删除换行符，按照'\t'分割
    # 将数字计算num1和num2的和，如果为1065那么print num1以及num2,否则继续
    # 在下面写上你的代码
    num0 = int(line[0])
    num1 = int(line[1])
    # print(num0,num1)
    if num0 + num1 == 1065:
        print(num0,num1)


# -*- coding:utf-8 -*-
# 任务4：输出100以内所有的素数。素数指的是只能被1和自身整除的正整数（不包括1），可以查资料，百度上很多
from math import sqrt
# num = int(input('请输入一个正整数: ')) 

for num in range(1,101):
    end = int(sqrt(num))
    is_prime = True
    for x in range(2, end + 1):
    # for x in range(2, num):
        if num % x == 0:
            is_prime = False
            # break
    if is_prime and num != 1:
        print('%d是素数' % num) 
    # else:
    #     print('%d不是素数' % num)

# 问题：集体往右移动的快捷键是什么
