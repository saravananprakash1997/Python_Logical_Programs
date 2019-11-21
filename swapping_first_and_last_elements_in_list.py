# python program to swap first and last elements in the given list
empty_list=[]
list_limit=int(input("enter the limit of the list :"))
for i in range(0,list_limit):
	values_of_list=(int(input("enter the list value :")))
	empty_list.append(values_of_list)
print(empty_list)
temporary_variable=empty_list[0]
empty_list[0]=empty_list[list_limit-1]
empty_list[list_limit-1]=temporary_variable
print(empty_list)
