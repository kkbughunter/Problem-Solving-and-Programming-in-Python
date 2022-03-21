#Print the number of letters, digits, whitespace, newline in a given text 
sentence=input("Type the sentence :- ")
space=0
letter=0
word=0
number=0
newline=0
Aletter=0
specialchar=0
numberlist=['1','2','3','4','5','6','7','8','9','0']
specialcharlist=['!','@','#','$','%','^','&','*','(',')','_','-','+','=','|']
wordlist=sentence.split(" ")
Sletterlist=['a','b','c','d','e','f','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
Aletterlist=['A','B','C','D','E','F','G','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


for i in wordlist:
    word+=1
for i in sentence:
    if i==" ":
        space+=1
    if i in Sletterlist:
        letter+=1
    if i in Aletterlist:
        Aletter+=1
    if i == "\n":
        newline+=1
    if i in specialcharlist:
        specialchar+=1
    if i in numberlist:
        number+=1
print("The total number of space             = ",space)
print("The total number of new line          = ",newline)
print("The total number of letter            = ",letter)
print("The number of words in the sentence   = ",word)
print("The number of special character       = ",specialchar)
print("The number of numbers in the sentence = ",number)
print("The number of caps letter in the sentence = ",Aletter)
print("I have only include ",specialcharlist)