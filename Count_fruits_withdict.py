fruits = ["apple", "banana", "cherry", "apple", "cherry", "cherry", "apple"]

countdict = {
    "apple": 0,
    "banana": 0,
    "cherry": 0
}
for f in fruits:
    if f == "apple":
        countdict[f] += 1 #f can be replaced by "apple" as well
    if f == "banana":
        countdict["banana"] += 1
    if f == "cherry":
        countdict["cherry"] += 1
print("Apple = ", countdict["apple"])
print("Banana = ", countdict["banana"])
print("Cherry = ", countdict["cherry"])