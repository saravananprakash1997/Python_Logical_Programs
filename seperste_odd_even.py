# python program to print even and odd numbers in a given list into seperate lists.
number=int(input("enter the limit of the list:"))
lists=[]
even=[]
odd=[]
for i in range(1, number+1):
	a=int(input("enter the values of the lists :"))
	lists.append(a)
for j in lists:
	if j%2==0:
		b=even.append(j)
	else:
		c=odd.append(j)
print(even)
print(odd)
