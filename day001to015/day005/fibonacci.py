# 输出前20个斐波那契数
a,b=0,1
n=21
i=1
while i<n :
    a,b=b,a+b
    print(a,end=' ')
    i+=1