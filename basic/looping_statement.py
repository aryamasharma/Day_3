'''i = 0 
while i<10:
    print(f"hello world {i}")
    i+= 1

for j in range(0,10):
    print(f"for loop ")
'''

'''user_number = int(input("enter a number: "))
sum = 0 
for j in range(0,user_number+1):
    sum += j
print(sum)

sum1= 0
i=0
while i<= user_number:
    sum1 += i
    i += 1 
print(sum1)    
'''

'''user_number = input("enter a 4 digit number: ")
sum = 0 
for i in range(0,len(user_number)):
    sum+= int(user_number[i])
print(sum) 

sum1= 0 
j=0
while j< len(user_number):
    sum1 += int(user_number[j])
    j+= 1
print(sum1)    
'''
'''user_input = input("enter your name")
repeat_store = ""
for j in range(0,len(user_input)):
    if user_input[j] not in repeat_store:
        repeat_store+= user_input[j]
        char = user_input[j].lower()
        count = user_input.lower().count(char)
        print(f"the number of {char} is {count}")'''
import random
'''#break and continue keyword
for i in range(1,10):
    if i==5:
        continue
    print(f"the new number is {i}")

usernumber = input("enter a number")
sum =0  
for i in usernumber:
    sum += int(i)
print(sum)
'''
'''guess= 1
number = int(input("enter a number"))
required_number= random.randint(1,100)
print (required_number)
while number != required_number:
    if number< required_number:
        number=int(input("enter a higher number"))
        
    else:
        number = int(input("enter a lower number"))
    guess += 1

print(f"you winnn with {guess} guesses")
'''


 
