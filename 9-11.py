out_file = open('vocabulary.txt', 'w', encoding='UTF8')

while True:
    english_word = input("영어 단어를 입력하세요: ")
    if english_word == 'q':
        break

    korean_meaning = input("한국어 뜻을 입력하세요: ")
    out_file.write("%s: %s\n" % (english_word, korean_meaning))
    if korean_meaning == 'q':
        break
out_file.close()
