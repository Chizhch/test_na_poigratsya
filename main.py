
def menu():
    print('Выберете действие: '
                   f'\n1. пополнить счет'
                   f'\n2. покупка'
                   f'\n3. история покупок'
                   f'\n4. выход')
    deystvie=int(input('введите одну цифру для продолжения: '))
    return deystvie

def funkcii(vibor,shet,history):
    if vibor == 1:
        print('введиту сумму пополнения')
        popolnenie = int(input('Сумма: '))
        shet_1=0
        shet_1 = popolnenie + shet_1
        return shet_1

    elif vibor == 3:
        print(history)
        return 3
    elif vibor == 4:
        return False

    elif vibor == 2:
        print('введиту сумму покупки')
        pokupka=int(input('сумма: '))
        if pokupka > shet:
                print('пополните счет')
                return 3
        else:
                print(f'Списано со счета {pokupka}')
                i = int(len(history)/4+1)
                history.append('номер покупки:')
                history.append(i)
                history.append('сумма покупки:')
                history.append(pokupka)
                return -(pokupka)
    else:
        return 3
shet=0
popolnenie=0
history = []
while True:
    result = menu()
    vozrat = funkcii(result,shet,history)
    shet = shet + vozrat

    if vozrat == False:
        print('Работа программы завершена')
        break
    elif vozrat == 3:
        print('работа продолжена')
        shet=shet-3
    else:
        print('')
    print('\n')
    print(f'сумма счета: {shet}','\n')



