from random import randint
from time import sleep
from enemy import*
name = input("введите своё имя путник: ")
print("добро пжаловать в этот мир хауса: ",name)
while True:
    print("чего ты желаешь:",name,
          f'1-начать битву '
          f'2-тренировка '
          f'3-магазин '
          f'4-статистика о игроке')
    deistvie = int(input(""))
    if deistvie ==1:
        from bitva import*
    if deistvie == 2:
        print("что ты хочешь повысить:"
           f'1-здоровье '
           f'2-атака')
        deistvie = int(input(""))
        if deistvie == 1:
            igor['hp'] +=  randint(1,10)
            print("ваше здоровье увеличилось",igor['hp'])
        else:
            igor['atk'] +=  randint(1,10)
            print("ваша атака увеличилась",igor['atk'])
    if deistvie == 4:
        for key,item in igor.items():
            print(f"ваша статистика:",key,item)
    if deistvie == 3:
        for key,item,in magazin.items():
            print("что вы хотите приобрести:",key,item)
        deistvie = int(input(""))
        if deistvie == 1:
            if igor['money']<100:
                print('вы не можете себе этого позволить')
            else:
                igor['money']-=100
                igor['atk']+=10
                print('ваша атака увеличена на 10')
        elif deistvie == 2:
            if igor['money']<200:
                print('вы не можете себе этого позволить')
            else:
                igor['money']-=200
                igor['atk']+=15
            print('ваша атака увеличена на 25')
        elif deistvie == 3:
            if igor['money']<300:
                print('вы не можете себе этого позволить')
            else:
                igor['money']-=300
                igor['atk']+= 25
                print('ваша атака увеличена на 40')
        elif deistvie == 4:
            if igor['money']<400:
                print('вы не можете себе этого позволить')
            else:
                igor['money']-=400
                igor['atk']+= 40
            print('ваша атака увеличена на 55')
        elif deistvie == 5:
            if igor['money']<600:
                print('вы не можете себе этого позволить')
            else:
                igor['money']-=600
                igor['atk']+= 35
                print('ваша атака увеличена на 35')
        elif deistvie == 6:
            if igor['money']<700:
                print('вы не можете себе этого позволить')
            else:
                igor['money']-=700
                igor['atk']+= 70
                print('ваша атака увеличена на 70')
        elif deistvie == 7:
            if igor['money']<1000:
                print('вы не можете себе этого позволить')
            else:
                igor['money']-=1000
                igor['atk']+= 90
                print('ваша атака увеличена на 90')
