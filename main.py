"""Field of wonders game"""
import random
import re
worlds = ['banana', 'apple', 'world']

def find_letters(wordlist:list):
    """
    find letters or worlds in list
    :param wordlist:
    :return: bool
    """
    secretword = random.choice(wordlist)
    temp = re.sub("[a-zA-Z]", "*", secretword)
    templist = []

    while True:
        try:
            num = int(input("Введіть кількість спроб: "))
            break
        except ValueError:
            print("Помилка: Введіть ціле число!")

    print('Вгадайте слово з ', num, 'спроб:', temp)

    while num != 0:
        letter = input("Введіть букву або все слово:")
        if letter != secretword:
            if letter in secretword:
                templist.append(letter)
                pattern = r"[^" + "".join(templist) + "]"
                temp = re.sub(pattern, "*", secretword)
                print("Така буква э в цьому слові:", temp)
                if temp == secretword:
                    return True
            else:
                num -= 1
                if len(letter) == len(secretword):
                    print("Слово не вгадано, залишилось спроб:", num)
                else:
                    print("Такої літери немає, залишилось спроб:", num)
        else:
            return True

if find_letters(worlds):
    print('Вітаю, ви вгадали слово!')
else:
    print('Наступного разу пощастить!')
