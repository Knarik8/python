# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.
month = int(input("Введите месяц в виде целого числа от 1 до 12"))
winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
if month in winter:
    print(f"{month} месяц относится к зиме")
if month in spring:
    print(f"{month} месяц относится к весне")
if month in summer:
    print(f"{month} месяц относится к лету")
if month in autumn:
    print(f"{month} месяц относится к осени")