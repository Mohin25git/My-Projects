#factorial

n=4
def call(n):
    if n>1:
        n= n*call(n-1)
    else:
        return 1
    return n
y=int(call(n))
print(y)
