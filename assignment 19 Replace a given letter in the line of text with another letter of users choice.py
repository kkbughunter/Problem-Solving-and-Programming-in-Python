# Replace a given letter in the line of text with another letter of users choice 


line=input("Enter your line :- ")
letter1=input("which letter you want to replace : ")
letter2=input(" what letter you want to replace : ")

for i in line:
    if i == letter1:
        print(letter2,end="")
    else:
        print(i,end="")
















