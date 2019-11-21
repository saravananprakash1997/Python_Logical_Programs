#Python program to find the average of the numbers in the given list
empty_list=[]
limit_of_the_list=int(input("enter the limit of the list:"))
for x in range(0,limit_of_the_list):
	values_of_the_empty_list=int(input("enter the values of the list: "))
	empty_list.append(values_of_the_empty_list)
print ("the length of the list is ",len(empty_list))
s=0
print(empty_list)
for i in range(0,len(empty_list)):
	s=s+empty_list[i]
average=s/(len(empty_list))
print ("The Average of the numbers present in the given list is :",average)
