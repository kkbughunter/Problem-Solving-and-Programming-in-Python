#Check if a number is present in a list of numbers 
li_st=['1','2','3','4','5','6','7','8','9','0','10']
check=int(input("Enter your number to check : "))
if check in li_st:
    print(f"The given number {check} is IN LIST :)")
else:
    print(f"The given number {check} is NOT in LIST :(")
i=input("do you want to see the list hit enter")
if i==i:
    print("The list is = ",li_st)