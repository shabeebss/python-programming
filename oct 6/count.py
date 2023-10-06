a=input("type a sentence:")
b=input("type the word to search:")
lst=a.split()
count=0
for n in lst:
    if n==b:
        count+=1

print("the number of",b ,"is",count)
