def printMax(a,b):
    if a > b:
        print(a, 'MAX')
    elif a == b:
        print(a, 'equally', b)
    else:
        print(b, 'MAX')

printMax(3,4) # Прямая передача значений

x = 5
y = 7

printMax(x,y) # Передача переменных в качестве аргумента 
