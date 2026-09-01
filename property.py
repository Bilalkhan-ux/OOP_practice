# class Person():
#     def __init__(self,name,age):
#         self.__name = name
#         self.__age = age

#     @property
#     def name(self):
#         return self.__name

#     @name.setter
#     def name(self,n):
#         self.__name = n

#     @property
#     def age(self):
#         return self.__age

#     @age.setter
#     def age(self,a):
#         if a > 0:
#             self.__age = a
#         else:
#             print("Age can't be less than 0")

# person = Person("Bilal", 21)
# print(person.name)
# person.name = "ALi"
# print(person.name)
# print(person.age)

class Student():
    school = "ABC school"
    def __init__(self,name,age):
        self.name = name
        self.age= age

    def introduce(self):
        print("Name:" , self.name)
        print("Age:" , self.age)
        print("School: ",self.school)

    @classmethod
    def changeSchool(cls):
        cls.school = "DEF school"

    @staticmethod
    def isAdult(age):
        return age >= 18

s1 = Student("Bilal", 22)
s1.introduce()
s1.changeSchool()
s1.introduce()

print(Student.isAdult(14))
print(Student.isAdult(19))