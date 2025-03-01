# -*- coding: utf-8 -*-
from ast import Index
import csv
import random

cptl_list = []
ctry_list = []

with open('capital_cities.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader) #skip header

    for row in reader:
        cptl_list.append(row[5])
        ctry_list.append(row[6])

    i = 1
    s = 5
    print('1:簡単')
    print('2:普通')
    print('3:難しい')
    print('9:IMPOSSIBLE')

    lv = int(input('レベル選択:'))
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
            print('仕様上1文字でも間違えると不正解になります')
            print('空欄で回答するとスキップ')
    else:
        print('有効な値を入力してください')

print('Start!\n')

while True:
    opt_ary = random.sample(cptl_list,dif)
    rnd = random.randint(0,dif - 1)

    ans = cptl_list.index(opt_ary[rnd])
    q = ctry_list[ans]

    #start game
    print(i,q + " の首都は？\n")
    if (impossible == False):
        for idx, city in enumerate(opt_ary, start=1):
            print(f"{idx}. {city}")
        print()  # 改行

        a = int(input('番号で回答:'))

        if (a == rnd + 1):
            print('\n正解！\n')
            i = i + 1
        else:
            print('\n不正解')
            print(q + ' の首都は' , rnd + 1 , '番の ' + cptl_list[ans] + ' だぞ！\n')
            break
    else:
        a = input()

        if (a == cptl_list[ans]):
            print('\n正解！\n')
            i = i + 1
        elif(a == ''):
            if (s > 0):
                s = s - 1
                print('スキップ使用 残り', s , '回')
                i = i + 1
            else:
                print('\n不正解')
                print(q + ' の首都は ' + cptl_list[ans] + ' だぞ！\n')
                break
        else:
            print('\n不正解')
            print(q + ' の首都は ' + cptl_list[ans] + ' だぞ！\n')
            break

