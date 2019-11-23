# python program to find whether the given letter exists in the string which is given by the user using user defined functions.


def existing_letter(letter,string_name):
	letter=input("enter the letter which you want to check ")
	string_name=input("enter the string ")
	for i in string_name:
		if letter==i:
			print("the given letter  exists in the given string")
		else:
			print("the given lettter  does not exits in the given string")

existing_letter(letter,string_name)






