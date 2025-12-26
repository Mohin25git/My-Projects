#2
Set1 = {23,42,65,57,78,83,29}
Set2 = {57,83,29,67,73,43,48}
# Intersection (Common elements of each sets):
newSet = Set1 & Set2
print(newSet)
# Difference (The Elements in first set but not in other):
newSet1= Set1 - newSet
print(newSet1)

#3
SetA = {27, 43, 34}
SetB = {34,93,22,27,43,53,48}
NewSet = SetA.issubset(SetB)
print(NewSet)

removed_subset = newSet - SetB
print(removed_subset)
