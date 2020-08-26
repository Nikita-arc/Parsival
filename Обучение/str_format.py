age = 26
name = 'Swaroop'

print('Возраст {0} -- {1} лет.'.format(name, age))
print('Почему {0} забавляется с этим Python?'.format(name))

""">>> '{0:.3}'.format(1/3) # десятичное число (.) с точностью в 3 знака для плавающих
'0.333'
>>> '{0:_^11}'.format('hello') # заполнить подчёркиваниями (_) с центровкой текста (^) по ширине 11
'___hello___'
>>> '{name} написал {book}'.format(name='Swaroop', book='A Byte of Python') # по ключевым словам
'Swaroop написал A Byte of Python'"""
