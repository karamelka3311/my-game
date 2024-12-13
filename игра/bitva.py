from random import randint
from time import sleep
from enemy import*
print(f"на вас напал:",sloidog['name'])
while True:
        print("ваши действия:"
        "1-удар "
        '2-защита ')
        deistvie = int(input(""))
        if deistvie == 1:
            udar = sloidog['hp']-igor['atk']
            sloidog['hp'] -= igor['atk']
            print("вы нанесли удар,у злой собаки осталось:",udar)
            udar = igor['hp']-sloidog['atk']
            igor['hp']-=sloidog['atk']
            print("злая собака вас атаковала,у вас осталось",udar,"хп")
        elif deistvie == 2:
            defens = igor['defens']-sloidog['atk']
            igor['defens']-=sloidog['atk']
            print("вы заблокировали удар злой собаки,защита составила",defens)
            kontr = sloidog['hp']-igor['atk']
            sloidog['hp'] -= igor['atk']
            print("вы контр атаковали,у злой собаки осталось",kontr)
            if igor['defens'] <=0:
                defens = igor['hp']-sloidog['atk']
            igor['hp']-=sloidog['atk']
            print('ваша защита сломана вы больше не сможете контратаковать в этой битве,ваше хп составляет',defens)
        if igor['hp'] <= 0:
            print(f'вы проиграли,злая собака:',sloidog['lose'])
            break
        elif sloidog['hp'] <= 0:
             print(f'вы выйграли',sloidog['win'])
             igor['money']+=50
             print(f'в кошелёк добавилось 50')
             igor['lvl']+=1
             print("ваш уровень повышен на 1")
             
        
        if igor['lvl'] == 2:
            print(f"на вас напал:",mishkasosiska['name'])
            print("ваши действия:"
            "1-удар "
            '2-защита ')
            deistvie = int(input(""))
            if deistvie == 1:
                udar = mishkasosiska['hp']-igor['atk']
                mishkasosiska['hp'] -= igor['atk']
                print("вы нанесли удар,у мышки сосиски осталось:",udar)
                udar = igor['hp']-mishkasosiska['atk']
                igor['hp']-=mishkasosiska['atk']
                print("мышки сосиска вас атаковала,у вас осталось",udar,"хп")
            elif deistvie == 2:
                defens = igor['defens']-mishkasosiska['atk']
                igor['defens']-=mishkasosiska['atk']
                print("вы заблокировали удар мышки сосиски ,защита составила",defens)
                kontr = mishkasosiska['hp']-igor['atk']
                mishkasosiska['hp'] -= igor['atk']
                print("вы контр атаковали,у мышки сосиски  осталось",kontr)
                if igor['defens'] <=0:
                    defens = igor['hp']-mishkasosiska['atk']
                    igor['hp']-=mishkasosiska['atk']
                    print('ваша защита сломана вы больше не сможете контратаковать в этой битве,ваше хп составляет',defens)
                    break
            if igor['hp'] <= 0:
                print(f'вы проиграли,мышки сосиска:',mishkasosiska['lose'])
            elif mishkasosiska['hp'] <= 0:
                print(f'вы выйграли:',mishkasosiska['win'])
                igor['money']+=50
                print(f'в кошелёк добавилось 150')
                igor['lvl']+=1
                print("ваш уровень повышен на 1")
                
               
        if igor['lvl'] == 4:
            print(f"на вас напал:",enemiposhalko['name'])
            print("ваши действия:"
            "1-удар "
            '2-защита ')
            deistvie = int(input(""))
            if deistvie == 1:
                udar = enemiposhalko['hp']-igor['atk']
                enemiposhalko['hp'] -= igor['atk']
                print("вы нанесли удар,у КРОКОДИЛА В ВАННОЙ осталось:",udar)
                udar = igor['hp']-enemiposhalko['atk']
                igor['hp']-=enemiposhalko['atk']
                print("КРОКОДИЛ В ВАННОЙ вас атаковала,у вас осталось",udar,"хп")
            elif deistvie == 2:
                defens = igor['defens']-enemiposhalko['atk']
                igor['defens']-=enemiposhalko['atk']
                print("вы заблокировали удар КРОКОДИЛА В ВАННОЙ ,защита составила",defens)
                kontr = enemiposhalko['hp']-igor['atk']
                enemiposhalko['hp'] -= igor['atk']
                print("вы контр атаковали,у КРОКОДИЛА В ВАННОЙ  осталось",kontr)
                if igor['defens'] <=0:
                    defens = igor['hp']-enemiposhalko['atk']
                    igor['hp']-=enemiposhalko['atk']
                    print('ваша защита сломана вы больше не сможете контратаковать в этой битве,ваше хп составляет',defens)
                    break
            if igor['hp'] <= 0:
                print(f'вы проиграли,КРОКОДИЛ В ВАННОЙ:',enemiposhalko['lose'])
            elif enemiposhalko['hp'] <= 0:
                print(f'вы выйграли:',enemiposhalko['win'])
                igor['money']+=50
                print(f'в кошелёк добавилось 200')
                igor['lvl']+=1
                print("ваш уровень повышен на 2")
                break

        if igor['lvl'] == 8:
            print(f"на вас напал:",magicaltree['name'])
            print("ваши действия:"
            "1-удар "
            '2-защита ')
            deistvie = int(input(""))
            if deistvie == 1:
                udar = magicaltree['hp']-igor['atk']
                magicaltree['hp'] -= igor['atk']
                print("вы нанесли удар,у магического древа осталось:",udar)
                udar = igor['hp']-magicaltree['atk']
                igor['hp']-=magicaltree['atk']
                print("магическое древо вас атаковала,у вас осталось",udar,"хп")
            elif deistvie == 2:
                defens = igor['defens']-magicaltree['atk']
                igor['defens']-=magicaltree['atk']
                print("вы заблокировали удар магического древа,защита составила",defens)
                kontr = magicaltree['hp']-igor['atk']
                magicaltree['hp'] -= igor['atk']
                print("вы контр атаковали,у магического древа  осталось",kontr)
                if igor['defens'] <=0:
                    defens = igor['hp']-magicaltree['atk']
                    igor['hp']-=magicaltree['atk']
                    print('ваша защита сломана вы больше не сможете контратаковать в этой битве,ваше хп составляет',defens)
                    break
            if igor['hp'] <= 0:
                print(f'вы проиграли,магического древа:',magicaltree['lose'])
            elif magicaltree['hp'] <= 0:
                print(f'вы выйграли:',magicaltree['win'])
                igor['money']+=50
                print(f'в кошелёк добавилось 200')
                igor['lvl']+=1
                print("ваш уровень повышен на 2")
                break
