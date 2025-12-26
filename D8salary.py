age = int(input("enter your age: "))
gender = input("enter your gender: ")
yearsService = int(input("Enter the days/years you have worked: "))
salary = int(input("Enter the base salary: "))

if yearsService > 10:
    Bonus= salary * 10/100
elif yearsService >= 6 and yearsService <= 10:
    bonus = salary * 8/100
elif yearsService < 6:
    bonus = salary * 5/100

print(f"Bonus amount: {bonus}")
print(f"actual salary: {bonus + salary}")


