# Задача 10. Настолки
# Для настольной игры используются карточки с номерами от 1 до N. Одна карточка потерялась.
# Найдите ее, зная номера оставшихся карточек.
# Вводится число N, далее еще N − 1 чисел: номера оставшихся карточек (различные числа от 1 до N).
# Программа должна вывести номер потерянной карточки.
inputCardSumm = 0
cardSumm = 0
lastCard = int(input('Введите номер последней карточки: '))
for card in range(1, lastCard + 1):
    cardSumm += card
for card in range(lastCard - 1):
    remainingCard = int(input('Введите номер карточки: '))
    inputCardSumm += remainingCard
missedCard = cardSumm - inputCardSumm
print('Потеряли карточку под номером', missedCard)