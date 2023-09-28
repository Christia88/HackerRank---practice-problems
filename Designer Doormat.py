x,z=input().split()
x=int(x)
z=int(z)
b=int((x-1)/2)
d=b+1
if x%2!=0 and z/3==x:
    for i in range(1,d):
        j=x-((2*(i-1))+1)
        p=int(j/2)
        for k in range(0,p):
            print("---",end="")
        y=x-(p*2)
        for l in range(0,y):
            print('.|.',end="")    
        for k in range(0,p):
            print("---",end="")
        print("")
    h=int(((x*3)-7)/2)
    for i in range(0,h):
        print('-',end="")
    print("WELCOME",end="")
    for i in range(0,h):
        print('-',end="")
    print("")
    for i in range(1,d):
        for m in range(0,i):
            print('---',end="")
        q=x-(i*2)
        for k in range(0,q):
            print('.|.',end="")
        for m in range(0,i):
            print('---',end="")
        print("")
