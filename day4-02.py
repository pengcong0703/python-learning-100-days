# -*- coding: UTF-8 -*-
f = open('table.txt','r')  
lines = f.readlines()
print(lines)
# exit()

# 读取全部内容  
for line in lines: 
    line = line.strip('\n')
    print (line+','+str(1)+'\n')

# for i in range(10)
#     print(i)

# 搜索
# （1）python 读txt文件，
# （2）python 逐行读取文件；
# （3）python 字符串相加；
# （4）python,写入文件

# print('a'+'b')
# print('a'+'1')
# print('a'+str(1))

# ff = open('C:/Users/pengcong/Desktop/Python100 days/write.txt','w')  
# #打开一个文件，可写模式
# with open('C:/Users/pengcong/Desktop/Python100 days/table.txt','r') as f:  
# #打开一个文件只读模式
#     line = f.readlines()　　
# #读取文件中的每一行，放入line列表中
#     for line_list in line:　　　　
#         line_new =line_list.replace('\n','')　　
# #将换行符替换为空('')
#         line_new=line_new+r'|'+'\n'  
# #行末尾加上"|",同时加上"\n"换行符
#         print(line_new)
#         ff.write(line_new) 
# #写入一个新文件中


# exit 
