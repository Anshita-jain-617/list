a=[105,102,107,109]
i=0
b=[]
while i<len(a):
    c=str(a[i])
    j=0
    sum=""
    sum1=""
    while j<len(c):
        if c[j]!="0":
            sum=sum+(c[j])
        else:
            sum1=sum1+(c[j])
        j+=1
    m=(sum+sum1)
    k=int(m)
    b.append(k)
    i=i+1
print(b)


        


