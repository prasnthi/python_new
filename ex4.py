f=open("god.txt","w")
for i in range(10):
    f.write("this is my first program%d\n" %(i+1))
f=open("god.txt","r")
f1=f.read()
print(f1)
f=open("god.txt","a")
f2=f.write("this is my first program")
print(f2)
f.close()
    
    
    
