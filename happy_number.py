a=int(input())
while(a>=10):
    sum=0
    while(a):
        r=a%10
        sq=r*r
        sum+=sq
        a//=10
    a=sum
if(sum==7 or sum==1):
    print("True")
else:
    print("False")