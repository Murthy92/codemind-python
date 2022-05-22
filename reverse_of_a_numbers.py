a=int(input())
rev=0
while(a):
    rev=rev*10+(a%10)
    a//=10
print(rev)