# 18. Replace a word in the given line of text with another word 


line=input("Enter your line :- ")
letter1=input("which letter you want to replace : ")
letter2=input(" what letter you want to replace : ")
list1=line.split(" ")
for i in list1:
    if i == letter1:
        print(letter2,end=" ")
    else:
        print(i,end=" ")


