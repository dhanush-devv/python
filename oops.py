# # class Employee:
# #     possition="SDE"
# #     salary=450000

# # content=Employee()
# # content.name="Dhanush" #instance attribute
# # content.salary=5000000
# # print(content.salary, content.possition,content.name)


# class Employee:
#     name="Dhanush"
#     salary=15000000


#     def __init__(self,name,language,salary):
#          print("Hello")
#          self.name=name
#          self.language=language
#          self.salary=salary
#          print("I am creating object")
         
#     def getInfo(self):
#         print(f"Name {self.name} salary {self.salary}")

#     @staticmethod
#     def greet():
#             print("Hello World!")

# content=Employee("Dhanush","MERN",150000)
# print(content.name,content.language)
# content.getInfo()
# content.greet()

# class Programmer:
#     company="Microsoft"

#     def __init__(self,name,salary,pincode):
#         self.name=name
#         self.salary=salary
#         self.pincode=pincode
    
# info=Programmer("Dhanush",1500000,576107)
# print(info.company,info.name,info.salary,info.pincode)


# class Calculator:
#     def __init__(self,n):
#         self.n=n
#     def square(self):
#         print(self.n*self.n)
#     def cube(self):
#         print(self.n*self.n*self.n)
#     def squareroot(self):
#         print(self.n**1/2)
# cal=Calculator(4)
# cal.square()
# cal.cube()
# cal.squareroot()

# from random import randint
# class Train:
#     def __init__(self,trainNo):
#         self.trainNo=trainNo
#     def book(self,fro,to):
#         print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")
#     def getStatus(self):
#          print(f"Train no :{self.trainNo} is running on time")
#     def getFare(self,fro,to):
#         print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222,5555)}")

# t=Train(12339)
# t.book("Udupi","Mangalore")
# t.getStatus()
# t.getFare("udupi","Mangalore")


# class Employee:
#     company="ITC"
#     def show(self):
#         print(f"Name is {self.name} and salary is {self.salary}")

# class Programmer(Employee):
#     company="ITC Infotech"
#     def showLanguage(self,name,language):
#         print(f"Name is {name} and language is {language}")

# a=Employee()
# b=Programmer()

# print(a.company,b.company)
# print(b.showLanguage("Dhanush","MERN"))


# class TwoDVector:
#     def __init__(self,i,j):
#         self.i=i
#         self.j=j

#     def show(self):
#         print(f"The vector is {self.i}i  +{self.j}j")


# class ThreeDVector(TwoDVector):
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.k=k
#     def show(self):
#         print(f"The vector is {self.i}i  +{self.j}j +{self.k}k")

# a=TwoDVector(1,2)
# a.show()
# b=ThreeDVector(1,2,3)
# b.show()

# class Animals:
#     pass

# class Pets(Animals):
#     pass

# class Dog(Pets):
#     @staticmethod
#     def bark():
#         print("Dog Barks")

# d=Dog()
# d.bark()

# class Employee:
#     salary = 1233333
#     increment = 50

#     @property
#     def salaryaAfterIncrement(self):
#         return self.salary + self.salary * self.increment / 100

#     @salaryaAfterIncrement.setter
#     def salaryaAfterIncrement(self, salary):
#         self.increment = ((salary / self.salary) - 1) * 100


# a = Employee()

# a.salaryaAfterIncrement = 280
# print(a.increment)


# class Complex:
#     def __init__(self,r,i):
#         self.r=r
#         self.i=i

#     def __add__(self,c2):
#         return Complex(self.r + c2.r, self.i+c2.i)
    
#     def __str__(self):
#         return f"{self.r}+{self.i}i"
    

# c1=Complex(1,2)
# c2=Complex(3,4)

# print(c1 + c2)



        
