num=int(input())
add=0
temp=num
while(num):
    rem=num%10
    add+=rem
    num//=10
if(temp%add==0):
    print("True")
else:
    print("False")