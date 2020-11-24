"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл."""

with open("text_4.txt", "r", encoding="utf-8") as my_file:
    num = []
    for i in my_file:
        One_Two_Three_Four = str(i).split()[2]
        num.append(One_Two_Three_Four)

l = ["один", "два", "три", "четыре"]

with open("text_4_2.txt", "w", encoding="utf-8") as new_file:
    new_file.write(f"{l[0]} - {num[0]}\n")
    new_file.write(f"{l[1]} - {num[1]}\n")
    new_file.write(f"{l[2]} - {num[2]}\n")
    new_file.write(f"{l[3]} - {num[3]}")
