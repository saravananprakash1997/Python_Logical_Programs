number=int(input("enter the number which you want to reverse :"))
r=0
while number>1:
	a=number%10
	r=r*10+a
	n=number/10
print("the reverse of given nummber is"+str(r)) 


