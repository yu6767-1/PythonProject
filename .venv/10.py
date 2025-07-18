#打印菱形
y,n=input("输入字符和层数:").split()
n=int(n)
#先对前四行进行布局
for i in range(1,n//2+1+1):
    s1=4-i
    s2=2*i-1
    print(' '*s1+y*s2)
for j in range(1,n//2+1):
    s1=j
    s2=7-2*j
    print(' '*s1+y*s2)
