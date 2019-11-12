# to print the largest number and smallest in the given list from the user
number=int(input("enter the limit of the given list :")) # 9 6 3 5 8
lists=[]
for i in range(1, number+1):
	values=int(input("enter the values of the list"))
	lists.append(values)

print(lists)
b=sorted(lists)
print(b[number-1])
