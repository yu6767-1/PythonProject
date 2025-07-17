#判断是否为素数
from math import sqrt
def isprimenumber(x):
    for i in range(2,int(sqrt(x))+1):
        if x%i==0:
            return False
    else:
            return True
for k in range(100,200):
    if isprimenumber(k):
        print(k,end=' ')