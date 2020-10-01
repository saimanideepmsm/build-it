#Code goes here!
m=int(input())
l1=list(map(int,input().split()))
if m==len(l1):
    print("insertion valid")
else:
    print("array index out of bound")