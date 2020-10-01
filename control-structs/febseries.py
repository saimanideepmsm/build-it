n=int(input())
a=0
b=1
l=list()
l.append(a)
l.append(b)
for _ in range(n-2):
    c=a+b
    l.append(c)
    a=b
    b=c
for i in l:
    print(i,end=" ")#Code goes here!
n=int(input())
a=0
b=1
print(a,b,end=" ")
for i in range(n-2):
    c=a+b
    if i<n-3:
        print(c,end=" ")
    else:
        print(c)
    a=b
    b=c