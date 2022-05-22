num=int(input())
for i in range(1,num+1):
    pro=1
    a=int(input())
    for j in range(a,1,-1):
        pro*=j
    print(pro)