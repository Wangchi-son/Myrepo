import random

s=1

while s == 1:
    k = 10

    for i in range(10):
        a = random.randrange(9)+1
        b = random.randrange(9)+1
        d = input("{}번 문제 {}+{} 는 얼마인가?".format(i+1,a,b))
        
        if int(d) == a+b:
            print(" 참 잘했습니다.",k,"점 입니다.")
            k += 10

        else:
            print("틀렸습니다.")

        s=int(input(" 계속 하시겠습니까? 1/2"))
        if s ==2:
            print("고생하셨습니다. 문제를 끝내셔도 좋습니다.")
        break
