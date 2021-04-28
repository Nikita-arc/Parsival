def nums(a, b): #Функция предназначена для вычислений(Для удобства редактирования)
    if num == "+":
        print(int(a) + b)
    elif num == "-":
        print(int(a) - b)
    elif num == "*":
        print(int(a) * b)
    elif num == "/":
        print(int(a) / b)
    elif num == "%":
        print(int(a) % b)
    elif num == "**":
        print(int(a) ** b)


while True:

    a = input('Введите первое число что бы начать считать или "Выход", что бы выйти: ')

    if a == 'Выход': #Выходим из нашего цикла
        break

    num = input('Введите нужное действие: ')
    b = int(input('Введите второе число: '))

    nums(a, b) #Вызываем функцию
print('Спасибо! Заходите ещё :-)')
