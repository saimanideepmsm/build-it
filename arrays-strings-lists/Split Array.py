#Code goes here!
n=int(input())
l1=list(map(int,input().split()))
#print(l1)
k=int(input())
temp1=l1[0:k]
temp2=l1[k:]
#print(temp2+temp1)
temp2=temp2+temp1
for i in temp2:
    print(i,end=" ")