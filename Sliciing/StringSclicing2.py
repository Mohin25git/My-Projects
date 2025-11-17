programming_language = 'python programming'
#        -18 -17 -16 -15 -14 -13         -11 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1
       
# Logic:   p   y   t   h   o   n   |-12|   p   r  o   g   r   a   m   m   i   n   g

#          0   1   2   3   4   5   | 6 |   7   8  9  10  11  12  13  14  15  16  17

# Our base string → total 18 characters
# Index range: 0 → 17 (left to right), -1 → -18 (right to left)

print(programming_language[6])       
# Index 6 → the 7th character → this is the space between 'python' and 'programming'

print(programming_language[-12])     
# Negative index -12 also lands on the same space → prints ' '

print(programming_language[0])       
# First character of the string → 'p'

print(programming_language[-1])      
# Last character of the string → 'g'

print(programming_language[9])       
# Index 9 → character 'o' inside the word 'programming'

# -------------------------------
# 2. Forward & Reverse Full String
# -------------------------------

print(programming_language[::1])     
# Step +1 → move normally from start to end → prints whole string

print(programming_language[::-1])    
# Step -1 → walk backward through the string → gives full reverse

# -------------------------------
# 3. Partial Slices (Start or End)
# -------------------------------

print(programming_language[7:])      
# Start at index 7 and go to end → 'programming'

print(programming_language[:6])      
# From start until BEFORE index 6 → 'python'

print(programming_language[-11:])    
# From index -11 (which is the 'p' of 'programming') to end → 'programming'

# -------------------------------
# 4. Step Sizes – Skipping Characters
# -------------------------------

print(programming_language[0:18:2])  
# Take every 2nd character → skip one each time → 'pto rgamn'

print(programming_language[1:18:3])  
# Start at index 1 ('y'), jump 3 steps at a time → 'yhpgai'

print(programming_language[-18::4])  
# Start from index -18 (same as 0) and take every 4th char → 'ph r'

print(programming_language[::5])     
# Every 5th character of the entire string → 'poai'

print(programming_language[::-3])    
# Move backwards, picking every 3rd character → 'ggr rnpo'

# -------------------------------
# 5. Mid-Range Substrings
# -------------------------------

print(programming_language[2:15])    
# From index 2 ('t') up to before index 15 → 'thon program'

print(programming_language[-16:-3])  
# Same section using negative indexes → 'thon program'

print(programming_language[7:18])    
# From index 7 to end → 'programming'

# -------------------------------
# 6. Reverse Ranges – Moving Backwards
# -------------------------------

print(programming_language[:10:-1])    
# Go backwards starting from the end until BEFORE index 10 → 'gnimmarg'

print(programming_language[-1:-10:-2]) 
# Start at last char ('g'), move backwards skipping 2 → 'gmrp'

print(programming_language[::2])       
# Every 2nd char of whole string → 'pto rgamn'

print(programming_language[1::2])      
# Start at index 1 and take every 2nd → 'yhnpormig'

# -------------------------------
# 7. Complex Start/Stop/Step Combos
# -------------------------------

print(programming_language[3:18:4])   
# From index 3 ('h'), jump 4 each time → 'hrpi'

print(programming_language[-15:18:3]) 
# From negative index -15 ('h'), jump by 3 → 'hpgai'

print(programming_language[-1::-1])   
# Full reverse again → 'gnimmargorp nohtyp'

print(programming_language[0:6])      
# First six characters → 'python'

print(programming_language[7:18])     
# Characters from index 7 to end → 'programming'

print(programming_language[-18:-12])  
# From -18 (same as index 0) to before -12 → first 6 chars → 'python'

print(programming_language[-11:])     
# Last 11 characters → 'programming'

print(programming_language[6:7])      
# Single index slice → only character at 6 → ' ' (space)

print(programming_language[:])        
# Print entire string → 'python programming'

print(programming_language[::])       
# Same as above → whole string printed again

# -------------------------------
# 8. More Slicing Variations
# -------------------------------

print(programming_language[0:18:1])    
# Full string normally one-by-one → 'python programming'

print(programming_language[-18:18])    
# From -18 (start) to end → full string

print(programming_language[5:-5])      
# From index 5 ('n') to before last 5 chars → 'n progr'

print(programming_language[-10:-1])    
# From -10 ('r') to before -1 ('g') → 'rogrammin'

print(programming_language[-1:-19:-1]) 
# Full reverse again using full negative range → 'gnimmargorp nohtyp'

print(programming_language[17::-1])    
# Start at last index (17) and reverse to the start → 'gnimmargorp nohtyp'

#print(programming_language[:0::-1])     
# Reverse everything EXCEPT index 0 → 'gnimmargorp nohty'

print(programming_language[10:0:-2])    
# Going backwards from index 10 skipping 2 each time → 'arnopy'

print(programming_language[0:18:3])     
# Every 3rd character from start → 'ph rga'

print(programming_language[1:18:4])     
# Every 4th character starting at index 1 → 'y oai'

print(programming_language[-17:-1:2])   
# From -17 ('y') to -1 ('g'), jumping 2 → 'yhnpormig'

print(programming_language[-18:0:2])    
# Invalid direction: going forward but stop=0 (behind start) → returns empty string ''

print(programming_language[::7])        
# Every 7th character: indexes → 0 ('p'), 7 ('p'), 14 ('m') → 'ppm'

value = 5
print(f"{value}*{value}") # 5*5 = 25

a = 10
b = 20
print(f'{10*b}') # output: 10 * 20 = 200

#print('{} {c} {}'.format(b, c=10, a)) # Output: syntax error, 
                                      # In Python, all positional arguments must come before any keyword arguments
                                      # in here b and a are positional arguement c is keyword arguement

#print('{b}'.format(b,a)) # Output: key error, due to python expecting b=20 in .format()

print('{0} {}'.format(b, a)) # {0} → first argument b (20)
                             # {}  → next unused argument a (10)
                             # Output: 20 10

print('{0} {0} {0}'.format(b, a)) # {0} refers to the first argument in .format(), which is b = 20
                                  # Since all three placeholders are {0}, the same value is repeated thrice
                                  # Output: 20 20 20

#print('{0} {1} {2}'.format(b, a, c=10)) # {0} → first argument = b = 20
                                        # {1} → second argument = a = 10
                                        # {2} → third positional argument (not provided)
                                        # Keyword 'c=10' can't be used as {2} — needs {c} only
                                        # IndexError: Replacement index 2 out of range

print('{0} {c} {}'.format(b, a, c=10)) # Output: 20 10 10, b is {0}, a is {1}, c=10 is {2}
                                       # so, in {0}: b value 10 will be assigned, then {c} then {1}: a 
                                       # will be assigned in the empty slot

#print('{0} {0} {0}'.format(b, a, c=10, c=40)) # Output: Error, Python does not allow duplicate keyword arguments in .format()
                                              # in this case c is repeated twice

# Logic Understood by self and done with AI
