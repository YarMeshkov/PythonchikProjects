class operations:
    def plus(Number1, Number2):
        addiction = Number1 + Number2
        print(addiction)
    def minus(Number1, Number2):
        subtraction = Number1 - Number2
        print(subtraction)
    def multiply(Number1, Number2):
        multiplication = Number1 * Number2
        print(multiplication)
    def divide(Number1, Number2):
        divider = Number1 / Number2
        print(divider)
    def dividefully(Number1, Number2):
        dividerfully = Number1 // Number2
        print(dividerfully)
    def divideremainder(Number1, Number2):
        dividerremainder = Number1 % Number2
        print(dividerremainder)
    def degree(Number1, Number2):
        degreer = Number1 ** Number2
        print(degreer)

Number1 = int(input("Введите первое число:"))
Number2 = int(input("Введите второе число:"))
Operation = input("Введите знак операции, на выбор: +, -, *, /, //, %, **")
while not Operation == "+" and not Operation == "-" and not Operation == "*" and not Operation == "/" and not Operation == "//" and not Operation == "%" and not Operation == "**":
    print("Вы вписали постронний знак!")
    Operation = input("Введите знак операции, на выбор: +, -, *, /, //, %, **")
if Operation == "+":
    operations.plus(Number1, Number2)
elif Operation == "-":
    operations.minus(Number1, Number2)
elif Operation == "*":
    operations.multiply(Number1, Number2)
elif Operation == "/":
    while Number2 == 0:
        print("На ноль делить нельзя!")
        Number2 = int(input("Введите заново второе число:"))
    operations.divide(Number1, Number2)
elif Operation == "//":
    while Number2 == 0:
        print("На ноль делить нельзя!")
        Number2 = int(input("Введите заново второе число:"))
    operations.dividefully(Number1, Number2)
elif Operation == "%":
    while Number2 == 0:
        print("На ноль делить нельзя!")
        Number2 = int(input("Введите заново второе число:"))
    operations.divideremainder(Number1, Number2)
elif Operation == "**":
    operations.degree(Number1, Number2)