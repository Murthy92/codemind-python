def prime(num):
    if(num==1):
        return 0
    else:
        for i in range(2,int(num**0.5)+1):
            if(num%i==0):
                return 0
    return 1
a=int(input())
if(prime(a)):
    print("prime")
else:
    print("not a prime")