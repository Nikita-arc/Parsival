newlist = []
print(newlist)

newlist.append('My name is Nikita')
print()

while True: #Тест цикла с input
    your_year = input('Введите возраст: ')

    if your_year == 'exit':
        break

    newlist.append(your_year)

    for item in newlist:
        print(item, end = ' ')
