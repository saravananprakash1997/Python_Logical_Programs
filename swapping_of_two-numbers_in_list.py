# Python program to swap first and last  numbers in the given list
list1=[]
limit=int(input("enter the limit of the list1 :"))
for i in range(1,limit+1):
	values=int(input("enter the values of the list1 :"))
	list1.append(values)
print("the list which is given by the user is ",list1)
temporary=list1[0]
list1[0]=list1[limit-1]
list1[limit-1]=temporary
print("The list after swapping is ",list1)

