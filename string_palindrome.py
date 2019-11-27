#python program to check whether a given strig is a palindrome or not.
input_string=input('Enter the input string to check whether it is a palindrome or not :')
reversed_string=input_string[::-1]
if reversed_string==input_string:
    print("the given string is a palindrome")
else:
    print("the given string is not a palindrome")
