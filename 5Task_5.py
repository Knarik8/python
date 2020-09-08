"""5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""
from random import randrange


with open("text_5.txt", "w", encoding="utf-8") as my_file:
    my_list = []
    while len(my_list) < 10:
        my_list.append(randrange(10, 99))
    my_file.write(str(my_list))
    print(sum(my_list))
