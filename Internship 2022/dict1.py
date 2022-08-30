thisdict={"key1":"Android","key2":"iOS"}


for i,j in thisdict.items():
    print(i,j)




print(thisdict)
print(len(thisdict))
print(thisdict["key1"])
allkey=thisdict.keys()
print(allkey)
allvalue=thisdict.values()
print(allvalue)
thisdict["key1"]="ABC"
print(thisdict)
thisdict["key3"]="PQR"
print(thisdict)

del thisdict
print(thisdict)
