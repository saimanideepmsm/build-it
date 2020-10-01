def fact(n):
    if n==1:
        return 1
    else:
        f=n*fact(n-1)
        return f
n=int(input())
c=fact(n)
print(c)