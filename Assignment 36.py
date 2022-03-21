# write a program to compute the frequency of the words from the input 


line =input("Enter Text:")
l=line.split()
d = {}   
for i in l:
    if i not in d.keys():
        d[i]=0
    d[i]=d[i]+1
print(d)