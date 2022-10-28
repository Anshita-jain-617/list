# a=['mam','dad','ans','ita','dad']
# i=0
# c=0
# while i<len(a):
#     b=a[i]
#     j=1
#     rev=''
#     while j<=len(b):
#         rev=rev+b[-j]
#         j+=1
#     if b==rev:
#         c+=1
#     i+=1
# print(c)


a=['abc','xyz','aba','1221']
i=0
c=0
while i<len(a):
    b=a[i]
    j=1
    rev=''
    while j<=len(b):
        rev=rev+b[-j]
        j+=1
    if b==rev:
        c+=1
    i+=1
print(c)










        