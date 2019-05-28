# just start learning python by jackfrued's tutorial
import random

count=0
answer=random.randrange(0,100)
while True:
    count+=1
    guess=int(input("Enter your guess,between 1 and 100 : "))
    if guess > answer :
        print('your answer is bigger')
    elif guess < answer :
        print('your answer is smaller')
    elif guess==answer:
        print("success!you figured out the right number!")
        break
# print('you tried {0} times!',count)
print('you tried %d times!' % count)
if count > 7 :
    print('you need some medicine for the head.')

    
    
