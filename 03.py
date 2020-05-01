# 练习2:百分制成绩转换为等级制成绩。
# 如果输入的成绩在90分以上(含90分)输出A;
# 80分-90分(不含90分)输出B;
# 70分-80分(不含80分)输出C;
# 60分-70分(不含70分)输出D;
# 60分以下输出E
x = float(input('请输入成绩: ')) 
if x > 90:
   print('A')
elif x >= 80:
   print('B') 
elif x >= 70:
   print('C') 
elif x >= 60:
   print('D') 
else:
   print('E')
   
   
# -*- coding: UTF-8 -*-
# 练习3:输入三条边长，如果能构成三角形就计算周长和面积。
# 说明: 上面使用的通过边长计算三角形面积的公式叫做海伦公式。
a = float(input('请输入最长边长1: ')) 
b = float(input('请输入中间边长2: ')) 
c = float(input('请输入最短边长3: ')) 
if a > b and a > c:
    x = a
    y = b
    z = c
elif b > c:
    x = b
    y = a
    z = c
else:
    x = c
    y = a
    z = b
print ('最长边 = %.f' % (x))

# 两种写法：
# ('最长边 = %.f' % (max))
# ("{}是闰年".format(year))

if y+z > x:
    c = x+y+z
    d = (x+y+z)/2
    p = d*(d-x)*(d-y)*(d-z)
    p_sqrt = p**0.5
    print ('三角形周长 = %.4f' % (c))
    print ('三角形面积 = %.4f' % (p_sqrt))
else:
    print ('无法构成三角形')
