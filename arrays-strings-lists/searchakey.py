#Code goes here!
#Search a Key
n=int(input())
l=list()
for i in range(n):
    l.append(int(input()))
k=int(input())
if k in l:
    print("Found")
else:
    print("Not Found")
