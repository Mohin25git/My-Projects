'''
A store gives a 20% discount if the total purchase is above RS 1000 AND the
customer is a member, or a 10% discount if the purchase is above RS 1000 but the
customer is not a member. Write a program that takes total_amount and
is_member (True/False) as input and prints the final amount after applying the
correct discount (or no discount).
'''
total_purchase = int(input("Enter the total purchase amount: "))
member = input("Are you a member(yes/no): ").lower()

if total_purchase > 1000 and member == "yes":
    discount = total_purchase * 20/100
    print(f"{total_purchase - discount}")
elif total_purchase > 1000 and member == "no":
    discount = total_purchase * 10/100 
    print(f"{total_purchase - discount}")
else:
    print("sorry no discount")

