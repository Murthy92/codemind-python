n=int(input())
i=1
while(i):
  a=2**i
  if(a<=n):
    d1=n-a
  else:
    d2=a-n
    break
  i+=1
if(d1>d2):
    print(d2)
else:
    print(d1)