#count the number of vowles in the given string
string=input("enter the the string:")
count=0
vowels=set("aeiou")
for i in string:
  if i in vowels:
    count=count+1
print("the count is",count)
