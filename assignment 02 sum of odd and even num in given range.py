# 2. Print the sum of odd and even numbers in a given range (using for loop)

print("Print the sum of odd and even numbers in a given range (using for loop)\n")

start=int(input("Enter the starting value = "))
end=int(input("Enter the ending value = "))
ans1=0
ans2=0
if start>=end:
    print("Enter the valide number")
else:
    for i in range(start,end+1):
        if ((i%2)==0):
            ans1=ans1+i
        else:
            ans2=ans2+i
    print(f"The sum of given Even Number = {ans1}")
    print(f"The sum of given odd Number = {ans2}\n\n")

# 2. Print the sum of odd and even numbers in a given range (using for while loop)

print("Print the sum of odd and even numbers in a given range (using for while loop)\n")

start=int(input("Enter the starting value = "))
end=int(input("Enter the ending value = "))
ans1=0
ans2=0
if start>=end:
    print("Enter the valide number")
else:
    while start<=end:
        if ((start%2)==0):
            ans1=ans1+start
        else:
            ans2=ans2+start
        start+=1
    print(f"The sum of given Even Number = {ans1}")
    print(f"The sum of given odd Number = {ans2}")

