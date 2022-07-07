import random
import re


'''
age = int(input("please provide your age ---->"))
if age> 18:
    print(f"as your age is {age} and you can watch Thor Love & thunder")
    #if you dont want to write anything then write "pass" instead of a statement
else:
    print(f"as your age is {age} and you cannot watch Thor Love & thunder")

number = int(input("enter a number"))
required_number= random.randint(1,100)
print (required_number)
if number== required_number:
    print("you win the game")
else:
    
    if number<required_number: 
        print(" too low")
    else:
        print("too high")

# and // or
name, user_age = input("enter you name and age(comma seperated) ").split(",")
char = name[0].lower().strip()
if int(user_age)>= 18 and char == "a":
    print("you can watch the movie")
else:
    print("you cant watch the movie") 

    '''

'''theage= int(input("enter age"))
if theage<0:
    print("you cannot have that age -_-")
elif 0<=theage<=5:
    print("ticket free")
elif 6<=theage<=60:
        print("the fee is 200")
else:
    print("the free is 100")'''

#in and check for empty string
fname= input("please enter your first name")
sname= ""
if fname:

    if "h" in fname:
        print("h is present in your name")
    else:
        print("not present")
else:
    print("please input your name properly")
