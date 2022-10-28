a=[11, 33, 50]
i=0
sum=""
while i<len(a):
    b=str(a[i])
    j=1
    while j<len(b):
        sum=str(sum)+b
        j+=1
    i+=1
print(sum)

