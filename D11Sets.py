# Sets in Python
Set1 = {1,2,3,4}
print(Set1) # Output: {1,2,3,4}

# Using set() function:
Set2 = set([1,2,2,3])
print(Set2) # Output: {1,2,3} Duplicate values are removed in Sets

# Set Operators/Operations(|,&,-,^):
SetA = {2,4,6,8}
SetB = {2,3,4,5}

# Union (All unique values of each sets):
print(SetA | SetB) # Output: {2,3,4,5,6,8}

# Intersection (Common elements of each sets):
print(SetA & SetB)

# Difference (The Elements in first set but not in other):
print(SetA - SetB) # Output: {6, 8}

# Symmetric difference (The Elements in either sets but not in both):
print(SetA ^ SetB) # Output: {3, 5, 6, 8}

# Using Set operators Functions():
SetI = {"A","B","C","D"}
SetII = {"C","D","E","F"}
# difference() Finds elements in one set that are not in another
print(SetI.difference(SetII)) # Output: {"A","B"}
print(SetII.difference(SetI)) # Output: {"E","F"}

# symmetric_difference() Finds elements in either set but not in both
# Unique values of each set Cuts-off Common values
print(SetI.symmetric_difference(SetII)) # Output: {"A","B","E","F"}

# isdisjoint() Checks if two sets have no elements in common. Returns True or False.
print(SetI.isdisjoint(SetII)) # output: True because there are Common

# issubset() Checks if all elements of one set are in another
friends1 = {"Mohin","Manny","Dihless","Pragyan"}
friends2 = {"Mohin","Manny","Dihless","Pragyan","Yuvraj","Rochak"}

print(friends1.issubset(friends2)) # Output: True because All are members of friends2
print(friends2.issubset(friends1)) # Output: False because not All are members of friends1

#issuperset() Checks if all elements of another set are in this set
buddies1 = {"Mohin","Elon","Jeff","Bill"}
buddies2 = {"Mohin","Elon"}

print(buddies1.issuperset(buddies2)) # Output:True because 1st set contains all elements of the 2nd

# add remove discard pop methods of modifying sets
set_Mod = {1,2,3,4,5}
# Applying modifications:
set_Mod.add(6)     # Adds 6 → {1, 2, 3, 4, 5, 6}
set_Mod.remove(3)  # Removes 3 → {1, 2, 4, 5, 6} else throws error if value doesn't exist
set_Mod.discard(8) # Removes 8 if exists, else does nothing
set_Mod.pop()      # Removes a random element (because unordered)

