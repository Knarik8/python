"""7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста."""
import json

with open("text_7.txt", "r", encoding="utf-8") as my_file:
    my_list = []
    name_list = []
    sum_list = []
    summa = 0
    count = 0
    while True:
        c = my_file.readline().split()
        if not c:
            break
        for i in c:
            viruchka = c[2]
            izderjki = c[3]
            name = c[0]
            name_list.append(name)
            pribil = int(viruchka) - int(izderjki)
            sum_list.append(pribil)
        if pribil > 0:
            summa += pribil
            count += 1
        average_profit = summa / count
    my_dict1 = (dict(zip(name_list, sum_list)))
    my_dict2 = dict(Средняя_прибыль = average_profit)
    my_list.append(my_dict1)
    my_list.append(my_dict2)

with open("text_777.json", "w", encoding="utf-8") as write_f:
    json.dump(my_list, write_f, ensure_ascii=False)


