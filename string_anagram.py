#python program to check whether the input strings are anagram are not.
string1=input("enter the string 1 :")
string2=input("enter the string 2 :")
sorted1=string1.sort()
sorted2=string2.sort()
if sorted1==sorted2:
	print("Yes,the given strings are anagrams")
else:
	print("No,the given strings are not anagrams") 
