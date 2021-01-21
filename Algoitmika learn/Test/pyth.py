def perimeter(a,b):
    return 2*(a+b)
def area(a,b):
    return a*b
a = int(input("Enter the first side of the rectangle: "))
b = int(input("Enter the second side of the rectangle: "))
print('Perimeter = ',perimeter(a,b))
print('Area = ',area(a,b))