number=int(input("enter the table number:"))
limit=int(input("enter the limit of the table:"))
for i in range (1,limit+1,1):
	print(str(number)+ "*"+str(i)+"="+str(number*i))
