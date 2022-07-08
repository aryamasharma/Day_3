'''
first_name , second_name = input("please provide your full name(space seperated): ").split(" ")
print("your full name is ---> " +first_name + " "+ second_name)
first_name , second_name = input("please provide your full name(comma seperated): ").split(",")
print("your full name is ---> " +first_name + " "+ second_name)
name_type = type(first_name)
print("type of firstname is ", name_type)
print("type of second is ", type(second_name))
print(2+3)
'''

first_num ,second_num, third_num = input("enter three numbers(comma seperated):").split(",")
first = int(first_num)
second= int(second_num)
third = int(third_num)

average= (first + second + third)//3 
print("the average is :" , average )


'''#string indexing
# 01234567
from dataclasses import replace'''


name = "language"
#print(name[5])
#print(name[-1])

#print(name[3:8])

#print(name[3:8:2])
print(name[7:0:-1]) #??????????????
print(name[-1::-1])
#print (len(name))
print(name[-1:-9:-1])
#string method
'''
example = "LeArN pYtHoN"
print(example.upper())
print(example.lower())
print(example.title())

print(example.count("a"))

full_name = input("enter your full name space seperated : ")
print(full_name.lower().count("a"))
'''
'''
full_name, character = input("enter your fullname and character you want to search (comma seperated)").split(",")
print("your name is : " , full_name , "the character count is" , full_name.lower().count(character)) #python2

print("your full name is {} and '{}' char count is {}".format(full_name,character, full_name.lower().count(character)))  #python3
charcount=  full_name.lower().count(character)
print(r"your fullname is {full_name} and '{character} character count is {charcount} ")
'''
'''
#solved problem with spaces : lstrip(), rstrip(),strip()
spaces_problem= "        aryama        "
stars="**********"
print(stars+spaces_problem+stars)
print(stars+spaces_problem.lstrip()+stars)
print(stars+spaces_problem.rstrip()+stars)
print(stars+spaces_problem.strip()+stars)

full_name, character = input("enter your fullname and character you want to search (comma seperated)").split(",")
charcount=  full_name.lower().count(character.strip())
print(f"your name is {full_name} \nthe character to count is {character} \nthe character number is {charcount}")
solved_problem = spaces_problem.replace(" ","")
print(f"the solve of spaces problem is : {solved_problem}")

replace_example = "kritika is a beautiful and she is out standing "
print(replace_example.replace("is","was"))
print(replace_example.replace("is","was",1))
insdez= replace_example.find("is", 1)
print(replace_example.find("is", insdez+1))'''


# print(replace_example.replace("is","was", replace_example.find("is,10")))
'''

#center() method

example2= "python"
print(example2.center(4+6+4,"*"))

#name= input("enter your name ")
#print(name.center(5+len(name)+5,"*"))



#string are imutable and assignment operator 
example3= "any"
#example3[1]="N" #can't do because of imutable (copy hancha)

print(example3.replace("n","N"))
print (example3)

example3= example3 + "body" # is the same as example += "body"
print(example3)
'''

replace_example = "kritika is a beautiful and she is out standing "

insdez= replace_example.find("is", 1)
print(replace_example.find("is", insdez+1))
half_sentence= replace_example[replace_example.find("is", insdez+1):].replace("is","was",1)
full_sentence= replace_example[:replace_example.find("is", insdez+1)] + half_sentence
print(full_sentence)
