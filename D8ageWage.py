age = (input("Enter your age: "))
gender = (input("Enter your gender: "))
no_of_workdays = int(input("Enter the days you worked: "))

if age >= 18 and age < 30:
     if gender == "m":
          wagesPerDay = no_of_workdays * 700
          print(f"(wagesPerDay)")
     else:
        wagesPerDay = no_of_workdays * 750
        print(f"(wagesPerDay)")
elif age >= 30 and age <= 40:
     if gender == "m":
      wagesPerDay = no_of_workdays * 800
      print(f"(wagesPerDay)")
     else:
      wagesPerDay = no_of_workdays * 850

else:
    print("Invalid age")


     