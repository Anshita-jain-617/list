a=[45,67,1,4,68,90,100,101,23,45,12]
i=0
max=0
max2=0
max3=0
while i<len(a):
    j=0
    while j<len(a):
        if a[j]>max:
            max=a[j]
        if a[j]>max2 and a[j]!=max:
            max2=a[j]
        if a[j]>max3 and a[j]!=max2 and a[j]!=max:
            max3=a[j]
        j+=1
    i+=1
print(max,max2,max3)    






    

