n=int(input())
l=list()
for _ in range(n):
    l.append(int(input()))
even=list()
odd=list()
for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
for i in even:
    print(i)
for i in odd:
    print(i)