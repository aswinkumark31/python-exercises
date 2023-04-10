a='a,e,i,o,u'

def vowels(b):
    count=0
    s=''
    for i in b:
        if i in a:
            count+=1
    print(count)
vowels(b=input('enter a word:'))