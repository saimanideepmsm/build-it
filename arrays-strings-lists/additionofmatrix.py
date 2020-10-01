#Code goes here!
m1=int(input())
n1=int(input())
m2=int(input())
n2=int(input())
l1=list()
l2=list()
for i in range(m1):
    temp=list()
    for j in range(n1):
        temp.append(int(input()))
    l1.append(temp)
for i in range(m2):
    temp=list()
    for j in range(n2):
        temp.append(int(input()))
    l2.append(temp)
#print(l1)
#print(l2)
l3=list()
for i in range(m1):
    temp=list()
    for j in range(n1):
        temp.append(l1[i][j]+l2[i][j])
    l3.append(temp)
print(l3)