thisdict={"name":"Hitesh","subject":"Python"}

for i,j in thisdict.items():
    print(i,":",j)

print(thisdict)
print(len(thisdict))
print(type(thisdict))

thisdict["name"]="Praxware Technologies"
print(thisdict)

thisdict["key3"]="Android"
print(thisdict)
print(thisdict.keys())
print(thisdict.values())

thisdict.pop("subject")

print(thisdict)

#del thisdict
print(thisdict)