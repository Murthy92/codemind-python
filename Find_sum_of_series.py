n=int(input())
add=0
for i in range(1,n+1):
    add=add+float(1/i)
print('{0:.2f}'.format(add))