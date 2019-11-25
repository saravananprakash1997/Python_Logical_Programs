#Python program to extract mail id and mobile number present from  the given string
import re 
string_name="""The mobile number of John is 8939233505 , whose mail id is johnstephen@yahoo.co.in.
He also have another mobile number which is 7418609004  and his alternate ,mail id is stephenjohn@google.co.in""" 
a=re.findall(r"\d{10}",string_name)
b=re.findall(r"\S+@\S+",string_name)
print(a,b)
