l=int(input())
n=int(input())
for i in range(1,n+1):
    w,h=map(int,input().split())
    if(w<l or h<l):
        print("UPLOAD ANOTHER")
    else:
        if(w==h or h==w):
            print("ACCEPTED")
        else:
            print("CROP IT")