#python program to remove odd characters using user defined functions
def remove_odd_characters():
    input_string=input("enter the input string :")
    string2=""
    for x in range (1,len(input_string)+1):
        if (x%2==0):
            string2=string2+input_string[x]
    print(string2)
remove_odd_characters()
