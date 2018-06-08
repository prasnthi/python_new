with open('pandu.txt','wb+')as f1:
    for x in range(10):
        f1.write("this is my first abc%d\n" %(x+1))
with open('pandu.txt','r')as f1:
    x=f1.read()
    print(x)
    if 'this is my first abc4' in x:
        print True

