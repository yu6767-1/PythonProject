#求四位水仙花数
for i in range(1000,10000):
    a=i//1000
    b=i//100%10
    c=i//10%10
    d=i%10
    if a**4+b**4+c**4+d**4==i:
        print(i,end=' ')