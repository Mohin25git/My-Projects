class Person:
    def __init__(self, name, age, address, course):
        self.name = name
        self.age = age
        self.address = address
        self.course = course

    def introduce(self):
        return f"Hello, my name is {self.name}, I am {self.age} years old. I live in {self.address}, and I study {self.course}."

no_of_people = int(input("Enter the number of people: "))

people_list = []

for i in range(no_of_people):
    print(f"\nEnter the details for person {i+1}:")
    
    # Asking user input inside the loop
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    address = input("Enter your address: ")
    course = input("Enter your course: ")
    
    # Create an instance with user input and add to the list
    person_instance = Person(name, age, address, course)
    people_list.append(person_instance)

# Introduce all people
print("\nIntroductions of everyone:")
for person in people_list:
    print(person.introduce())
