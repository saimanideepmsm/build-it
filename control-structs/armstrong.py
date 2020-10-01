n=int(input())
temp=n
s=0
while(n>0):
    p=n%10#last digit
    p=p**3
    s=s+p
    n=n//10
#print("yea boi",s)
if int(s)==temp:
    print("yes")
else:
    print("no")