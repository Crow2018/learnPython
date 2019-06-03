# 输出九九乘法表
#my version

# i,j=0,0
# while i<10:
#     i+=1
#     j=i
#     while j<10:
#         print('%d x %d = %d' % (i,j,i*j),end='\t')
#         j+=1
#     print()

#after checked version
i=1
while i<10:
    j=1
    while j<i+1:
        print('%d x %d = %d' % (j,i,i*j),end='\t')
        j+=1
    print()
    i+=1