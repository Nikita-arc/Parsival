a = b = 1
c = input('Введите номер искомого элемента : ')
c = int(c)
for n in range(int(c-2)):
    tmp = a + b
    a = b
    b = tmp
print(str(c)+' элемент последовательности равен ' + str(b))