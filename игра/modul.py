def length (time,speed):
    len = time * speed
    return len

def speed (length,time):
    speed = length / time
    return speed

def time (length,speeg):
    speed = length / speed
    return time
def battle(igor,enemy):
    deistvie = int(input(""))
    if deistvie == 1:
            udar = enemy['hp']-igor['atk']
            enemy['hp'] -= igor['atk']
            print("вы нанесли удар,у злой собаки осталось:",udar)
            udar = igor['hp']-enemy['atk']
            igor['hp']-=enemy['atk']
            print("злая собака вас атаковала,у вас осталось",udar,"хп")
    elif deistvie == 2:
            defens = igor['defens']-enemy['atk']
            igor['defens']-=enemy['atk']
            print("вы заблокировали удар злой собаки,защита составила",defens)
            kontr = enemy['hp']-igor['atk']
            enemy['hp'] -= igor['atk']
            print("вы контр атаковали,у злой собаки осталось",kontr)
            if igor['defens'] <=0:
                 defens = igor['hp']-enemy['atk']
                 igor['hp']-=enemy['atk']
                 print('ваша защита сломана вы больше не сможете контратаковать в этой битве,ваше хп составляет',defens)
    if igor['hp'] <= 0:
            print(f'вы проиграли,злая собака:',enemy['lose'])