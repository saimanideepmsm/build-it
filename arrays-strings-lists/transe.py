m=int(input())
n=int(input())
l=list()
for i in range(m):
    temp=list()
    for j in range(n):
        temp.append(int(input()))
    l.append(temp)
transe=0
for i in range(m):
    for j in range(n):
        if i!=j:
            continue
        transe+=l[i][j]
print(transe)