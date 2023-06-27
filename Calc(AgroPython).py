Number1 = int(input("Введите первое число:"))
Number2 = int(input("Введите второе число:"))
Operation = input("Введите знак операции, на выбор: +, -, *, /, //, %, **")
while not Operation == "+" and not Operation == "-" and not Operation == "*" and not Operation == "/" and not Operation == "//" and not Operation == "%" and not Operation == "**":
    print("Вы вписали постронний знак!")
    Operation = input("Введите знак операции, на выбор: +, -, *, /, //, %, **")
if Operation == "+":
    Summa = Number1 + Number2
    print(Summa)
elif Operation == "-":
    Raznost = Number1 - Number2
    print(Raznost)
elif Operation == "*":
    Proizvedenie = Number1 * Number2
    print(Proizvedenie)
elif Operation == "/":
    while Number2 == 0:
        print("На ноль делить нельзя!")
        Number2 = int(input("Введите заново второе число:"))
    Delenie1 = Number1 / Number2
    print(Delenie1)
elif Operation == "//":
    while Number2 == 0:
        print("На ноль делить нельзя!")
        Number2 = int(input("Введите заново второе число:"))
    Delenie1 = Number1 // Number2
    print(Delenie1)
elif Operation == "%":
    while Number2 == 0:
        print("На ноль делить нельзя!")
        Number2 = int(input("Введите заново второе число:"))
    Delenie1 = Number1 % Number2
    print(Delenie1)
elif Operation == "**":
    Stepen = Number1 ** Number2
    print(Stepen)