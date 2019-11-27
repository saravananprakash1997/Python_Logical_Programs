#python program to count the number of characters and words  in the given string .
input_string=input("Enter the input String:")
character_count=0
word_count=1
for x in input_string:
    character_count=character_count+1
print("the total number of characters in the given string are :",character_count)
for i in input_string:
    if (i==" "):
        word_count=word_count+1
print("the total number of words in the given string are ",word_count)
