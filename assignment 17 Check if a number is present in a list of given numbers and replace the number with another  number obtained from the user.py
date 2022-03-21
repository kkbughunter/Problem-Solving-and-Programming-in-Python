# Check if a number is present in a list of given numbers and replace the number with another number obtained from the user

li_st=[1,2,3,4,5,6,7,8,9,0]
print("BEFORE EDIT :- ",li_st)
usernum=int(input("Enter the checking number : "))
if usernum in li_st:
    print("The number is IN LIST :) ")
    edit=int(input("Enter the adding number(IT WILL CHANGE THE NUMBER) : "))
    li_st.remove(usernum)
    li_st.append(edit)
else:
    print("The given number is not in LIST :(")
print("AFTER EDIT :- ",li_st)












