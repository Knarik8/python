"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке."""
with open("text_8.txt", "r", encoding="utf-8") as my_file:
    line = 0
    while True:
            c = my_file.readline()
            if not c:
                break
            line += 1
            for i in c.split():
                words = len(c.split())
            print(f"Количество слов в строке:{words}")
print(f"Количество строк:{line}")




