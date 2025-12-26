# Methods of modifying a dictionary

# fromkeys() function: Creates a new dictionary using the given keys, all set to the same value
Dict1 = {"A", "B", "C"}
newDict1 = dict.fromkeys(Dict1, 0)
print(newDict1) # {'A': 0, 'B': 0, 'C': 0}

# setdefault() function: Returns the value for a key if it exists; otherwise, adds the key with a default value
grades = {'Mohin': 86}
print(grades.setdefault('Mohin', 100)) # 86 → 'Mohin' exists, so value stays
print(grades.setdefault('Tony', 100))  # 100 → 'Tony' didn’t exist, so it’s added
print(grades) # {'Mohin': 86, 'Tony': 100}

# pop() function: Removes a specific key and returns its value
grades = {'Mohin': 88, 'Tony': 100}
value = grades.pop('Mohin')
print(value)  # 88 → value of the removed key
print(grades) # {'Tony': 100} → 'Mohin' is gone

# popitem() function: Removes the last inserted key-value pair and returns it
grades = {'Mohin': 89, 'Tony': 98}
item = grades.popitem()
print(item)   # ('Tony', 98) → last item removed
print(grades) # {'Mohin': 89} → only remaining item

# get() function: Returns the value of a key, or a default value if the key doesn’t exist
grades = {'Mohin': 88}
print(grades.get('Mohin'))   # 88 → existing key
print(grades.get('Tony', 'name not found')) # name not found → key not found, so default returned

# keys() function: Returns a view of all the keys in the dictionary
grades = {'Mohin': 89, 'Tony': 98}
print(grades.keys()) # dict_keys(['Mohin', 'Tony'])

# values() function: Returns a view of all the values in the dictionary
print(grades.values()) # dict_values([89, 98])

# items() function: Returns a view of all key-value pairs as (key, value) tuples
print(grades.items()) # dict_items([('Mohin', 89), ('Tony', 98)])

sort = {"Ball":3, "Apple":1, "Cat":2}
print(dict(sorted(sort.items())))


student_info = {'Mohin':55, 'Tony':65}
newValues = {'Mohin':555,'Tony':655}

student_info.update(newValues)
print(student_info)


student_info1 = {"Id1":{"name":"Mohin", "age":22, "gender":"Male"}}
student_info2 = {"Id2":{"name":"Tony", "age":45, "gender":"Male"}}
gender = student_info1["Id1"].pop("gender")
student_info1["Id1"]["gender"] = "MALE"
print(student_info1)



