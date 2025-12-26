#a
i = 4
j = 6
k = 8

# #b
# i = 7
# j = 3
# k = 9

# #c
# i = 7
# j = 3
# k = 10

if i < 10:
    if j > 5:
        print("Result A")
    else:
        if k % 2 == 0:
            print("Result B")
        else:
            print("result C")
else:
    if k > 10:
        if i == k:
            print("result D")
        else:
            print("Result E")
    else:
        print("result F")

 