#python program to count the number of lowercase numbers in the given string.
input_string=input("Enter the input string :")
count=0
for x in input_string:
    if(x.islower()):
        count=count+1
print("the total number of lowercase letters in the given input string are :",count)
