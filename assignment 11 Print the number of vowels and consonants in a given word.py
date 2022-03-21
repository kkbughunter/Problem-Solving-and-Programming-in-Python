# Print the number of vowels and consonants in a given word. 

inp=input("enter the character to check vowel or not = ")
count1=0
count2=0
letter=["a","e","i","o","u"]
for i in inp:
    if i in letter:
        count1=count1+1
    else:
        count2=count2+1

print("The total number of vowels in word is = ",count1)
print("The total number of consonants in word is = ",count2)

