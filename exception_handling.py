# Exception handling in Python.The Purpose of this concept is to run a program even after your coding has error(s),so that your program won't crash
#ZeroDivisionError
import sys
try:
	a=2
	b=0
	c=a/b
	print(c)
except:
	print("number can't be divided zero")

try:
	e=2
	f=0
	g=e/f
except:
	print("the error occured is ",sys.exc_info()[0])
# A try block can have several exception blocks

try:
	a=4
	b=0
	c=d//b
except Exception:
	print("d hasn't been defined",sys.exc_info()[0]) #first name error will occur,than if it is handled later the zro division error will be excecuted. 
except ZeroDivisionError:
	print(" number cannot be divided by zero")
print("the purpose of this statement is to explain that eventhough  the program has errors it will exceute the further satements , it is becoz of exceptio handling")  


