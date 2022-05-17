import random
#입력하는 곳
number = random.randrange(1,100)

#결과
down = "다운"
up = "업"
same = "정답"
op = 0
#숫자 계산
while 1:
    number2 = input("1에서 100중 숫자를 고르시오:")
    if int(number)<int(number2):
        op+= 1
        print(down)
        print("_____________________________")

        
    elif int(number)>int(number2):
        op+= 1
        print(up)
        print("_____________________________")

    else:
        print(same)
        print("시도횟수:",op)
        break