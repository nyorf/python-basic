score = int(input('Сколько ты набрал баллов? '))
medal = int(input('Есть медаль? (1 - да, 0 - нет) '))
if score < 280 or medal == 0:
    print('К сожалению, ты не поступил в наш университет.')
else:
    print('Поздравляем, ты поступил в наш университет!')