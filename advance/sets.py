set1= {"k","r","i","t","i","k","a"}
print(set1)

if "r" in set1:
    print ("present")
else:
    print("not present")    

for i in set1:
    print (i)

set2 ={"m","a","h","a","r","s","h","i"}

union_set = set1 | set2
intersection_set = set1 & set2

print(f"the union of two sets are: ---> {union_set}")
print(f"the intersection of two sets are: --> {intersection_set}")

    