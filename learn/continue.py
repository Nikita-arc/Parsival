while True:
    s = input('Введите что-нибудь: ')
    if s == 'Выход':
        break
    if len(s) < 3:
        print("Слишком мало")
    print('Введёная строка достаточной длины')
    # Разные другие действия здесь...
