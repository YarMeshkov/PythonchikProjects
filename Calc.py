def Plus(Number1, Number2):
    Summa = Number1 + Number2
    return Summa
def Subtract(Number1,Number2):
    Raznost = Number1 - Number2
    return Raznost
def Multiply(Number1, Number2):
    Proizvedenie = Number1 * Number2
    return Proizvedenie
def Divide(Number1,Number2):
    Delenie = Number1 / Number2
    return Delenie

Number1 = int(input("Введите первое число:"))
Number2 = int(input("Введите второе число:"))
Operation = input("Введите знак операции, на выбор: +, -, *, /")

if Operation == "+":
    print(Plus(Number1, Number2))
elif Operation == "-":
    print(Subtract(Number1, Number2))
elif Operation == "*":
    print(Multiply(Number1, Number2))
elif Operation == "/":
    if Number2 == 0:
        print("Иди матешу учи! На ноль делить нельзя!")
    else:
        print(Divide(Number1, Number2))
else:
    print("Братан, ты не врубаешься? Мне нужен знак операции из списка!")