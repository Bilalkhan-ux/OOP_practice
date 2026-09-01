# # class student():
# #     def __init__(self, name ,marks):
# #         self.name = name
# #         self.__marks = marks

# #     def setMarks(self, marks):
# #         self.__marks = marks
# #     def getMarks(self):
# #         return self.__marks    
# #     def display(self):
# #         print("Name: ", self.name)
# #         print("Marks: ", self.__marks)

# #     def isPassed(self):
# #         return self.__marks >50


# # student1 = student("Bilal", 99)
# # student2 = student("Mustafa", 57)

# # student1.display()        
# # student2.display()  

# # if student1.isPassed():
# #     print("Pass")
# # else:
# #     print("Failed")
# # if student2.isPassed():
# #     print("Pass")
# # else:
# #     print("Failed")

# # print(student1.getMarks())

# # class Person():
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age  

# # class   Student(Person):
# #     def __init__(self, name,age,rollno):
# #         super().__init__(name,age)
# #         self.rollno = rollno

# # student1 = Student("Bilal" ,15,2111)
# # print(student1.rollno)
# # print(student1.name)







# # class Person():
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age

# #     def introduce(self):
# #         print("I am person")

# # class Student(Person):
# #     def __init__(self, name, age, rollNo):
# #         super().__init__(name, age)
# #         self.rollNo = rollNo

# #     def introduce(self):
# #         print("Name: ", self.name)
# #         print("Age: ", self.age)
# #         print("Roll no: ", self.rollNo)
# # class Teacher(Person):
# #     def __init__(self, name, age,subject):
# #         super().__init__(name,age)
# #         self.subject = subject

# #     def introduce(self):
# #         print("Name: ", self.name)
# #         print("Age: ", self.age)
# #         print("Subject: ", self.subject)

# # student1 = Student("Bilal", 22, 21321)
# # teacher = Teacher("Sir", 44, "Science")

# # # student1.introduce()
# # # teacher.introduce()

# # people = [student1 , teacher]

# # for i in people:
# #     i.introduce()

# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def introduce(self):
#         print("Name: ",self.name)
#         print("Age: ",self.age)

# class Coder():
#     def __init__(self, lang):
#         self.lang = lang

#     def code(self):
#         print("Language: ", self.lang)

# class Student(Person, Coder):
#     def __init__(self,name,age,lang):
#         Person.__init__(self,name, age)
#         Coder.__init__(self, lang)

# student1 = Student("Bilal Khan", 22,"Python")
# student2 = Student("Ali Khan", 22,"Java")

# student1.introduce()
# student2.code()


class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)

class Student(Person):
    def __init__(self,name,age,marks):
        super().__init__(name,age)
        self.marks = marks

    def isPassed(self):
        return self.marks > 50

student1 = Student("Ahmad", 14 , 40)    
student2 = Student("Bilal", 22 , 99)

if student1.isPassed():
    print("PASS")
else:
    print("Fail")
if student2.isPassed():
    print("PASS")
else:
    print("Fail")