# a=[1,2,3,4,5,6,2,3]
# i=0
# b=[]
# c=[]
# while i<len(a):
#         if a[i] not in b:
#             b.append(a[i])
#         else:
#             c.append(a[i])
#         i+=1
# print(c)


       
a=[1,2,3,4,5,6,2,3]
i=0
b=[]
c=[]
while i<len(a):
    j=i+1
    while j<len(a):
        if a[i]==a[j]:
            b.append(a[i])
        j+=1
    i+=1
print(b)
