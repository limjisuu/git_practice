out_file = open('vocabulary.txt', 'r', encoding='UTF8')

vocab = {}
for line in out_file:
    data = line.strip().split(': ')
    english_word = data[0]
    korean_word = data[1]

    for word in data:
        vocab['%s' % (korean_word)] = '%s' % (english_word)

from random import randint

keys = list(vocab.keys())

while True:
    index = randint(0, len(keys) - 1)
    korean_word = keys[index]
    english_word = vocab[korean_word]
    # 코드를 입력하세요.
    user_answer = input("%s: " % (korean_word))
    if user_answer == english_word:
        print('맞았습니다!')
    else:
        print('틀렸습니다. 정답은 %s입니다.' % (english_word))