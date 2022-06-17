a=[]
for i in range(3):
    b=[]
    for j in range(3):
        j=int(input("enter number"))
        b.append(j)
    a.append(b)
print("magic")
for i in range(3):
    for j in range(3):
        print(a[i][j],end=" ")
    print()
s1=0
s2=0
for i in range(3):
    for j in range (3):
        if i==j:
            s1=s1+a[i][j]
        if i+j==3-1:
            s2=s2+a[i][j]
if s1 !=s2:
    f=1
else:
    for i in range(3):
        s3=0
        s4=0
        for j in range(3):
            s3=s3+a[i][j]
            s4=s4+a[i][j]
        if s3!=s4:
            f=1
        elif s4!=s1:
     	    f=1
        else:
            f=0
if f==0:
	print("magic square is completed")
else:
    print("not a magic square")