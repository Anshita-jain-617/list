a=["apple","boy","custard","papaya"]
c=[]
i=0
n=int(input('enter'))
while i<len(a):
    if len(a[i])>=n:
        c.append(a[i])
    i+=1
print(c)
            