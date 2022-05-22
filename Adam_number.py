def reverse(num):
    rev=0
    while(num):
        rev=rev*10+(num%10)
        num//=10
    return rev 
n=int(input())
sq=n*n
r=reverse(n)*reverse(n)
if(reverse(r)==sq):
    print("True")
else:
    print("False")