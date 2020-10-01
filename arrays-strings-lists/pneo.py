#Code goes here!
n=int(input())
l=list()
for _ in range(n):
    l.append(int(input()))
#print(l)
p=0
n=0
e=0
o=0
for i in l:
    if i>0:
        p+=1
    else:
        n+=1
    if i%2==0:
        e+=1
    else:
        o+=1
print(p)
print(n)
print(e)
print(o)

