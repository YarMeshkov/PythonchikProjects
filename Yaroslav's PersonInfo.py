class Person:
    def info(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def introduce(self):
        print(f"Имя: {self.name}, возраст: {self.age}, пол: {self.gender}")

class Student(Person):
    def info(self, name, age, gender, id):
        self.id = id
    def introduce(self):
        print(f"Имя: {self.name}, возраст: {self.age}, пол: {self.gender}, номер студента: {self.id}")

class Teacher(Person):
    def info(self, name, age, gender, subject1):
        self.subject1 = subject1
    def introduce(self):
        print(f"Имя: {self.name}, возраст: {self.age}, пол: {self.gender}, предмет: {self.subject1}")

p1 = Person()
p1.name = "Василий"
p1.age = 26
p1.gender = "мужской"
Person.introduce(p1)
p2 = Student()
p2.name = "Анна"
p2.age = 19
p2.gender = "женский"
p2.id = "123456"
Person.introduce(p2)
p3 = Teacher()
p3.name = "Дмитрий"
p3.age = 45
p3.gender = "мужской"
p3.subject1 = "математика"
Person.introduce(p3)