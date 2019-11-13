# merge two lists and sort them
limit1=int(input("enter the limit of the list1 :"))
list1=[]
for i in range(1, limit1+1):
	input1=int(input("enter the list values :"))
	list1.append(input1)
print(list1)
limit2=int(input("enter the limit of list2 :"))
list2=[]
for j in range(1, limit2+1):
	input2=int(input("enter the list values :"))
	list2.append(input2)
print(list2)
for k in list2:
	list1.append(k)
print(list1)
list1.sort()
print(list1)
	 
