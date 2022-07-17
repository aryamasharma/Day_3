from venv import create


one_tuple = ("monday",)
print(type(one_tuple))

#tuple unpacking (js object de-structuring) same value:
days=("sunday","monday","tuesday")
day1,day2,day3=days
print(day1)
print(day2)
print(day3)

#function returning two values
def calculator(num1,num2):
    sum=num1+num2
    multiplyTwo= num1*num2
    return(sum,multiplyTwo)

returned_value= calculator(4,5)
print(f"the value is :{returned_value}")
print(f"the type of returned value is : {type({returned_value})}")

sum1,multiply= returned_value
print(f"the multiple of two values is {multiply}")

#list inside tuples:
tuple_a = (1,2,3,[4,5,6],7,8,9)
print(tuple_a[3])
print(tuple_a[3][1])
#tuple_a[3]="kritika" cant assign cause tuples are immutable
tuple_a[3][1]="kritika"
print(tuple_a)
tuple_b=(0,1,2,3,4,56,7,8,9)
print(min(tuple_b))
print(max(tuple_b))
print(sum(tuple_b))

'''
searched_value= "sth"
left_pointer=0
right_pointer=len(tuple_a)-1
mid_pointer=(left_pointer+right_pointer)/2
if value< mid_pointer:
    right_pointer = mid_pointer

'''

#more about tuples:
# creating new tuple from range function as like list
new_tuples = tuple(range(1,11))
print(new_tuples)

create_list_from_tuples = list(new_tuples)
print(f"the list is: {create_list_from_tuples} and its type is: {type(create_list_from_tuples)}")
create_string_from_tuples= str(new_tuples)
print(f"the string is: {create_string_from_tuples} and its typr is: {type(create_string_from_tuples)}")