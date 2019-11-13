# python program to print the largest value in the given list
number=int(input("enter the limit of the list :"))
list1=[]
for i in range(1,number+1):
	values=int(input("enter the values of the list "))
	list1.append(values)
print(list1)
largest_value=list1[0]
for j in list1:
	if j>largest_value:
		largest_value=j
print("the largest value in the given list is "+str(largest_value))
	
