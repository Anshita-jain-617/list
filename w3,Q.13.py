a=[23,44,12,54,33,13,68,90]
b=[]
i=0
while i<len(a):
    if a[i]%2!=0:
        b.append(a[i])
    i+=1
print(b)