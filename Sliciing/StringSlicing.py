a = 'Expression'   # Our base string (10 characters total → indexes from 0 to 9)

# 1️ [::2] → Start at the beginning (index 0), go till the end, and skip every 1 character (step = 2)
print(a[::2])   # Output: Epeso

# 2️ [:] → No start, no stop → meaning “take everything” → the whole string as it is
print(a[:])     # Output: Expression

# 3️ [-2:3:-1] → Start at index -2 ('o'), move backward one step at a time till index 3 ('r'), but stop *before* 3
print(a[-2:3:-1])  # Output: osserxE

# 4️ [-3:4] → Start from index -3 ('s'), move forward till index 4 ('r')
#     But start (-3 = 7th position) is *after* 4, and step is +1 (forward)
#     → Python can’t move forward from 7 to 4 → empty string
print(a[-3:4])     # Output: (empty string)

# 5️ [-3:-4:-1] → Start at index -3 ('s'), move backward till index -4 (exclusive)
#     → Takes only one step back → captures 's'
print(a[-3:-4:-1]) # Output: s

# 6️ [-3:7:-2] → Start at -3 ('s'), move backward every 2 steps, stop before index 7
#     → Only one valid step before 7, gives same result
print(a[-3:7:-2])  # Output: s

# 7️ [1:-8] → Start at index 1 ('x'), move forward till index -8 (which is index 2)
#     → The range is tiny, so it stops right after 'x'
print(a[1:-8])     # Output: x

# 8️ [9::-10] → Start from last index (9 → 'n'), move backward 10 steps at a time
#     → Since length < 10, it only takes the first character
print(a[9::-10])   # Output: n

# 9️ [9:-10:-1] → Start from last index (9 → 'n'), move backward one step each time till before index -10
#     → This goes fully backward → reversing the string
print(a[9:-10:-1]) # Output: noisserpxE

# 10 [11::-6] → Index 11 doesn’t exist (string ends at 9), but Python treats it as “start from end”
#     → Then move backward by 6 steps, picking characters at that gap
print(a[11::-6])   # Output: nx

# 1️1️ [2:-15:-1] → Start at index 2 ('p'), move backward till index -15 (which doesn’t exist)
#     → So it goes all the way backward till start
print(a[2:-15:-1]) # Output: pxE

# 1️2️ [-15::-2] → Start way before string begins (-15), so Python starts from the beginning
#     → But step = -2 (move backward), and you can’t go backward from start → no movement
print(a[-15::-2])  # Output: (empty string)

# 1️3️ [7:-1] → Start at index 7 ('i'), go forward till index -1 ('n'), but stop right before 'n'
#     → Picks characters between them
print(a[7:-1])     # Output: io

# 1️4️ [-1:0:] → Start from the last character ('n'), no step given (so default step = +1)
#      It tries to move forward, but can’t go beyond the end → empty result
print(a[-1:0:])    # Output: (empty string)

# 1️5️ [:-1:] → Take everything from start till one step before the last character
print(a[:-1:])     # Output: Expressio

# 1️6️ [::-1] → Reverse the string completely (start to end, step = -1)
print(a[::-1])     # Output: noisserpxE

# 1️7️ [-1:7] → Start from last character ('n'), move forward till index 7
# Not possible since direction is wrong (start > stop with +1 step)
print(a[-1:7])     # Output: (empty string)

# 1️8️ [:-3:] → Take everything from start until the 3rd last character (exclusive)
print(a[:-3:])     # Output: Express

# 1️9️ [-1:0] → Start from last index ('n'), try to move forward till index 0 (with default +1 step)
# Can’t move in that direction → empty again
print(a[-1:0])     # Output: (empty string)

# Part self part AI