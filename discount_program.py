product_name="CRICKET BAT"
print(product_name)
print("")
quantity=int(input("Enter the nuber of quantity:"))
price=int(input("Enter the price of the product:"))
cost=price*quantity
print("")
if quantity==1:
	print(cost)
elif quantity==2:
	discount=cost*(20/100)
	cost=cost-discount
	print(cost)
elif quantity==3:
	discount=cost*(30/100)
	cost=cost-discount
	print(cost)
elif quantity>3: 
	discount=cost*(40/100)
	cost=cost-discount
	print(cost)
else:
	print("This discount is valid only for few days,HURRY UP and become a star cricketer")



