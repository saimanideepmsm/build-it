for _ in range(int(input())):
	n=int(input())
	a[0]=0
	a=list(map(int,input().split()))
	if n==1 or sum(a)<0:
		print("NO")
	elif sum==0:
		print("YES")
	else:
		for i in range(1,n+1):
			if a[i]>0:
				a[i]-=i
		if sum(a)==0:
			print("yes")
		else:
			print("NO")