li=[1,4,2,3,5]
l=-1
sl=-1
for i in li:
    if i>l and i>sl:
        sl=l
        l=i
    elif i>sl:
        sl=i
print(sl)

