mydict = {
    "apple": "type of fruit",
    "tesla": "type of car",
    "pakistan": "type of country" 
}

print(mydict["tesla"]) #will print type of car

mydict["tesla"] = "type of car and color is blue" #will change tesla
print(mydict)

mydict["temp"] = 29 #will add a new key and value
print(mydict)

mydict["temp"] += 1 #will increase temp
print(mydict)

count = len(mydict) #will count the number of keys
print("There are ", count, "variables in the dict")

mydict.pop("pakistan") #will remove pakistan
print(mydict)

for key, value in mydict.items(): #will print keys against the value
    print("the key = ", key, "and the value = ", value)

for key, value in mydict.items():
    if key == "apple":
        print("the key = ", key, "and the value = ", value)
    if key == "temp":
        mydict["temp"] += 1
        print("the key = ", key, "and the value = ", mydict[key])