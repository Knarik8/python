# 6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например название,
# а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }
count = int(input("Какое количество товаров хотите ввести?\n"))
my_list = []
result_dict = {"название": set(),
               "цена": set(),
               "количество": set(),
               "ед": set()}
for i in range(count):
    name = input("Введите название товара\n")
    result_dict["название"].add(name)
    price = int(input("Введите цену товара\n"))
    result_dict["цена"].add(price)
    number = int(input("Введите количество товара\n"))
    result_dict["количество"].add(number)
    unit = input("Введите единицу измерения\n")
    result_dict["ед"].add(unit)
    my_dict = {"название": name, "цена": price, "количество": number}
    my_tuple = (i + 1, my_dict)
    my_list.append(my_tuple)
print(my_list)
print(result_dict)

