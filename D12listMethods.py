# different methods in List 
# Step 1: Create a list
friends = ['Mohin', 'Dilesh', 'Manish', 'Tony']
print(friends)  
# Output → ['Mohin', 'Dilesh', 'Manish', 'Tony']

# append(): Adds a new element at the END of the list
# Think: "append = add to END"
friends.append('Elon')
print(friends)
# Output → ['Mohin', 'Dilesh', 'Manish', 'Tony', 'Elon']

# insert(): Insert a value at a SPECIFIC INDEX
# Existing items shift to the right
# Think: "insert = forcefully push between"
friends.insert(1, 'Mark')
print(friends)
# Output → ['Mohin', 'Mark', 'Dilesh', 'Manish', 'Tony', 'Elon']

# pop(): Removes item by index AND returns it
# pop() removes last item if index not provided
# Think: "pop = pop out a bubble"
friends.pop()  # removes last → Elon
friends.pop(1) # removes index 1 → Mark
print(friends)
# Output → ['Mohin', 'Dilesh', 'Manish', 'Tony']

# remove(): Removes by VALUE (NOT index)
# Only removes FIRST matching value
# Think: "I know your name — come out!"
friends.remove('Tony')
print(friends)
# Output → ['Mohin', 'Dilesh', 'Manish']

# extend(): Adds MULTIPLE values at once
# IMPORTANT: extend() takes **one iterable**, so it must be inside a list/tuple
friends.extend(['Sam', 'Cade'])
print(friends)
# Output → ['Mohin', 'Dilesh', 'Manish', 'Sam', 'Cade']

# index(): Returns index of FIRST matching value
# Think: "Where is this person sitting?"
print(friends.index('Mohin')) # Output → 0

# reverse(): Reverses the entire list
# Think: "Flip the list order"
friends.reverse()
print(friends)
# Output → ['Cade', 'Sam', 'Manish', 'Dilesh', 'Mohin']

# count(): Count how many times a value appears
numbers = [2, 1, 1, 2, 3, 3, 4, 3]
print(numbers.count(3))
# Output → 3

# sort(): Sorts list in ascending order
# Works only if elements are comparable (all numbers or all strings)
numbers.sort()
print(numbers)
# Output → [1, 1, 2, 2, 3, 3, 3, 4]

# copy(): Creates a SHALLOW copy of the list
# Think: "clone the list"
new_list = friends.copy()
print(new_list)

# del: Deletes item by index, OR removes entire list
# Think: "Deletion without return, no mercy"
del friends[2] # deletes index 2 item
print(friends)

# del friends # remove entire list

# clear(): Empties the list completely
# Think: "Everybody OUT!"
friends.clear()
print(friends) # Output → []
