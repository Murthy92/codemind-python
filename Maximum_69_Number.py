def reverse(num):
    rev=0
    while(num):
        r=num%10
        rev=rev*10+r
        num//=10
    return rev
a=int(input())
rev=reverse(a)
m=0
c=0
while(rev):
    r=rev%10
    if(r==6 and c==0):
        r=9
        c+=1
    m=m*10+r
    rev//=10
print(m)