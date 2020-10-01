#Code goes here!
n=int(input())
l1=list(map(int,input().split()))
di=dict()
for i in l1:
    di[i]=di.get(i,0)+1
#print(di)
for i,j in di.items():
    if j>1:
        print("%d-%d"%(i,j),end="\n")