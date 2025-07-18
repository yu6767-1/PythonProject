#用户输入3个数 进行降序或升序排序  区别在于sort
a=list(map(int,input("请输入数字：").split()))
a.sort(reverse=True)
for i in a:
    print(i,end=' ')