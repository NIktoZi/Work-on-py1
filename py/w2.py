n=int(input())
def fact(n):
    f = 1
    for i in range(n):
        f *= i+1
    return f
 
f = fact(n)
print(f)