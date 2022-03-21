#print the reverse of a given numbers

#using string
name=input("Enter the text = ")
print("the reverse of a given numbers is = ",name[::-1])   

#using integer
num=int(input("Enter the number = "))
tot=len(str(num))
for i in range(0,tot):
    dig=num%10
    num=num//10
    print(dig,end="")



# :: how it working
# [ start : stop : jump ]
# where you want to start that give in first place 
# where you want to stop that give in second place
# where you want to jump that give in third place





"""
# example for start this will start in 2
name=input("Enter the text = ")
print("the reverse of a given numbers is = ",name[2::])"""
     
"""
# example for stop this will start in 3
name=input("Enter the text = ")
print("the reverse of a given numbers is = ",name[:3:])"""

"""
# example for jump this will start in 2
name=input("Enter the text = ")
print("the reverse of a given numbers is = ",name[::2])"""






