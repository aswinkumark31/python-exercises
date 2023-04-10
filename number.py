x=input("enter a number:")
d={
    '1':'one',
    '2':'two',
    '3':'three',
    '4':'four',
    '5':'five',
    '6':'six',
    '7':'seven',
    '8':'eight',
    '9':'nine',
    '0':'zero'
}
l=list(x) # l=['1','2','3']

m = ''
for i in l:
    if i in d:
        m+=d[i] + ' '
print(m)
    

    
