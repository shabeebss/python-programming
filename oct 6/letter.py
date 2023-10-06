lst=["vinayak","Mubaris","sanjay","irfan"]
count=0
print(lst)
a=input("type the letter to search:")
for n in lst:
    for f in n:
        if f==a:
            count+=1

print("the number of",a,"is",count)
