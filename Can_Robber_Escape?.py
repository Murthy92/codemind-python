n=int(input())
count=0
num_list=list(int(num)for num in 
input().strip().split())[:n]
for i in range (n):
    if(num_list[i]+1<=n):
        count+=1
if (count==n):
    print("YES")
else:
    print("NO")
