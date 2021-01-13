def is_allergen(product):
    if product == "апельсин" or product == "арахис" or product == "морепродукты" or product == "мёд":
        return True
    else:
        return False 

product = input('Введите название продукта ')
if is_allergen(product):
    print('Есть вероятность аллергической реакции')
else:
    print('Продукт безопасен')