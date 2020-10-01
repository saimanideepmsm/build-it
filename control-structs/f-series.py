#Code goes here!\
n=int(input())
a=0
b=1
print(a,b,end=" ")
for _ in range(n-2):
    temp=a+b
    a,b=b,temp
    print(temp,end=" ")