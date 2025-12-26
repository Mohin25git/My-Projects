'''
. Write a program to accept the cost price of a bike and display the road tax to be
paid according to the following criteria:
Cost price (in Rs) Tax
>100000            15%
>50000 & <=100000  10%
<=50000             5%
'''
bike_price = int(input("enter the price of the bike: "))
if bike_price > 100000:
    print(f'road tax for bike of Rs.100000: {bike_price * 15/100}')
elif bike_price > 50000 and bike_price <=100000:
    print(f'road tax for bike for Rs.>50000 & <=100000: {bike_price * 10/100}')
elif bike_price <= 50000:
    print(f'road tax for bike for Rs.<=50000: {bike_price * 5/100}')
else:
    print("Invalid pricing!")
