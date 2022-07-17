# # list_of_numbers = [1,2,3,4,5]
# # list_of_evennumbers = [2,4,6]
# # list_of_oddnumbers = [1,3,5]


# # mixed = ["one",2,3.0,"Four",False]
# # for i in list_of_evennumbers:
# #     print (f"{i}\n")
# # list_of_oddnumbers[2] = False 
# # print(list_of_oddnumbers[2])

# # print(type(mixed))

# # # 2) add data to list ---> append() method 
# # list_of_numbers = [1,2,3,4,5]
# # list_of_numbers.append(6)
# # list_of_numbers.insert(2,11)  # position = 2 
# # print(list_of_numbers)

# fruits1 = ["apple","mango","banana"]
# fruits2= ["graoes","watermelon","guava","guava"]

# fruits1.pop(0)      #position 

# print(fruits1)

# del fruits1[1]
# print(fruits1) 


# # 4) in keyword in list 
# if "apple" in fruits1: 
#     print("Present")
# else: 
#     print("Absent")

# print(fruits2.count("grapes")) 
# fruits2.sort()
# print(fruits2) 



# fruits2.reverse()
# fruits3 = fruits2.copy() 
# print(fruits2) 

# fruits2.clear()
# print(fruits2) 
# print(fruits3) 

# # Is vs Equal

# fruits5 = ["apple","mango","banana"]
# fruits6 = ["apple","mango","banana"]

# print(fruits5 == fruits6) # Check for same value as well as num 

# print(fruits5 is fruits6) # Check for the location ofobjext in memory i.e RAM 

# def give_me_list(num):
#     my_list = []
#     for i in range(0,num+1):
#         my_list.append(i)
#     return my_list

# mero_list = give_me_list(10) 
# print (mero_list)


        
'''def qs(num): 
    my_list = [] 
    for i in range(0,num+1):
        my_list.append(i**2)
    return my_list

mero_list = int(input("Enter number")) 
new_list = qs(mero_list)
print (new_list)'''

'''any = ["aryama","kritika","rushav","samay","maharshi"]

def reserse_item(a_list):
    newlist=[]
    for i in a_list:
        newlist.append(i[::-1])
    return(newlist)

returned_value= reserse_item(any)
print(returned_value)        '''

from telnetlib import theNULL


my_list= [10,9,8,7,6,5,4,3,2,1,0]

def diff_lists(a_list):
    odd_list=[]
    even_list=[]
    final_list=[]
    for i in a_list:
        if i % 2==0:
            even_list.append(i)
        else:
            odd_list.append(i)   
    final_list.append(even_list)
    final_list.append(odd_list)

    return(final_list)
returned_value= diff_lists(my_list)
print(returned_value)

def counter(another_list):
    count=0
    for i in another_list:
        if type(i)==list:
            count= count+1
    return count        

print(counter(diff_lists(my_list)))

