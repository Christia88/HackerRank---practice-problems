def print_rangoli(size):
        al="abcdefghijklmnopqrstuvwxyz"
        let=size-1
        tot=(let*4)+1
        str1=""
        str2=""
        for i in range(0,size):   #this works
            str1=str1+al[i]
        str1=str1[::-1]
        li=tot-1
        g=int(li/2)
        
        for i in range(0,size-1):
            for k in range(0,g):
                print("-",end="")
                str2=str2+"-"
            g=g-2
            if i==0:
                print(str1[i],end="")
            else:
                for j in range(0,i):
                    print(str1[j],end="")
                    print("-",end="")
                    str2=str2+str1[j]+"-"
                print(str1[j+1],end="")
    
            str2=str2[::-1]
            print(str2)
            str2=""
        str2=""
        for i in range(0,size):
            if i<size-1:
                print(str1[i],end="")
                print("-",end="")
                str2=str2+str1[i]+"-"
            else:
                print(str1[i],end="")
                str2=str2[::-1]
                print(str2)
        g=2
        str2=""
        m=size-2
        for i in range(0,size-1):
            for k in range(0,g):
                print("-",end="")
                str2=str2+"-"
            g=g+2
            if i==size-2:
                print(str1[0],end="")
            else:
                for j in range(0,m):
                    print(str1[j],end="")
                    print("-",end="")
                    str2=str2+str1[j]+"-"
                print(str1[j+1],end="")
                m=m-1
            str2=str2[::-1]
            print(str2)
            str2=""

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
