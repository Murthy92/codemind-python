n=int(input())
arr=list(map(int,input().strip().split()))
l=0
h=n
m=(l+h)//2
for(i)in range(h-1,m-1,-1):
    print(arr[i],end=' ')
for i in range(l,m):
    print(arr[i],end=' ')