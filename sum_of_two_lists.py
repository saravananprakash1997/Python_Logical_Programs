list1=[]
number=int(input("enter the limt of the list1 :"))
for i in range(1,number+1):
  values=int(input("enter the values of the list1:"))
  list1.append(values)
print(list1)
list2=[]
number=int(input('enter the limit of list2:'))
for i in range(1,number+1):
  values2=int(input('enter the values of list2:'))
  list2.append(values2)
print(list2)
total=[]
for i in range(number):
  total.append(list1[i]+list2[i])
print("The sum of two lists are"total)
