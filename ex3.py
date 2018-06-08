def main():
    f=open("pras.txt","w+")
    f.write("this is my program\n")
    f.write("in this program i am going to\n ")
    f.write("discuss about file handling concepts")
    f=open("pras.txt","r")
    f1=f.read()
    print(f1)
    f.close()
if __name__ == "__main__":
    main()
    
