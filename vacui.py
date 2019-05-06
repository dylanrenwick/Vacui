from time import time as i
t=lambda n,x:int(n*(10**x))/10**x
c=''
k=['+','-','<','>','[',']',',','.']
while 1:
 s=i()
 input()
 e=sum([int(x)for x in str(t(i()-s,2))if x!='.'])%(len(k)+1)
 if e==len(k):
  print(c)
  break
 c+=k[e-1]