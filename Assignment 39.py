# Write a program to generate and print another tuple whose values are even 
# numbers in the given tuple (1,2,3,4,5,6,7,8,9,10)


tu = (1,2,3,4,5,6,7,8,9,10)
print("Before Tuple edit = ", tu)
list1=[]
for i in range(len(tu)):
    if(tu[i] % 2 == 0):
        print(tu[i], end = "  ")
        list1.append(tu[i])
print("\nAfter edit the tuple : ",tuple(list1))