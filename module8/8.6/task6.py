# Задача 6. Письмо
# У нас есть квадратный конверт размера 12х12 сантиметров и письмо на квадратном листе бумаги, которое не помещается в
# конверт. Напишите программу, которая подскажет сколько раз нужно сложить письмо пополам, чтобы оно поместилось в
# конверт. Размеры письма вводятся с клавиатуры
width = int(input('Введите ширину листа с письмом: '))
length = int(input('Введите длину листа с письмом: '))
envelopeWidth = 12
envelopeLength = 12
folds = 0
while True:
    if width > envelopeWidth:
        width /= 2
        folds += 1
    else:
        break
    if length > envelopeLength:
        length /= 2
        folds += 1
    else:
        break
print('Чтобы письмо поместилось в конверт его нужно свернуть', folds, 'раз.')
print('Размеры письма в итоге:', str(width) + 'x' + str(length))

#Не знаю как решить с for (если это, конечно, нужно решить с for) :(