coin1 = int(input('Введите вес первой монеты: '))
coin2 = int(input('Введите вес второй монеты: '))
coin3 = int(input('Введите вес третьей монеты: '))
if coin1 == coin2:
    print('Фальшивая монета - третья!')
elif coin2 == coin3:
    print('Фальшивая монета - первая!')
else:
    print('Фальшивая монета - вторая!')