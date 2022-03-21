# Write a program which can filter even numbers in a list by using 
# filter function. The list is:[1,2,3,4,5,6,7,8,9,10]
def even(n):
    if n%2==0:
        return n
list1= [1,2,3,4,5,6,7,8,9,10]
lis2 = list(filter(even, list1))
print(lis2)


















