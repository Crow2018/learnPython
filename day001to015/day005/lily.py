#水仙花数 153=1^3+5^3+3^3
#找出100~999之间的所有lily

for num in range(100,1000):
    low=num%10
    mid=num//10%10
    high=num//100
    if num==low**3+mid**3+high**3:
        print(num,'\t')

#**表示指数运算
#//表示向下取整除法