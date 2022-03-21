# Question
# 1. Print all the odd numbers and even numbers in a given range

start=int(input("Enter the starting value = "))
end=int(input("Enter the ending value = "))

for i in range(start,end):
    if ((i%2)==0):
        print(f"The {i} is Even Number")
    else:
        print(f"The {i} is Odd Number")








