Operation = input("Напишите операцию, на выбор: записать в файл, дозаписать в файл, считать из файла, выйти.")
Operation = Operation.lower()
while Operation != "выйти":
    if Operation == "записать в файл":
        Write = input("Впишите, то что хотите записать в файл:")
        with open("hw_txt.txt", "w") as file:
            file.write(Write)
    elif Operation == "дозаписать в файл":
        Write = input("Впишите, то что хотите дозаписать в файл:")
        with open("hw_txt.txt", "a") as file:
            file.write(Write)
    elif Operation == "считать из файла":
        with open("hw_txt.txt", "r") as file:
            print(file.read())
    Operation = input("Напишите операцию, на выбор: записать в файл, дозаписать в файл, считать из файла, выйти.")
file.close()