"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников."""
with open("text_3.txt", "r", encoding="utf-8") as my_file:
    summa = 0 
    workers_count = 0
    workers = []

    for i in my_file:
        workers_count += 1
        surname = str(i).split()[0]
        money = str(i).split()[1]
        summa += float(money)
        if float(money) < 20000.0:
            workers.append(surname)
    print(f"Сотрудники с окладом менее 20 тыс.: {workers}")
    print(f"Cредняя величина дохода сотрудников: {summa / workers_count}")






