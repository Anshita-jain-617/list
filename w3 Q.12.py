a = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
b=[]
i=0
while i<len(a):
    if i!=0 and i!=4 and i!=5:
        b.append(a[i])
    i+=1
print(b)