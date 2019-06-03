"""

求解《百钱百鸡》问题
1只公鸡5元 1只母鸡3元 3只小鸡1元 用100元买100只鸡
问公鸡 母鸡 小鸡各有多少只

Version: 0.1
Author: 骆昊
Date: 2018-03-02

"""
"""
my version:.1
author:李辰鹏
date：2019/05/29
"""
# 提示是穷举法
for x in range(0,20):
    for y in range(0,33):
        z=100-x-y
        if(x*5+y*3+z//3)==100:
            print("公鸡 母鸡 小鸡各有 %d , %d , %d 只" % (x,y,z))
