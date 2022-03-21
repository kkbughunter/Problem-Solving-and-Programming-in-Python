start=int(input("Enter the starting number = "))
end=int(input("Enter the ending number = "))
ans=0
if start>=end:
     print("Please enter the valide number :(")
else:
     for i in range(start,end+1):
          ans=ans+i
     print("The total of given number is = ",ans)