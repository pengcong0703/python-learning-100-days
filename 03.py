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
