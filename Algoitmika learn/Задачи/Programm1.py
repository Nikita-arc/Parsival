print('Введите два числа: ')

One = int(input())
Two = int (input())

if One>Two and One % 2 == 0 and Two % 2 == 0: 
    print("Попугай")
elif One % 2 == 0 and Two % 2 == 0 and Two>One:
    print("Медведь")
elif One % 2 == 0 and Two % 2 != 0 and One>Two:
    print("Крокодил")
elif One % 2 != 0 and Two % 2 == 0 and One>Two:
    print("Крокодил")
elif One % 2 == 0 and Two % 2 != 0 and One<Two:
    print("Белочка")
elif One % 2 == 0 and Two % 2 != 0 and One<Two:
    print("Белочка")
elif One % 2 != 0 and Two % 2 != 0 and One>Two:
    print("Зайчик")
elif One % 2 != 0 and Two % 2 != 0 and One<Two:
    print("Гусеница")
elif One == Two and One % 2 == 0 and Two % 2 == 0:
    print("escherichia coli")
elif One == Two and One % 2 != 0 and Two % 2 != 0:
    print("Кот леопольд")
else:
    print("Извините, ошибка")