#Code goes here!
#Without string library functions
p=-1
temp=0
s=(input())
for i in s:
    if i!=s[p]:
        temp=1
        break
    p-=1
if temp>0:
    print("Not Palindrome")
else:
    print("Palindrome")