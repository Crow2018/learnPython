#输出2~99的质数
import math
#第一个可通过的版本
# for i in range(2,100):
#     flag=True
#     if i>2:
#         m = math.floor(math.sqrt(i))
#         for x in range(2,m+1):
#             if i%x==0 :
#                 flag=False
#     if flag==True :
#         print(i,end=',')
#     flag=False

#查看答案后
#因为range(2,2)是空集，所以i=2不会进入里循环迭代，完美避免了2%2==0导致2被当作非素数的结果
for i in range(2,100):
    is_prime=True
    for factor in range(2,int(math.sqrt(i))+1):
        if i%factor==0:
            is_prime=False
            break
    if is_prime :
        print(i,end=' ')