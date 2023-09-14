a=input().split()
b=input().split()
    
l3=[]
st=""
l4=[]
for i in a:
    for j in b:
        l4.append(i)
        l4.append(j)
        l3.append(l4)
        l4=[]
               
for i in l3:
    d=i[0]
    c=i[1]
    print(f"({d}, {c}) ",end="") 
