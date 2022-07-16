def greatest(num1,num2,num3):
    high=0
    if num1>num2:
        high = num1 
       
    elif num2>num1:
        high=num2
    if num3>high:
            high=num3
    return high

print(greatest(12,16,78))