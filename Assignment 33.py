# Write a program that accepts a sentence and calculate the number of letters and digits.
 
text=input("enter the text:")
a=tuple(text)
print(a)
b=len(a)
n=0 
m=0 
for i in range (0,b,1):
    if (a[i]==' '):
        continue
    elif (a[i]=='.'):
        continue
    elif (a[i]=='0' or a[i]=='1' or a[i]=='2' or a[i]=='3' or a[i]=='4' or a[i]=='5' or a[i]=='6' or a[i]=='7' or a[i]=='8' or a[i]=='9'):
        continue
    elif (a[i]==',' or a[i]=='<' or a[i]=='>' or a[i]=='/' or a[i]=='?' or a[i]==':' or a[i]==';' or a[i]=='{' or a[i]=='}' or a[i]=='[' or a[i]==']' or a[i]=='\\' or a[i]=='|' or a[i]=='"' or a[i]=='+' or a[i]=='`' or a[i]=='~' or a[i]=='!' or a[i]=='@' or a[i]=='#' or a[i]=='$' or a[i]=='%' or a[i]=='^' or a[i]=='&' or a[i]=='*' or a[i]=='(' or a[i]==')' or a[i]=='-' or a[i]=='_' or a[i]=='=' ):
        continue
    else:
        n=n+1
print(n,"is the number of letters in a given text.")
for j in range (0,b,1):
    if (a[j]==' '):
        continue
    elif (a[j]=='.'):
        continue
    elif (a[j]=='0' or a[j]=='1' or a[j]=='2' or a[j]=='3' or a[j]=='4' or a[j]=='5' or a[j]=='6' or a[j]=='7' or a[j]=='8' or a[j]=='9'):
        m=m+1
    else:
        continue
print(m,"is the number of digits in a given text.")

print("the program was executed.")