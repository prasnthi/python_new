def main():
    f=open("20.py","w+")
    for x in range(10):
        f.write("I AM THE LINE NO %d\n" %(x+1))
    f=open("20.py","ab+")
    f.write("HEY HAI THIS IS PRASHANTHI")
    f=open("20.py","r")
    x=f.read()
    y=f.readline()
    z=f.readlines()
    print(x)
    print(y)
    print(z)
if __name__ == "__main__":
    main()
