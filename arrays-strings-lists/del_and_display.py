#Code goes here!
n=int(input())
l=list()
for _ in range(n):
    l.append(int(input()))
#print(l)
k=int(input())
l.remove(k)
for i in l:
    print(i)