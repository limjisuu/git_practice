in_file = open('vocabulary.txt', 'r', encoding='UTF8')
for line in in_file:
    data = line.strip().split(": ")
    english_word = data[0]
    korean_word = data[1]
    user = input("%s: " % korean_word)
    if user == english_word:
        print("정답입니다")
    else:
        print("아쉽습니다. 정답은 %s입니다." % (korean_word))