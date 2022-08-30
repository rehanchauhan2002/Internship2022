#1)function with random argument

def randomargument(*data):
    print("ID :",data[0])
    print("Name :",data[1])
    print("Subject :",data[2])

randomargument(1,"Hitesh","Python")


#2)Function With List Argument

def randomargument(data):
    print("ID :",data[0])
    print("Name :",data[1])
    print("Subject :",data[2])

randomargument([1,"Hitesh","Python"])



#3)Function with Kwerg ** argument

def randomargument(**data):
    print("ID :",data["name"])
    print("Name :",data["subject"])

randomargument(name="Hitesh",subject="Python")




