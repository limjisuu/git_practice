in_file = open('chicken.txt', 'r', encoding='UTF8')
sum = 0
day = 0
for line in in_file:
    data = line.strip().split(": ")
    amount = int(data[1])
    sum = sum + amount
    day = day + 1
print(sum / day)
