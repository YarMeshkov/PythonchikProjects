print("Работа со списками")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.append(11)
numbers.insert(0, 0)
numbers.remove(5)
print(len(numbers))
for i in numbers:
    if i ** 2 > 25:
        print(i)

print("Работа с множествами")
fruits = {"apple", "banana", "cherry", "orange"}
fruits.add("kiwi")
fruits.remove("cherry")
print(len(fruits))
citrus = {"orange", "lemon", "grapefruit"}
print(fruits.union(citrus))
print(fruits.intersection(citrus))

print("Работа со словарями")
student = {"name": "John", "age": 15, "grade": 9}
student["school"] = "XYZ School"
student["grade"] = 10
del student["age"]
print(student.keys())
print(student.values())
if "name" in student:
    print("YES")
else:
    print("NO")

print("Работа с кортежами")
colors = ("red", "green", "blue")
print(colors[1])
print(len(colors))
numbers = (1, 2, 3)
combined = colors + numbers
print(combined[::1])

print("Работа со строками")
message = "Hello, world!"
print(len(message))
print(message.upper())
print(message[4:])
message = message.replace("o", "x")
if "world" in message:
    print("YES")
else:
    print("NO")