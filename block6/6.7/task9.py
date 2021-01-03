# Задача 9. Игра “Угадай число”
# В одном из домашних заданий мы делали задачу, где папа-программист написал для сына программу, которая просит его
# угадать число. Недостаток той программы был в том, что бедному сыну приходилось её каждый раз перезапускать, чтобы
# угадывать число. Теперь, когда мы знаем гораздо больше, пришло время исправить этот недостаток и заодно немного
# улучшить саму игру.
# Напишите программу-игру, которая запрашивает у пользователя число до тех пор, пока он его не отгадает.
# Выводите сообщения в соответствии с примером
number = 7
inputnum = 0
trycounter = 0
while inputnum != 7:
    inputnum = int(input('Введите число: '))
    if inputnum > number:
        print('Число больше, чем нужно. Попробуйте ещё раз!')
    else:
        print('Число меньше, чем нужно. Попробуйте ещё раз!')
    trycounter += 1
print('Вы угадали! Число попыток:', trycounter)