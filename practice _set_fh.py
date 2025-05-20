# Q1 WAP to read the text from a given file "poems.txt"and find out wheter it contains the word 'twinkle or not'
f=open('poems.txt',)
t=f.read()
if 'twinkle'in t:
    print('twinkle is present')
else:
    print("twinkle  is not present")
    f.close()    
    

