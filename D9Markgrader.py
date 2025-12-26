'''
WAP which accepts marks of four subjects and display total marks, percentage and
grade. Hint: more than 70 –> distinction, more than 60 –> first, more than 40 –>
pass, less than 40 –> fail
'''
python = int(input("enter the marks scored in Python: "))
Dmaths = int(input("Enter the marks scored in Dmaths: "))
comp_sys = int(input("enter the marks scored in Computer system: "))
Gets = int(input("enter the marks scored in GETS: "))

total_mark = python + Dmaths + comp_sys + Gets
grade = (total_mark / 400) * 100

if grade > 70:
    print("Distinction")

elif grade > 60:
    print("first division")

elif grade > 40:
    print("pass")
    
else:
    print("fail")
