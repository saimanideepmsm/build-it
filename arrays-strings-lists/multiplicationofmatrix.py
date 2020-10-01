#Code goes here!
#Code goes here!
m1=int(input())
n1=int(input())
m2=int(input())
n2=int(input())
X=list()
Y=list()
#input 1st matrix with m1*n1
for i in range(m1):
    temp=list()
    for j in range(n1):
        temp.append(int(input()))
    X.append(temp)
print(X)
#----------------------------------------#
#input 2nd matrix with m2*n2
for i in range(m2):
    temp=list()
    for j in range(n2):
        temp.append(int(input()))
    Y.append(temp)
print(Y)
#----------------------------------------#
result=list()
r_matrixsize=m1*n2
#creating a result matrix to store the solution
for i in range(m1):
    temp=list()
    for j in range(n2):
        temp.append(0)
    result.append(temp)
print(result)
#----------------------------------------#
for i in range(len(X)):
   for j in range(len(Y[0])):
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]
for i in result:
   print(i)
#----------------------------------------#

