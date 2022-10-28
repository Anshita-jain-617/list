a=[1,3,5,2,3,8]
b=[6,2,9,11,3,14]
i=0
c=0
while i<len(a):
    j=0
    c=0
    while j<len(b):
        if a[i]==b[j]:
            c+=1
            if c==1:
                print("true")
            j+=1
        i+=1
            