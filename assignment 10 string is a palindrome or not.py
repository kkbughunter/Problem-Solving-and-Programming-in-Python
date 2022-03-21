#check whether a given string is a palindrome or not
                                
w1=input("Enter the word = ")                         
w2=w1[::-1]                                            
if w1==w2:                                                  
    print("The given word is palindrome",w1)               
else:                                                       
    print(f"The given word is Not palindrome {w1} != {w2}") 
