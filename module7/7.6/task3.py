# Задача 3. Посчитали чужую зарплату...
# Бухгалтер устала постоянно считать вручную среднегодовую зарплату сотрудников компании и чтобы облегчить себе жизнь,
# обратилась к программисту.
# Напишите программу, которая принимает от пользователя зарплату сотрудника за каждый из 12 месяцев и
# выводит на экран среднюю зарплату за год.
salary = 0
total_salary = 0
for month in range(1, 13):
    print('Текущий месяц -', month)
    salary = int(input('Введите зарплату сотрудника за текущий месяц: '))
    total_salary += salary
avgSalary = total_salary / 12
print('Средняя зарплата сотрудника за год -', avgSalary, 'рублей')