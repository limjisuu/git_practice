from random import randint

def generate_numbers():
    numbers = []

    # 세개 뽑을때까지 반복
    while len(numbers) < 3:
        new_number = randint(0, 9)

        # 새로운 수 나올때까지 다시 뽑기
        while new_number in numbers:
            new_number = randint(0, 9)
        numbers.append(new_number)
    return numbers

answer = generate_numbers()
try_time = 0

print("0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다.")

print("세 수를 하나씩 차례대로 입력하세요.")

guesses = []
strike = 0
ball = 0

while strike < 3:
    time = 1
    while time < 4:
        guess = int(input("%d번째 수를 입력하세요: " % (time)))
        if guess not in guesses and 0 <= guess <= 9:
            time = time + 1

        elif guess in guesses:
            print('중복되는 수 입니다. 다시 입력해주세요.')

        else:
            print('범위를 벗어나는 수입니다. 다시 입력해주세요.')
        guesses.append(guess)

    strike = 0
    ball = 0
    i = 0
    while i < 3:
        if guesses[i] == answer[i]:
            strike += 1

        elif guesses[i] in answer:
            ball += 1
        i += 1
    print("%dS %dB" % (strike, ball))

    try_time += 1

print("축하합니다. %d번 만에 세 숫자의 값과 위치를 모두 맞추셨습니다." % (try_time))