i=-1
a=[]
b=[]
while i==-1:
    z=int(input("enter number to list1"))
    if z==0:
        break;
    else:
        a.append(z)


    while i==-1:
        z=int(input("enter number to list2"))
        if z==0:
            break;
        else:
            b.append(z)


if len(a)==len(b):
    print("list are same length",len(a))

else:
    print("list1:",len(a),"list2:",len(b))

if sum(a)==sum(b):
    print("list are same sum",sum(a))

else:
    print("list1:",sum(a),"list2:",sum(b))

for n in a:
    for z in b:
        if n==z:
            print(n,"is in both list1 at position ",a.index(n),"and in list2 at position ",b.index(n),"position")
