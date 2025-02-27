# -*- coding: utf-8 -*-
from ast import Index
import csv
import random

cptl_list = []
ctry_list = []

with open('capital_cities_2024.csv', mode='r', encoding='shift_jis') as file:
    reader = csv.reader(file)
    next(reader) #skip header

    for row in reader:
        cptl_list.append(row[5])
        ctry_list.append(row[6])

    i = 1
    s = 5
    print('1:Easy')
    print('2:Normal')
    print('3:Hard')
    print('9:IMPOSSIBLE')

    lv = int(input('Select Level:'))
    dif = 0
    impossible = False

    if (lv == 1 or lv == 2 or lv == 3 or lv == 9 ):
        if(lv == 1):
            dif = 2
        elif(lv == 2):
            dif = 4
        elif(lv == 3):
            dif = 10
        elif(lv == 9):
            dif = 197
            impossible = True
            print('Due to the specifications, if even one character is incorrect, the answer will be incorrect.')
            print('Skip if answer is blank')
    else:
        print('Enter a valid value')

print('Start!\n')

while True:
    opt_ary = random.sample(cptl_list,dif)
    rnd = random.randint(0,dif - 1)

    ans = cptl_list.index(opt_ary[rnd])
    q = ctry_list[ans]

    #start game
    print(i,"Where is the " q + "'s capital city? \n")
    if (impossible == False):
        for idx, city in enumerate(opt_ary, start=1):
            print(f"{idx}. {city}")
        print()  # 改行

        a = int(input('Answer with number'))

        if (a == rnd + 1):
            print('\nCorrect!\n')
            i = i + 1
        else:
            print('\nIncorrect')
            print(q + "'s capital city is" , 'option no.',rnd + 1 , '' + cptl_list[ans] + '!\n')
            break
    else:
        a = input()

        if (a == cptl_list[ans]):
            print('\nCorrect!\n')
            i = i + 1
        elif(a == ''):
            if (s > 0):
                s = s - 1
                print('Used Skip. Remaining', s )
                i = i + 1
            else:
                print('\nIncorrect')
                print(q + "'s capital city is" + cptl_list[ans] + '!\n')
                break
        else:
            print('\nIncorrect')
            print(q + "'s capital city is" + cptl_list[ans] + ' だぞ！\n')
            break

