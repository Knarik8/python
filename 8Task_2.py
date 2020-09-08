"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа
должна корректно обработать эту ситуацию и не завершиться с ошибкой."""

class OwnError(Exception):
    pass

inp_delim = input("Введите делимое: ")
inp_delit = input("Введите делитель: ")


try:
    result = int(inp_delim) / int(inp_delit)
    if inp_delit == 0:
        raise OwnError("Делить на ноль нельзя!")
except ValueError:
    print("Вы ввели не число")
except (OwnError, ZeroDivisionError) as err:
    print(err)
else:
    print(f"Ответ: {result}")