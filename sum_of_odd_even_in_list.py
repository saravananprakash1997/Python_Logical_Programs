# Python program to add odd numbers in the list and even  numbers in the list seperately and display the answers seperately
list=[]
number=int(input("enter the list limit :"))
for i in range(1,number+1):
	a=int(input("enter the list elements :"))
	list.append(a)
even=0
odd=0
for i in list:
	if i%2==0:
		even=even+i
	else:
		odd=odd+i
print("the sum of even numbers in the given list is "+str(even))
print("the sum of odd numbers in the given list is ",odd)
	
	
