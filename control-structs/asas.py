n1=int(input())
n2=int(input())
count=0
for num in range(n1+1,n2+1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
           count+=1
print(count)