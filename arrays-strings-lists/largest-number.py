#Code goes here!
#Code goes here!
n=int(input())
l=list()
for _ in range(n):
    l.append(int(input()))
#1st way
print(max(l))
#other way
mx=0
for i in l:
    if i>mx:
        mx=i
print(mx)