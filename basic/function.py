'''#function define with parameter
def name(needavalue):
    print(f"any {needavalue}")

#function calling with argument 
print(name(", Hello"))'''

'''def name_and_age(yname,yage):
    print(f"your name is {yname} and your age is {yage}")

name, age= input("enter your name and age (comma seperated) ").split(",")
print(name_and_age(name,age))'''

'''def odd_or_even(number):
    if number%2==0:
        return(f"the number {number} is even")

    return(f"the number {number} is odd")'''

'''def odd_or_even(number):
    return number%2==0 
num = int(input("enter a number to check"))
return_value = odd_or_even(num)
print (return_value)
'''

'''def palindrome(string):
    return string[::-1].lower() == string.lower()
string = input("enter a string: ")
return_value = palindrome(string)
print(return_value)'''

'''def greater(num1,num2):
    if num2>num1:
        return (f"{num2} is greater than {num1}")
    else:
        return (f"{num1} is greater than {num2}")
3,2,1 
3>2>1
fnum,fsnum = input("enter two nums comma seperated: ").split(",")
print(greater(int(fnum),int(fsnum)))'''

def greater(num1,num2,num3):
    high=0 
    if num1> num2:
        high = num1
        if num3>high:
            high= num3
    elif num2>num1:
        high = num2
        if num3>high:
            high=num3
    else:
        high = num3 
    return high


fnum,snum,tnum = input("enter three nums comma seperated: ").split(",")
print(greater(int(fnum),int(fnum),int(tnum)))

'''def greatest(a,b,c):
    greater_of_two_num= greater(a,b)
    return greater(greater_of_two_num,c)'''

def greatest(a,b,c):
    return greater(greater(a,b),c)
anything= greatest(int(first),int(second),int(third))
print(anything)