from random import randint

answer = randint(1, 20)
time = 4
while time >= 1:
    user = int(input("기회가 %d번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: " % (time)))
    if user < answer:
        print("Up")

    elif user > answer:
        print("Down")
    else:
        print("축하합니다. %d번만에 숫자를 맞추셨습니다." % (5 - time))
        break
    time = time - 1

if time == 0:
    print("아쉽습니다. 정답은 %d였습니다." % (answer))