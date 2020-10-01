#Code goes here!
m=int(input())
n=int(input())
l=list()
for i in range(m):
    temp=list()
    for j in range(n):
        temp.append(int(input()))
    l.append(temp)
print(l)