#n odd numbers
n1=int(input())
n2=int(input())
t=int(input())
if n1%2==0:
    n1+=1
for i in range(n1+2,n2,2):
    if t==0:
        break
    t-=1
    print(i)
#other way
n1=int(input())
n2=int(input())
t=int(input())
for i in range(n1+1,n2):
    if i%2!=0:
        print(i)
        t-=1
    if t==0:
        break