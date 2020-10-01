#Code goes here!
s=input()
v_l=["a","e","i","o","u","A","E","I","O","U"]
v=0
c=0
for i in s:
    if i in v_l:
        v+=1
    else:
        c+=1
print(v)
print(c)