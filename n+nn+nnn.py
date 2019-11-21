# Python Program to Read a Number n and Compute n+nn+nnn
number=int(input("enter the number:"))
number_converted_to_string=str(number)
temporary_variable_1=number_converted_to_string+number_converted_to_string
temporary_variable_2=number_converted_to_string+number_converted_to_string+number_converted_to_string
temporary_variable_3=int(number_converted_to_string)+int(temporary_variable_1)+int(temporary_variable_2)
print("the sum is",temporary_variable_3)
