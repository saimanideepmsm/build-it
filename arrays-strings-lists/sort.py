#Code goes here!
n=int(input())
l=list()
for _ in range(n):
    l.append(int(input()))
l=sorted(l)
for i in l:
    print(i)
