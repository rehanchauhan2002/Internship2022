double=lambda x: x * 2

print(double(10))


mylist=[1,5,4,6,8,11,3,12]
newlist=list(filter(lambda  x:(x%2==0),mylist))
print(newlist)