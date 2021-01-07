# Задача 9. ...Теперь можно посчитать и свою
# Пока бухгалтер считала среднюю зарплату сотрудников, ей стало интересно, а не зря ли она работает столько времени
# на одном месте? Ей захотелось узнать, увеличивается ли её зарплата с каждым месяцем или нет.
# Пользователь вводит 10 чисел. Напишите программу, которая проверяет, упорядочены ли они по возрастанию.
prevSalary = 0
rising = True
for month in range(10):
    salary = int(input('Введите зарплату: '))
    if salary <= prevSalary:
        rising = False
    prevSalary = salary
if rising:
    print('Зарплата всё время возрастала!')
else:
    print('Зарплата не возрастала всё время!')