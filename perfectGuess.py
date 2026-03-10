import random
n=random.randint(1,100)


guesses=1
a=-1
while(a!=n):
    a=int(input("Enter a number "))
    if(a>n):
        print("Lower number! ")
        guesses+=1
    elif(a==n):
        print("You guessed right number ")
        guesses+=1
    else:
        print("Higher number")
        guesses+=1
print(f"You guessed in {guesses} attempt")