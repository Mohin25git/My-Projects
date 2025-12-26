'''
Inputs:
Cookie size (in cm)
Cookie temperature (in °C)

Your Task:
Write a program that:
First checks the size:
If size >= 10 cm, print "Large cookie"
Inside this block, check temperature:
If temperature > 40°C, print "Hot and Large"
Else print "Large but Cool"
Else size < 10 cm, print "Small cookie"
Inside this block, check temperature:
If temperature > 40°C, print "Small but Hot"
Else print "Small and Cool"
'''
cookie_size = int(input("Enter the cookie size in cm: "))
temperature = int(input("Cookie temperature (in °C): "))

if cookie_size >= 10:
    print("Large cookie!")
    if temperature > 40:
        print("Hot and large!")
    else:
        print("Large but Cool!")
else:
    print("Small cookie!")
    if temperature > 40:
        print("Small but hot!")
    else:
        print("Small and Cool!")
