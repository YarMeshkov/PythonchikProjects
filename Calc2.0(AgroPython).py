def Plus(Number1, Number2):
    Summa = Number1 + Number2
    return Summa
def Subtract(Number1,Number2):
    Raznost = Number1 - Number2
    return Raznost
def Multiply(Number1, Number2):
    Proizvedenie = Number1 * Number2
    return Proizvedenie
def Divide(Number1, Number2):
    Delenie = Number1 / Number2
    return Delenie
def DivideFully(Number1, Number2):
    Delenie2_0 = Number1 // Number2
    return Delenie2_0
def DivideRemainder(Number1, Number2):
    Delenie2_0 = Number1 % Number2
    return Delenie2_0
def Degree(Number1, Number2):
    Stepen = Number1 ** Number2
    return Stepen

Number1 = int(input("Введите первое число:"))
Number2 = int(input("Введите второе число:"))
Operation = input("Введите знак операции, на выбор: +, -, *, /, //, %, **")
while not Operation == "+" and not Operation == "-" and not Operation == "*" and not Operation == "/" and not Operation == "//" and not Operation == "%" and not Operation == "**":
    print("Вы вписали постронний знак!")
    Operation = input("Введите знак операции, на выбор: +, -, *, /, //, %, **")
if Operation == "+":
    print(Plus(Number1, Number2))
elif Operation == "-":
    print(Subtract(Number1, Number2))
elif Operation == "*":
    print(Multiply(Number1, Number2))
elif Operation == "/":
    while Number2 == 0:
        print("На ноль делить нельзя!")
        Number2 = int(input("Введите заново второе число:"))
    print(Divide(Number1, Number2))
elif Operation == "//":
    while Number2 == 0:
        print("На ноль делить нельзя!")
        Number2 = int(input("Введите заново второе число:"))
    print(DivideFully(Number1, Number2))
elif Operation == "%":
    while Number2 == 0:
        print("На ноль делить нельзя!")
        Number2 = int(input("Введите заново второе число:"))
    print(DivideRemainder(Number1, Number2))
elif Operation == "**":
    print(Degree(Number1, Number2))