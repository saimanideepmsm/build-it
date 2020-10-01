# cook your dish here
import numpy as np
for _ in range(int(input())):
    d=dict()
    n,k,p=map(int,input().split())
    if((k*p)<n):
        print(-1)
    elif (k==1 and n>1):
        print(-1)
    else:
        temp=0
        for i in range(n):
            if temp==k:
                temp=0
            temp+=1
            print(temp,end=" ")