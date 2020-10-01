a=int(input())
b=int(input())
gdc=0
for i in range(1,min(a,b)):
    if a%i==0 and b%i==0:
        gdc=i
print(gcd)
#other way
import math
a=int(input())
b=int(input())
print(math.gcd(a,b))