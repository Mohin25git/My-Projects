Tuple = (1,2,3,4,5)

Result = list(Tuple)
Result[4] = '5'
print(tuple(Result))

# Sets
set1 = {1,2,3,4}
set1.add(5)
print((set1))

# pop remove discard methods
set2 = {2,4,6,8}
#set2.remove([0])
print((set2))

# What is difference, symmetric difference, isdisjoint, issubset, in sets in python

set1 - set2  # Using the '-' operator

set1.difference(set2)  # Using the difference() method


set1 ^ set2  # Using the '^' operator

set1.symmetric_difference(set2)  # Using the symmetric_difference() method


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y) # returns True if none of the items are present in both sets, otherwise it returns False.

print(z)

a = {"a", "b", "c"}
b = {"f", "e", "d", "c", "b", "a"}

c = a.issubset(b) # returns True if all items in the set exists in the specified set, otherwise it returns False.

print(c)

set4 = {1,2,2,2,2,3,4,5}
Result1 = set4.count(2)
print(Result1)

# fromkey setdefault pop popitems get keys items values

keys = ['a','b','c']
new_dict = keys.fromkeys(keys, 0)
'''
 This class method creates a new dictionary from an iterable of keys, 
 assigning each key the specified value. If value is not provided, 
 it defaults to None.
 '''
print(new_dict)

dict2 = {"name":"Mohin", "class": "AI-C", "college": "Softwarica"}
age = dict2.setdefault('age',22) #
print(dict2)

