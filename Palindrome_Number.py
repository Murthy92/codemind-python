a=int(input())
rev=0
for i in range(1,a+1):
    b=int(input())
    rev=0
    temp=b
    while(b):
        rem=b%10
        rev=rev*10+rem
        b//=10
    if(rev==temp):
        print("True")
    else:
        print("False")