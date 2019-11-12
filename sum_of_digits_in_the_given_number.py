# python program to add sum of the digits in the given number
number=int(input("enter the number which you want to reverse"))
sum=0
while(number>0):
	remainder=number%10
	sum=sum+remainder
	number=number//10
print("the sum of the digits in the given number is "+str(sum))
