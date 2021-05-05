from While_Calculator import nums
from Versions import __version__

while True:

    message = input('Приветствую. Меня зовут бот, введите что хотите сделать либо введите "Выход", что бы закончить работу со мной. Вот мой функционал: Калькулятор, Поддержка: ')

    if message == "Выход":
        break


    if message == 'Поддержка':
        info = input('Что бы узнать версию введите "version"')

        if info == 'version':
            print('Версия программы = ',__version__)


    elif message == 'Калькулятор':
        #Начало калькулятора
        a = input('Введите первое число: ')
        num = input('Введите нужное действие: ')
        b = int(input('Введите второе число: '))
        nums(a,b, num)
        #Конец калькулятора

print('Удачи!')
