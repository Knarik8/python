# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
user_answer = int(input("Введите целое положительное число"))
maximal = 0
while user_answer > 0:
    n = user_answer % 10
    if n > maximal:
        maximal = n
    user_answer = user_answer // 10
print(f"Самая большая цифра в числе: {maximal}")


