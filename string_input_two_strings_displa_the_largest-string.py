#python program to take two strings from the user and display the largest string.
string1=input("enter the string 1:")
string2=input("enter the string 2 ")
count_of_string_1=0
count_of_string_2=0
for x in string1:
    count_of_string_1=count_of_string_1+1
for y in string2:
    count_of_string_2=count_of_string_2+1
if count_of_string_1>count_of_string_2:
    print("The largest string is ", string1)
else:
    print("the largest string is " ,string2)
