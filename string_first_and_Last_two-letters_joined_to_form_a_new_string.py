#Python Program to Form a New String Made of the First 2 and Last 2 characters From a Given String
input_string=input("Enter the input string :")
print("the given string is ",input_string)
new_string=""
count=0
for x in input_string:
    count=count+1
print("the total count is ",count)
new_string=new_string+(input_string[:2]+input_string[-2:])
print ("the newely derived string is ",new_string)
