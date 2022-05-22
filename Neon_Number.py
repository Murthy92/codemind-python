a=int(input())
temp=a
sq=a*a
add=0
while(sq):
    rem=sq%10
    add+=rem
    sq//=10
if(temp==add):
    print("Neon Number")
else:
    print("Not Neon Number")