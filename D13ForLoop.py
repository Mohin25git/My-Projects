# for item in [1,2,3,4,5,6,7,8]:
#     print(item)

# # Index values of list:
# List = [1,2,3,4,5]
# # count = 0
# # for i in List:
# #     print(f'{count} {i}')
# #     count += 1

# for i in enumerate(List):
#     print(i)
    
# num = [3,4,5,6,7,8]
# for n in num:
#    if n % 2 == 0:
#     print(List[n],"is Even")
#    else:
#     print(List[n], "is Odd")

# # print odd and even in seperate list
# emptyOdd = []
# emptyEven = []
# for j in range(len(List)):
#    if List[j] % 2 == 0:
#       emptyEven.append(List[j])
#    else:
#       emptyOdd.append(List[j])
# print(f"Odd num: {emptyOdd}")
# print(f"Even num: {emptyEven}")

# # list given number and character seperately
# List2 = [1,"a",2,"b",3,"c"]
# emptyChar = []
# emptyInt = []
# for k in List2:
#    if isinstance(k, int):
#       emptyInt.append(k)
#    else:
#       emptyChar.append(k)
# print(f"Charaters are: {emptyChar}")
# print(f"Charaters are: {emptyInt}")   

# # Accept only vowels and reject others
# # Vowels = ["aeiouAEIOU"]
# # count = 0
# # Vset = set()
# # Cset = set()
# # for alpha in "Artificial Intelligence Programming":
# #    count += 1
# # print(alpha)

# input = "Artificial Intelligence Programming"
# vowel = set()
# consonant = set()
# for i in input:
#    if i in "AEIOUaeiou":
#       vowel.add(i)
#    else:
#       consonant.add(i)
# print(vowel)
# print(consonant)

# # Seperate str, int + and - in seperate sets
# input2 = [-20, -21, 22, 2, 4, "a", 2, 4]
# # Integer = set()
# # even = set()
# # positive = set()
# # negative = set()
# for i in input2:
#    if isinstance(i, int):
#       if i % 2 == 0:
#          if i > 0:
#             total += 1
# print(total)

# ask username and password give 3 attempts then block else let user enter

# for p in range(3, 0, -1): # lets entry three times
#     username = input("Enter your username: ")
#     password = input("Enter your password: ")
#     if username == "Mohin" and password == "Shakya":
#         print("Access granted!")
#         break
#     else:
#         print(f"{p-1}Attempt left")
#         continue

# Alternate Way
max_attempt = 3
for i in range(1, 4):
    userName = input("enter a username: ")
    password = input("enter a password: ")
    if userName == "Mohin" and password == "moen123":
        print("access granted!")
        break
    else:
        if i < max_attempt:
          print(f"{max_attempt-i} attempt left")
          print("Invalid username or password!")
        else:
            print("You are blocked!")
