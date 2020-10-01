#Code goes here!
n=int(input())
l1=list(map(int,input().split()))
l2=sorted(l1)
print(l2[n-2])
print(l2[1])