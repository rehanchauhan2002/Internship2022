try:
    no1=int(input("Enter no 1"))
    no2=int(input("Enter no 2"))
    ans=no1/no2
    print(ans)
except Exception as e:
    print("Can not divide by zero",e)
finally:
    print("This is Finally run")

print("Conti...")