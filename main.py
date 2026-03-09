#print("Hello World!")

#module
#import pyjokes

#joke=pyjokes.get_joke()
#print(pyjokes.get_joke())
"""
multline
Commetn
"""

'''
hello
'''
# print("hi")


# Practice set 1

# print(
# """Twinkle, Twinkle, Little Star
# Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.

# Twinkle, twinkle, little star,
# How I wonder what you are! ⭐"""
# )

# import text_to_image

# encoded_image_path = text_to_image.encode("Hello World!", "image.png")
# encoded_image_path = text_to_image.encode_file("hello.txt","output_image.png")

# decoded_text = text_to_image.decode("encoded_image.png")
# decoded_file_path = text_to_image.decode_to_file("encoded_image.png","output_text_file.txt")

# import pyttsx3
# engine = pyttsx3.init()

# engine.say("okkkkkkkkkkkkkkkkkkkkkkkk")
# engine.runAndWait()

# import os
# directory_path='/'

# content=os.listdir(directory_path)

# for item in content:
#     print(item)

# Variables and datatypes

# a=1
# b=2
# print(a+b)

# a="Dhanush"
# b="Nayak"
# print(a+" "+b)

# a=1
# b="string"
# c=2
# b=c
# print(b)

# print(bool(""))

# e=None
# print(e)

# Arithmatic operator

# a=1
# b=2
# print(a+b)
# print(a-b)


# a=1
# b=2
# print(a==b)

# print(a>b)

# print(a<b)

# print(a!=b)

# logical operator 

# e= True or False
# e=True and False
# print(e)

# a=True
# print(not a)

# type casting

# a=1
# print(type(a))

# b=str(a)
# print(type(b))

# a=10.0
# b=int(a)
# print(type(b))

# a=int(input("Enter a: "))
# b=int(input("Enter a: "))
# sum=a+b
# print("sum is ", sum)

# Practice set 2
# a=10
# b=20
# print(a+b)

# a=4
# b=2
# print(a%b)

# n=input("Enter")
# print(type(n))

# a=34
# b=80
# print(a>b)

# a=int(input("Enter a: "))
# b=int(input("Enter b: "))
# print("Average: ",(a+b)/2)

# a=int(input("Enter a: "))
# print("Square of",a,"is",a*a)

# a=int(input("Enter a: "))
# print("Square of",a,"is",a**2)

# chapter 3 ->Strings -> Strings are immutable

# a="Dhanush"
# print(type(a))

# name="Dhanush"
# print(len(name))
# nameshort=name[0:4]
# print(nameshort)

# word="amazing"
# print(word[1:6:2]) #skip

# name="DHANUSH"
# print(len(name))
# print(name.endswith("H"))
# print(name.startswith("dH"))
# print(name.capitalize())

# name=input("Enter name: ")
# print(name,"Good afternoon")

# name="Dhanush"
# date="13-03-2026"
# print(f"""
# Dear  {name},
# You are selected!
# {date},
# """)



# str="Hello  world"

# # print(str.find("  "))
# print(str.replace("  "," "))

# friends=["Rohan","Akash","Dhanush"]
# print(friends[0])
# friends[0]="shailesh"
# print(friends)


#tupple
# a=(1,2,3,4,5,1,1,1,1,1,1,1,1,6)
# print(a.count(1))

# b=(1,)
# print(type(b))

# fruits=[]

# for i in range(0,7):
#     n=input("Enter fruits")
#     fruits.append(n)

# print(fruits)

# marks=[]

# for i in range(0,6):
#     n=int(input("Enter marks "))
#     marks.append(n)
# print(marks)
# marks.sort()
# print(marks)

# num=[1,2,3]
# sum=0
# for i in num:
#     sum=sum+i
# print(sum)

# a=(7,0,8,0,0,0,9)
# b=a.count(0)
# print(b)

# mark={
#     "Dhanush":100,
#     "shubam":75,
#     "Rohan":54
# }
# mark["Dhanush"]=99

# print(mark["Dhanush"])
# print(type(mark))

# print(mark.items())

# s=set() #empty sets
# s.add(10)
# print(s)

# translate={
#     "namaste":"Hello",
#     "koni chiwa":"How are you"
# }

# search=input("Enter the thing that u want to search from dictonary ")

# print(translate.get(search))

# s=set()
# for i in range(0,8):
#     n=int(input("Enter the number: "))
#     s.add(n)
# print(s)

# s={8,'8'}
# print(s,type(s))

# d={}
# for i in range(0,4):
#     name=input("Enter your name ")
#     language=input("Enter your favourite programming langauge ")
#     d.update({name:language})
# print(d)

# s={8,7,12,"Harry"}
# s.remove(7)
# print(s)

# age=int(input("Enter your age: "))
# if n%2==0:
#     print("even")
# else:
#     print("odd")

# if(age>=18):
#     print("You are eligible to vote")
# elif(age<0):
#     print("Please provide valid age")
# else:
#     print("You are not eligible to vote")


