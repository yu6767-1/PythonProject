#冒泡排序
ls=[1,99,2,6,66,7,8,22]
for i in range(len(ls)):
    for k in range(len(ls)-i-1):
        if ls[k]>ls[k+1]:
            n=ls[k+1]
            ls[k+1]=ls[k]
            ls[k]=n
print(ls)
