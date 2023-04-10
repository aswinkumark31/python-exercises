a="st55ka{{23"
count=0
count2=0
count3=0
for i in a:
    print(i)
    if i.isalpha():
        count+=1
    elif i == '{':
        count3+=1
    else:
        count2+=1
print(count,count2,count3)