# a=int(input("Enter a number: "))
# b=int(input("Enter a number: "))
# c=int(input("Enter a number: "))
# d=int(input("Enter a number: "))

# if(a>b and a>c and a>d):
#     print(f"{a} is greater")
# elif(b>a and b>c and b>d ):
#     print(f"{b} is greater")
# elif(c>a and c>b and c>d ):
#     print(f"{b} is greater")
# else:
#     print(f"{d} is greater")

# a=int(input("Enter marks: "))
# b=int(input("Enter marks: "))
# c=int(input("Enter marks: "))



# total_percentage=((a+b+c)/300)*100
# print(int(total_percentage))

# if(total_percentage>=40 and a>=33 and b>=33 and c>=33):
#     print("You are pass")
# else:
#     print("Fail")

# p1="Make a lot of money"
# p2="buy now"
# p3="subscribe this"
# p4="click this"

# message=input("Enter message")

# if(p1 in message or p2 in message or p3 in message or p4 in message):
#     print("Spam")
# else:
#     print("hello world")


# for i in range(1,101):
#     print(i)

# i=1
# while(i<=5):
#     print(i)
#     i=i+1

# list=['Dhanush','Shailesh','Nithin',1,3,4,5,6]

# i=0
# while i<len(list):
#     print(list[i])
#     i=i+1

# l1=[1,2,3]
# l2=[4]
# print(l1+l2)

# for i in range(0,100):
#     if i==3:
#         continue;
#     print(i)

# for i in range(0,100):
#     if i==3:
#         break;
#     print(i)

# for i in range(0,11):
#     if i==3:
#         pass;
#     print(i)

# n=int(input("Enter a number : "))
# for i in range(1,11):
#     print(f"{n} x {i} = {n*i}")

# l=["Harry","Soham","Sachin","Rahul"]

# for name in l:
#     if(name.startswith("S")):
#         print(f"Hello {name}")

# n=int(input("Enter a number : "))
# i=0
# while(i<=10):
#      print(f"{n} x {i} = {n*i}")
#      i+=1

# n=int(input("Enter a number: "))

# for i in range(2,n):
#     if(n%i==0):
#         print(f"{n} Not a prime")
#         break;
# else:
#     print(f"{n}  a prime")

# sum=0
# i=1
# while(i<=10):
#     sum+=i
#     i+=1
# print(sum)

# n=int(input("Enter a number: "))
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)

# n=3
# for i in range(0,n):
#     print(" "*(n-i-1) + "*"*(2*i+1))

# n=3
# for i in range(1,n+1):
#     print("*"*i,end="")
#     print("")
# n=5
# for i in range(0,n):
#     for j in range(0,n):
#         if(i==0 or j==0 or i==n-1 or j==n-1):
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print("")

# n=5
# for i in range(10,0,-1):
#     print(f"{n}x{i}={n*i}")


# def function(name="Virat kohli"):
#     print("Good Day! ", name)


# function()


# def factorial(n):

#     if(n<2):
#         return 1
#     else:
#         return n*factorial(n-1)
    
# a=factorial(5)
# print(a)


# def greatest(a,b,c):
#     if(a>b and a>c):
#         print(f"{a} is greater")
#     elif(b>a and b>c):
#         print(f"{b} is greater")
#     else:
#         print(f"{c} is greater")

# greatest(1,2,3)

# def celToFar(cel):
#     return (cel*1.8)+32

# print(celToFar(66))

# def naturalSum(n):
#     if n==0:
#         return 0
#     return n+naturalSum(n-1)

# print(naturalSum(10))
# n=3
# for i in range(0,n):
#     print("*"* (n-i))

# f=open("file.txt","r")
# data=f.read()
# print(data)
# f.close()

# st="Hey"
# f=open('file.txt','w')
# f.write(st)
# f.close()

# with open("poem.txt",encoding="utf-8") as f:
#     data=f.read()
#     print(data)
#     if("twinkle" in data):
#         print("true")
#     else:
#         print("false")


# import random
# def game():
#     print("You are playing the game")
#     score=random.randint(1,62)

#     with open("hiscore.txt") as f:
#         hiscore=f.read()
#         if(hiscore!=""):
#             hiscore=int(hiscore)
#         else:
#             hiscore=0

#     print(f"Your score:{score}")

#     if(score>hiscore or hiscore==""):
#         with open("hiscore.txt","w") as f:
#             f.write(str(score))
#     return score
# game()
# def generateTable(n):
#     table=""
#     for i in range(1,11):
#         table+=f"{n} x {i} = {n*i}"

#     with open(f"tables/table_{n}.txt","w") as f:
#         f.write(table)




# for i in range(2,21):
#   generateTable(i)

# with open("donkey.txt") as f:
#     data=f.read()

# newData=data.replace("Donkey","######")

# with open("donkey.txt","w") as f:
#     f.write(newData)














         















