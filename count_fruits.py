fruits = ["apple", "banana", "cherry", "apple", "cherry", "cherry", "apple"]
a = "apple"
b = "banna"
c = "cherry"
count_apple = 0
count_banana = 0
count_cherry = 0
for f in fruits:
    if f == "apple": #or f == a
        count_apple += 1
    if f == "banana": #or f == b
        count_banana += 1
    if f == "cherry": #or f == c
        count_cherry += 1
print("Apple = ", count_apple)
print("Banana = ", count_banana)
print("Cherry = ", count_cherry)