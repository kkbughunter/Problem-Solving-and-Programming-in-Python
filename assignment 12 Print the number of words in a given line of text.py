# 12. Print the number of words in a given line of text. 
sen=input("Enter the sentence :- ")
vowels=sen.split(" ")
count=0
for i in vowels:
    count=count+1
print("The number of words in the sentence = ",count)
