#Code goes here!
n=int(input())
l=list()
for _ in range(n):
    l.append(int(input()))
p=int(input())
k=int(input())
l.insert(p,k)
for i in l:
    print(i)