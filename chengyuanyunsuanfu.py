'''
a=2
b=3
list=[1,2,3,4,5,6]
if(a in list):
    print('a在list中')
else:
    print('a不在list中')
  
  '''

'''
a=1
float(a)
print(a)
'''

'''
print(2+4)
print(3**3)#3的3次方  
t=max(1,3,4,9)#max为函数 可以直接调用了
print(t)
t=round(2,7382)#返回x的四舍五入值
print(t)
'''

print(round(10.4))
print(round(10.5))
print(round(11.4))
print(round(11.5))
'''
round函数的坑
当小数点左边为偶数：小数点右边X<6，舍
当小数点左边为偶数：小数点右边X>=6，入
当小数点左边为奇数：小数点右边X<5，舍
当小数点左边为奇数：小数点右边X>=5，入
4舍6入5看齐,奇进偶不进
'''
