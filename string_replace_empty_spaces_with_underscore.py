#Python program to get an input string from the user and replace all the empty spaces with _ underscore symbol
input_string=input("enter the input string :")
print("The input string is ",input_string)
for x in input_string:
	if (x==" "):
		replaced_string=input_string.replace(" ","_")
print("The input string after replacing the empty spaces is ",replaced_string)
