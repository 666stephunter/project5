import random
f_input = input('Введите название файла: ')
while True:
    try:
        f_in = open(f_input, 'r')
    except FileNotFoundError:
        print('попробуйте еще раз')
        f_inp = input('Введите название файла: ')
    else:
        f_in = open(f_input, 'r')
        break
with open('abc.txt') as f_in:
    with open('cba.txt','w') as f_out:
        text = f_in.readlines()
        for line in text:
            word = line.split()
            if word[0:2] == 'дез' or 'диз' or 'диc' or 'пан' or 'суб' or 'экс' :
                print(word)
            elif word[0:3] == 'анти' or 'архи' or 'гипо' or 'пост' :
                print(word)
            else:
                print('Иноязычные слова отсутствуют')