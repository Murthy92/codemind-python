num=int(input())
maxi=-999999
while(num):
    rem=num%10
    if(rem>maxi):
        maxi=rem
    num//=10
print(maxi)