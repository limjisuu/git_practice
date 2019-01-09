from random import randint

# 무작위로 정렬된 1 - 45 사이의 숫자 여섯개 뽑기


def generate_numbers():
    # 코드를 입력하세요
    lottery_number_list = []
    while len(lottery_number_list) < 6:
        lottery_number = randint(1, 45)

        # 새로운 수 나올때까지 다시 뽑기
        while lottery_number in lottery_number_list:
            lottery_number = randint(1, 45)

        lottery_number_list.append(lottery_number)

    lottery_number_list.sort()
    return lottery_number_list

six_lottery_numbers = generate_numbers()
# 보너스까지 포함해 7개 숫자 뽑기
# 정렬된 6개의 당첨 번호와 1개의 보너스 번호 리스트를 리턴
# 예: [1, 7, 13, 23, 31, 41, 15]
def draw_winning_numbers():
    # 코드를 입력하세요
    bonus_number = randint(1, 45)
    while bonus_number in six_lottery_numbers:
        bonus_number = randint(1, 45)
    six_lottery_numbers.append(bonus_number)
    return six_lottery_numbers

winning_numbers = draw_winning_numbers()

# 두 리스트에서 중복되는 숫자가 몇개인지 구하기
def count_matching_numbers(list1, list2):
    # 코드를 입력하세요
    count = 0
    for i in range(int(len(list1))):
        if list1[i] in list2:
            count += 1
    return count

# 로또 등수 확인하기
def check(numbers, winning_numbers):
    # 코드를 입력하세요
    check_match = count_matching_numbers(numbers, winning_numbers[0:len(winning_numbers)])
    if check_match == 6:
        return 1000000000
    elif check_match == 5 and winning_numbers[-1] in numbers:
        return 50000000
    elif check_match == 5:
        return 1000000
    elif check_match == 4:
        50000
    elif check_match == 3:
        5000