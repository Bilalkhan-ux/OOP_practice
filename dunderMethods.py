# # # class Battery():
# # #     def start(self):
# # #         print("Battery started")

# # # class Phone():
# # #     def __init__(self):
# # #         self.battery = Battery()

# # #     def startPhone(self):
# # #         self.battery.start()
# # #         print("Phone started")

# # # phone = Phone()
# # # phone.startPhone()

# # #aggregation

# # # class Student:
# # #     def __init__(self,name):
# # #         self.name = name


# # # class Classroom:
# # #     def __init__(self,name):
# # #         self.student = name

# # #     def display(self):
# # #         print("Name: ", self.student.name)

# # # student = Student("Bilal")  
# # # classroom = Classroom(student)
# # # classroom.display()

# class Book:
#     def __init__(self,title,author,price):
#         self.title = title
#         self.author = author
#         self.price = price

#     def __str__(self):
#         return f"Title: {self.title}, Author: {self.author}, Price: {self.price}"

#     def __len__(self):
#         return len(self.title)


# book = Book("45", "Bilal", 1500)
# print(book)
# print (len(book))


# # #__eq__()


# # class book():
# #     def __init__(self,name,price):
# #         self.name = name
# #         self.price = price

# #     def __add__(self, other):
# #         return self.price + other.price

# # book1= book("40 rules", 499)
# # book2= book("40 rules",899)

# # print(book1+book2)

class Inventory:
    def __init__(self,name , price):
        self.name = name
        self.price = price

    def __lt__(self,other):
        return self.price < other.price
    def __gt__(self,other):
        return self.price > other.price
    def __le__(self,other):
        return self.price <= other.price
    def __ge__(self,other):
        return self.price >=other.price
    def __str__(self):
        return f"Name: {self.name},Price: {self.price}"
    def __len__(self):
        return len(self.name)
    def __eq__(self,other):
        return self.price == other.price
    def __add__(self,other):
        return self.price+other.price 

item1 = Inventory("Ball", 99)
item2 = Inventory("Bat", 100)

print(item1 < item2)
print(item1 > item2)
print(item1 <= item2)
print(item1 >= item2)
print(item1)
print(len(item1))
print(item1==item2)
print(item1+item2)