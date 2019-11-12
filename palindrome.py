# Palindrome program,Initially a word or a given number is said to be a palindrome  only when if you  reverse the given word or the number it gives the same word or the number even after you reverse  it.
number=int(input("enter the number which you want to check for palindrome"))
duplicate_number=number
reverse=0
while(number>0):
	remainder=number%10
	reverse=reverse*10+remainder
	number=number//10
print("the reverse of the given number is ",reverse)
if  duplicate_number==reverse:
	print("the given number is a palindrome")
else:
	print("the given number is not a palindrome")

