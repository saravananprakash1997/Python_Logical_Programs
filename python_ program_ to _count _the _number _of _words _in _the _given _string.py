#python program to count the number of words in the given string.
input_string=input("enter the input string :")
word_to_be_counted=input("enter the word to be counted :")
list1=[]
word_count=0
list1=input_string.split(" ")
for x in list1:
    if (x==word_to_be_counted):
        word_count=word_count+1
print ('the total number of ',word_to_be_counted," word in the given input string is ",word_count)
