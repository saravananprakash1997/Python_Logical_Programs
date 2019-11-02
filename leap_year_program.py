year=int(input("enter the year which you want to check whether it is a leap year or not"))
print("")
if (year%4==0 and year%100!=0)||(year%400==0):
	print("The given year is a Leap Year")
else:
	print("The given year is not a leap year")
