# Задача 8. Вклады.
# Вклад в банке составляет X рублей. Ежегодно он увеличивается на P процентов, после чего дробная часть копеек
# отбрасывается. Определите, через сколько лет вклад составит не менее Y рублей. Напишите программу, которая
# по данным числам X, Y, P определяет, сколько лет пройдет, прежде чем сумма достигнет значения Y
savings = int(input('Введите баланс вклада: '))
profitpercent = int(input('Введите процентную ставку вклада: '))
goal = int(input('Сколько денег нужно накопить?'))
yearcounter = 0
while savings < goal:
    percent = profitpercent / 100
    savings += percent
    savings //= 1
    yearcounter