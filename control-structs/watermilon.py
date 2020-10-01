from itertools import product
def all_repeat(str1, rno):
  chars = list(str1)
  results = []
  for c in product(chars, repeat = rno):
      d=tuple(list(sorted(c)))
      results.append(d)
  return results
m,k=map(int,input().split())
m_l=list()
d=""
dic=dict()
for i in range(1,m+1):
    temp=0
    dic=dict()
    d=d+str(i)
    c=all_repeat(d,i)
    for x in c:
        dic[x]=dic.get(x,0)+1
    for x in dic.values():
        temp+=(x/len(dic))
    m_l.append(temp)
print(m_l)
    