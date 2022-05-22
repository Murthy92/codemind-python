a=int(input())
p=1
s=0
while(a):
    r=a%10
    p*=r
    s+=r
    a//=10
if(p==s):
    print("Spy Number")
else:
    print("Not Spy Number")