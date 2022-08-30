
f1=open("file1.txt","w")
f1.write("This is Python File Example")
f1.close()
print("File Created")

f2=open("file1.txt","r")
#print(f2.readlines())

for i in f2:
    print(i)

f3=open("file1.txt","a")
f3.write("this is new content added")
f3.close()

f4=open("file1.txt","r")
print(f4.readlines())






