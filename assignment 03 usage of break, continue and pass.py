# 3. Demonstrate the usage of break, continue and pass statements

# break
start=int(input("the starting value is = "))
print("Notes : please give the break number below ending value")
bre=int(input("in which place you want to break = "))
end=int(input("enter the ending value = "))
for i in range(start,end+1):
    if i ==bre:
        print("i have give contision to break  ")
        break
    print(i)

#----------------------------------------------------------------------------#

# continue
start=int(input("the starting value is = "))
print("Notes : please give the skip number below ending value")
con=int(input("in which place you want to skip = "))
end=int(input("enter the ending value = "))
for i in range(start,end+1):
    if i ==con:
        print("the value is skiped")
        continue
    print(i)

#----------------------------------------------------------------------------#

# pass
start=int(input("Enter the starting value = "))
s_err=int(input("Enter the remove-start value : "))
e_err=int(input("Enter the remove-end value : "))
end=int(input("Enter the endting value = "))
for i in range(start,end+1):
  if i not in range(s_err,e_err+1):
    print(i)
    pass

#----------------------------------------------------------------------------#


