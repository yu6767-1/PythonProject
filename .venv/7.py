#输入年月日 判断是这一年的第几天
y,m,d=map(int,input("输入年月日:").split('-'))
days=[0,
      31,28,31,30,
      31,30,31,31,
      30,31,30,31
      ]
if y%4==0 and y%100!=0 or y%400==0:
    days[2]=29
print(sum(days[0:m])+d)