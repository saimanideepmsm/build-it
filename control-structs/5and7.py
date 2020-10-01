n=int(input())
for i in range(0,n):
    if i%7==0 or i%5==0:
        continue
    print(i)