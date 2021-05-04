phone_num = {   'Nikita' : '89232564746',
                'Sasha'  : '89232734647',
                'Stas'   : '88007000505'
            }

while True:

    new_contact = input('Enter new name')

    if new_contact == 'exit':
        break

    new_number = input('Enter new number')
    phone_num[new_contact] = new_number
    print(phone_num)
