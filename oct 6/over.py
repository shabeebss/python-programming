a=int(input("type the limit:"))
i=0
list2=[]
while i<a:
    z=int(input("type the number:"))
    if z>100:
        list2.append("over listed")

    else:
        list2.append(z)
    i+=1

print(list2)
