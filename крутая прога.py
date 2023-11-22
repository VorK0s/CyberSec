import sys
import random
import calendar
import time
import turtle
import os
import re

print('Добро пожаловать в супер крутое и бессмысленное приложение')
time.sleep(2)
print('Доступные функции:')
print('1. Алфавит')
print('2. Калькулятор')
print('3. Календарь(любой год)')
print('4. Игры')
vibor = 0
vibor = int(input('Выбери цифру нужной тебе функции\n'))
if vibor == 1:
    print('Доступные алфавиты:')
    print('1. Русский')
    print('2. Английский')
    print('3. Латынский')
    alphabets = int(input('Алфавит:\n'))
    if alphabets == 1:
        print('А(гласн)\nБ(согл)\nВ(согл)\nГ(согл)\nД(согл)\nЕ(гласн)\nЁ(гласн)\nЖ(согл)\nЗ(согл)\nИ(гласн)\nЙ(согл)\nК(согл)\nЛ(согл)\nМ(согл)\nН(согл)\nО(гласн)\nП(согл)\nР(согл)\nС(согл)\nТ(согл)\nУ(гласн)\nФ(согл)\nХ(согл)\nЦ(согл)\nЧ(согл)\nШ(согл)\nЩ(согл)\nЪ(нет звука)\nЫ(гласн)\nЬ(нет звука)\nЭ(гласн)\nЮ(гласн)\nЯ(гласн)')
    elif alphabets == 2:
        print('A(vowel)\nB(constonant)\nC(constonant)\nD(constonant)\nE(vowel)\nF(constonant)\nG(constonant)\nH(constonant)\nI(vowel)\nJ(constonant)\nK(constonant)\nL(constonant)\nM(constonant)\nN(constonant)\nO(vowel)\nP(constonant)\nQ(constonant)\nR(constonant)\nS(constonant)\nT(constonant)\nU(vowel)\nV(constonant)\nW(constonant)\nX(constonant)\nY(vowel)\nZ(constonant)')
    elif alphabets == 3:
        print('A(vocalis)\nB(consonans)\nC(consonans)\nD(consonans)\nE(vocalis)\nF(consonans)\nG(consonans)\nH(consonans)\nI(vocalis)\nJ(consonans)\nK(consonans)\nL(consonans)\nM(consonans)\nN(consonans)\nO(vocalis)\nP(consonans)\nQ(consonans)\nR(consonans)\nS(consonans)\nT(consonans)\nU(vocalis)\nV(consonans)\nW(consonans)\nX(consonans)\nY(vocalis)\nZ(consonans)')
elif vibor == 2:
    drobi = str(input('дробные части (y / n)'))
    if drobi == 'y':
        first_num = float(input('фирст намбер: '))
        op = str(input('операция: '))
        second_num = float(input('секонд намбер: '))
        if op == '+':
            print(first_num + second_num)
        elif op == '-':
            print(first_num - second_num)
        elif op == '*':
            print(first_num * second_num)
        elif op == '/':
            print(first_num / second_num)
        else:
            print('та нифика, го нормальную операцию')
    elif drobi == 'n':
        first_num = int(input('фирст намбер: '))
        op = str(input('операция: '))
        second_num = int(input('секонд намбер: '))
        if op == '+':
            print(first_num + second_num)
        elif op == '-':
            print(first_num - second_num)
        elif op == '*':
            print(first_num * second_num)
        elif op == '/':
            print(first_num / second_num)
        else:
            print('та нифика, го нормальную операцию')
    else:
        print('ну ты вообще осел?')
elif vibor == 3:
    year = int(input('Год:\n'))
    month = int(input('Месяц:\n'))
    print(calendar.month(year, month))
elif vibor == 4:
    print('Список игр: ')
    print('1. Угадай число')
    print('2. Виселица')
    print('3. Камень, ножницы, бумага')
    games = int(input('Выбери игру: \n'))
    if games == 1:
        def guess_the_number():
            number = random.randint(1, 100)
            attempts = 0

            while True:
                guess = int(input('Начинай отгадывать: '))
                attempts += 1

                if guess < number:
                    print('больше')
                elif guess > number:
                    print('меньше')
                else:
                    print('поздравляю, ты угадал число за', attempts, 'попыток')
                    break
        guess_the_number()
    elif games == 2:
        def hangman():
            words = ['перфоратор','перфокарта','штаны', 'код', 'питон', 'дверь', 'полотенце', 'вкладка', 'взрыв', 'джава', 'мультиварка', 'микроволновка', 'клавиатура', 'окно', 'хлеб', 'календарь', 'звезда', 'видеокарта', 'текстиль', 'назначенец', 'читальня', 'библиотека', 'паникер', 'юность', 'брат']
            word = random.choice(words)
            guesses = ''
            attempts = 6
            while attempts > 0:
                for char in word:
                    if char in guesses:
                        print(char, end=' ')
                    else:
                        print('_', end=' ')
                print()
                guess = input('Буква: ')
                guesses += guess

                if guess not in word:
                    attempts -= 1

                if set(word) <= set(guesses):
                    print('поздравляю, вы угадали слово', word)
                    break
                elif attempts == 0:
                    print('Поражение, словом было:', word)
        hangman()
    elif games == 3:
        def check_play_status():
            valid_responses = ['д', 'н']
            while True:
                try:
                    response = input('Играем еще? (д/н): ')
                    if response.lower() not in valid_responses:
                        raise ValueError('да ты дурачек?')
                    if response.lower() == 'д':
                        return True
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print('Спасибо за игру!')
                        exit()
                except ValueError as err:
                    print(err)

        def play_rps():
            play = True
            while play:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('')
                print('Камень, Ножницы, Бумага - раз два три!')
                user_choice = input('Выбери'
                           ' [К]амень, [Н]ожницы, или [Б]умага: ')

                if not re.match("[КкНнБб]", user_choice):
                    print('ВЫБЕРИ БУКВУ:')
                    print('[К]амень, [Н]ожницы, или [Б]умага')
                    continue

                print(f'Твой выбор: {user_choice}')
                choices = ['К', 'Н', 'Б']
                opp_choice = random.choice(choices)
                print(f'Мой выбор: {opp_choice}')
                
                if opp_choice == user_choice.upper():
                    print('Ничья!')
                    play = check_play_status()
                elif opp_choice == 'Б' and user_choice.upper() == 'К':
                    print('Бумага кроет камень, я победил')
                    play = check_play_status()
                elif opp_choice == 'Н' and user_choice.upper() == 'Б':
                    print('Ножницы режут бумагу, я победил')
                    play = check_play_status()
                elif opp_choice == 'К' and user_choice.upper() == 'Н':
                    print('Камень бьет ножницы, я победил')
                    play = check_play_status()
                else:
                    print('Ты победил\n')
                    play = check_play_status()

        if __name__ == '__main__':
            play_rps()
