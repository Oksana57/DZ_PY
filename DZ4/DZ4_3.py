from decimal import Decimal

MIN_SUM = 50
PROCENT_COMIS = 0.015
MIN_TAKE = 30
MAX_TAKE = 600
PROCENT_INCOM = 0.03
LIMIT_FOR_TAX = 5_000_000
PROCENT_TAX = 0.1


def get_money(balance: Decimal):
    money_to_get = Decimal(input('введите количетво денег: '))
    procent_geting = money_to_get * Decimal(PROCENT_COMIS)
    if MIN_TAKE < procent_geting < MAX_TAKE:
        procent_geting = procent_geting
    elif MIN_TAKE > procent_geting:
        procent_geting = MIN_TAKE
    else:
        procent_geting = MAX_TAKE
    
    if money_to_get // MIN_SUM:
        if money_to_get + procent_geting <= balance:
           print(balance)
           return balance - (money_to_get + procent_geting)
        else:
            print("недостаточно денег")
            print(balance)
    else:
        print(f'сумма должна быть кратной {MIN_SUM}')
        print(balance)
        return balance   


def give_money(balance: Decimal):
    money_to_give = Decimal(input('введите количетво денег: '))
    if money_to_give // MIN_SUM:
        return balance + money_to_give
        print(balance)
    else:
       
        print(f'сумма должна быть кратной {MIN_SUM}')
            
        print(balance)
        return balance


def menu(balance: Decimal, count: int, is_flag: bool):
    if balance > LIMIT_FOR_TAX:
        balance*=(1-PROCENT_TAX)
    dict1 = {'1' : 'снять со счет', 
             '2' : 'пополнить счет',
             '3' : 'выйти'}
    
    for k, v in dict1.items():
        
        print(f'{k},{v}')
            
    choise = input('введите команду: ')
    
    if choise == '3':
        
        print("До свиданья")
        is_flag = False
    elif choise == '1':
        balance = get_money(balance)
        count+=1
    elif choise == '2':
        balance = give_money(balance)
        count+=1
    else:
        print('неверная комнда')
    if count % 3 == 0:
        balance*=(1+PROCENT_INCOM)
    print(balance)
    return balance, is_flag



if __name__ == '__main__':
     print('Добро пожаловать')
     sum_operation = 0
     balance = 1000
     count = 1
     is_flag = True
     while is_flag:
        balance, is_flag = menu(balance, count, is_flag)

