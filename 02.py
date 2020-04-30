import math
radius = float(input('请输入圆的半径: '))
c = 2*math.pi*radius
d = math.pi*radius**2
print (c,d)



# -*- coding: UTF-8 -*-
# year = int(input("请输入年份: "))
# if (year % 4) == 0:
#    if (year % 100) == 0:
#        if (year % 400) == 0:
#            print("{0} 是闰年".format(year))   # 整百年能被400整除的是闰年
#        else:
#            print("{0} 不是闰年".format(year))
#    else:
#        print("{0} 是闰年".format(year))       # 非整百年能被4整除的为闰年
# else:
#    print("{0} 不是闰年".format(year))

year = int(input("请输入年份: "))
if (year % 4) == 0 and (year % 100)!= 0 or (year % 400)==0:
   print("{}是闰年".format(year))
else:
   print("{0} 不是闰年".format(year))
# print(type(year))

# year = input("请输入年份: ")
# print(type(year))
