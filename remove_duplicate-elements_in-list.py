# python program to remove duplicate elements in the given list.(Here we use set concept since set does not allow duplicate elements).
list1=[]
limit=int(input('enter the limit of the list1:'))
for i in range (1,limit+1):
	values=int(input("enter the values of list1 :"))
	list1.append(values)
print(list1)
empty_set=set()
for i in list1:
	if i not in empty_set:
		empty_set.add(i) 
non_duplicate_list=list(empty_set)
print("the non duplicate elements list is ")
print(non_duplicate_list)
